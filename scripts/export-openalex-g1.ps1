[CmdletBinding()]
param()

$ErrorActionPreference = 'Stop'
$ProgressPreference = 'SilentlyContinue'

[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12

$query = '("artificial intelligence" AND ethics AND medicine AND Vietnam)'
$filter = 'from_publication_date:2024-01-01,to_publication_date:2024-01-07'
$selectFields = @(
    'id',
    'doi',
    'display_name',
    'publication_year',
    'publication_date',
    'type',
    'language',
    'ids',
    'primary_location',
    'authorships'
)
$perPage = 25
$apiBase = 'https://api.openalex.org/works'

$researchRoot = [IO.Path]::GetFullPath((Join-Path $PSScriptRoot '..'))
$artifactDir = [IO.Path]::GetFullPath(
    (Join-Path $researchRoot 'artifacts\g1-openalex-access')
)
$expectedArtifactDir = [IO.Path]::GetFullPath(
    (Join-Path $PSScriptRoot '..\artifacts\g1-openalex-access')
)

if ($artifactDir -ne $expectedArtifactDir) {
    throw "Artifact directory resolution mismatch: $artifactDir"
}

if (-not (Test-Path -LiteralPath $artifactDir -PathType Container)) {
    New-Item -ItemType Directory -Path $artifactDir | Out-Null
}

$artifactDir = (Resolve-Path -LiteralPath $artifactDir).Path

function Resolve-ContainedPath {
    param(
        [Parameter(Mandatory)]
        [string]$Root,

        [Parameter(Mandatory)]
        [string]$RelativePath
    )

    $resolvedRoot = [IO.Path]::GetFullPath($Root)
    $rootPrefix = $resolvedRoot.TrimEnd(
        [IO.Path]::DirectorySeparatorChar,
        [IO.Path]::AltDirectorySeparatorChar
    ) + [IO.Path]::DirectorySeparatorChar
    $candidate = [IO.Path]::GetFullPath(
        (Join-Path $resolvedRoot $RelativePath)
    )
    if (-not $candidate.StartsWith(
            $rootPrefix,
            [StringComparison]::OrdinalIgnoreCase
        )) {
        throw "Refusing path outside validated target $resolvedRoot`: $candidate"
    }
    return $candidate
}

function ConvertTo-NonNegativeInt64 {
    param(
        [Parameter(Mandatory)]
        [object]$Value,

        [Parameter(Mandatory)]
        [int]$PageNumber
    )

    $isInteger = (
        $Value -is [byte] -or
        $Value -is [sbyte] -or
        $Value -is [int16] -or
        $Value -is [uint16] -or
        $Value -is [int32] -or
        $Value -is [uint32] -or
        $Value -is [int64] -or
        $Value -is [uint64]
    )
    if (-not $isInteger) {
        throw "Page $PageNumber meta.count is not an integer."
    }

    try {
        $count = [Convert]::ToInt64($Value)
    }
    catch {
        throw "Page $PageNumber meta.count is outside the Int64 range."
    }
    if ($count -lt 0) {
        throw "Page $PageNumber meta.count must be non-negative."
    }
    return $count
}

function Get-ValidatedPageData {
    param(
        [Parameter(Mandatory)]
        [object]$Payload,

        [Parameter(Mandatory)]
        [int]$PageNumber
    )

    if ($Payload -isnot [Collections.IDictionary]) {
        throw "Page $PageNumber JSON root is not an object/hash."
    }
    if (-not $Payload.Contains('meta') -or -not $Payload.Contains('results')) {
        throw "Page $PageNumber lacks required meta/results properties."
    }

    $meta = $Payload['meta']
    if ($meta -isnot [Collections.IDictionary]) {
        throw "Page $PageNumber meta is not an object/hash."
    }
    if (-not $meta.Contains('count')) {
        throw "Page $PageNumber meta lacks count."
    }
    if (-not $meta.Contains('next_cursor')) {
        throw "Page $PageNumber meta lacks next_cursor."
    }

    $metaCount = ConvertTo-NonNegativeInt64 `
        -Value $meta['count'] `
        -PageNumber $PageNumber
    $results = $Payload['results']
    if ($results -isnot [Array]) {
        throw "Page $PageNumber results is not an array/collection."
    }

    $nextCursor = $meta['next_cursor']
    if (
        $null -ne $nextCursor -and
        (
            $nextCursor -isnot [string] -or
            [string]::IsNullOrWhiteSpace($nextCursor)
        )
    ) {
        throw "Page $PageNumber next_cursor must be null or a non-empty string."
    }

    return [pscustomobject]@{
        MetaCount = $metaCount
        Results = $results
        NextCursor = $nextCursor
    }
}

function Assert-SnapshotIntegrity {
    param(
        [Parameter(Mandatory)]
        [string]$SnapshotDir
    )

    $manifestFile = Resolve-ContainedPath `
        -Root $SnapshotDir `
        -RelativePath 'manifest.csv'
    $checksumsFile = Resolve-ContainedPath `
        -Root $SnapshotDir `
        -RelativePath 'checksums.sha256'
    if (-not (Test-Path -LiteralPath $manifestFile -PathType Leaf)) {
        throw "Snapshot is missing manifest.csv."
    }
    if (-not (Test-Path -LiteralPath $checksumsFile -PathType Leaf)) {
        throw "Snapshot is missing checksums.sha256."
    }

    $pageFiles = @(
        Get-ChildItem -LiteralPath $SnapshotDir -File -Filter 'page-*.json' |
            Sort-Object Name
    )
    $manifestRows = @(Import-Csv -LiteralPath $manifestFile)
    if ($pageFiles.Count -ne $manifestRows.Count) {
        throw (
            "Snapshot page count $($pageFiles.Count) does not match " +
            "manifest rows $($manifestRows.Count)."
        )
    }

    $checksumMap = @{}
    $checksumLines = @(
        Get-Content -LiteralPath $checksumsFile |
            Where-Object { -not [string]::IsNullOrWhiteSpace($_) }
    )
    if ($checksumLines.Count -ne ($pageFiles.Count + 1)) {
        throw "Snapshot checksum entry count is invalid."
    }
    foreach ($line in $checksumLines) {
        if ($line -notmatch '^([0-9a-fA-F]{64})  (.+)$') {
            throw "Malformed checksum entry: $line"
        }
        $name = $Matches[2]
        if ($checksumMap.ContainsKey($name)) {
            throw "Duplicate checksum entry for $name."
        }
        $checksumMap[$name] = $Matches[1].ToLowerInvariant()
    }

    foreach ($pageFile in $pageFiles) {
        $rowsForPage = @(
            $manifestRows | Where-Object { $_.filename -eq $pageFile.Name }
        )
        if ($rowsForPage.Count -ne 1) {
            throw "Manifest must contain exactly one row for $($pageFile.Name)."
        }
        $actualHash = (
            Get-FileHash -LiteralPath $pageFile.FullName -Algorithm SHA256
        ).Hash.ToLowerInvariant()
        if ($rowsForPage[0].sha256 -ne $actualHash) {
            throw "Manifest SHA256 mismatch for $($pageFile.Name)."
        }
        if (
            -not $checksumMap.ContainsKey($pageFile.Name) -or
            $checksumMap[$pageFile.Name] -ne $actualHash
        ) {
            throw "Checksum file mismatch for $($pageFile.Name)."
        }
    }

    $manifestHash = (
        Get-FileHash -LiteralPath $manifestFile -Algorithm SHA256
    ).Hash.ToLowerInvariant()
    if (
        -not $checksumMap.ContainsKey('manifest.csv') -or
        $checksumMap['manifest.csv'] -ne $manifestHash
    ) {
        throw "Checksum file mismatch for manifest.csv."
    }
}

function Commit-StagedSnapshot {
    param(
        [Parameter(Mandatory)]
        [string]$StagingDir,

        [Parameter(Mandatory)]
        [string]$TargetDir
    )

    $backupName = '.backup-' + [Guid]::NewGuid().ToString('N')
    $backupDir = Resolve-ContainedPath `
        -Root $TargetDir `
        -RelativePath $backupName
    New-Item -ItemType Directory -Path $backupDir | Out-Null

    $currentFiles = [Collections.Generic.List[IO.FileInfo]]::new()
    Get-ChildItem -LiteralPath $TargetDir -File -Filter 'page-*.json' |
        ForEach-Object { $currentFiles.Add($_) }
    foreach ($name in @('manifest.csv', 'checksums.sha256')) {
        $path = Resolve-ContainedPath -Root $TargetDir -RelativePath $name
        if (Test-Path -LiteralPath $path -PathType Leaf) {
            $currentFiles.Add((Get-Item -LiteralPath $path))
        }
    }

    $stagedFiles = [Collections.Generic.List[IO.FileInfo]]::new()
    Get-ChildItem -LiteralPath $StagingDir -File -Filter 'page-*.json' |
        Sort-Object Name |
        ForEach-Object { $stagedFiles.Add($_) }
    foreach ($name in @('manifest.csv', 'checksums.sha256')) {
        $path = Resolve-ContainedPath -Root $StagingDir -RelativePath $name
        $stagedFiles.Add((Get-Item -LiteralPath $path))
    }

    $backedUpNames = [Collections.Generic.List[string]]::new()
    $installedNames = [Collections.Generic.List[string]]::new()
    try {
        foreach ($file in $currentFiles) {
            $destination = Resolve-ContainedPath `
                -Root $backupDir `
                -RelativePath $file.Name
            Move-Item -LiteralPath $file.FullName -Destination $destination
            $backedUpNames.Add($file.Name)
        }

        foreach ($file in $stagedFiles) {
            $destination = Resolve-ContainedPath `
                -Root $TargetDir `
                -RelativePath $file.Name
            Move-Item -LiteralPath $file.FullName -Destination $destination
            $installedNames.Add($file.Name)
        }

        Assert-SnapshotIntegrity -SnapshotDir $TargetDir
    }
    catch {
        $commitError = $_
        $rollbackErrors = [Collections.Generic.List[string]]::new()

        foreach ($name in $installedNames) {
            $installedPath = Resolve-ContainedPath `
                -Root $TargetDir `
                -RelativePath $name
            try {
                if (Test-Path -LiteralPath $installedPath -PathType Leaf) {
                    Remove-Item -LiteralPath $installedPath -Force
                }
            }
            catch {
                $rollbackErrors.Add(
                    "Could not remove staged $name`: $($_.Exception.Message)"
                )
            }
        }

        foreach ($name in $backedUpNames) {
            $backupPath = Resolve-ContainedPath `
                -Root $backupDir `
                -RelativePath $name
            $restorePath = Resolve-ContainedPath `
                -Root $TargetDir `
                -RelativePath $name
            try {
                if (Test-Path -LiteralPath $restorePath) {
                    throw "Restore target already exists: $restorePath"
                }
                Move-Item -LiteralPath $backupPath -Destination $restorePath
            }
            catch {
                $rollbackErrors.Add(
                    "Could not restore $name`: $($_.Exception.Message)"
                )
            }
        }

        if ($rollbackErrors.Count -gt 0) {
            throw (
                "Snapshot commit failed and rollback was incomplete. " +
                "Commit error: $($commitError.Exception.Message) " +
                "Rollback errors: $($rollbackErrors -join '; ') " +
                "Backup retained at $backupDir"
            )
        }

        try {
            Remove-Item -LiteralPath $backupDir -Recurse -Force
        }
        catch {
            Write-Warning "Rollback succeeded; could not remove $backupDir."
        }
        throw $commitError
    }

    try {
        Remove-Item -LiteralPath $backupDir -Recurse -Force
    }
    catch {
        Write-Warning (
            "Snapshot committed; backup cleanup failed and was retained at " +
            "$backupDir."
        )
    }
}

function Encode-QueryValue {
    param(
        [AllowEmptyString()]
        [string]$Value
    )

    return [Uri]::EscapeDataString($Value)
}

$stagingName = '.staging-' + [Guid]::NewGuid().ToString('N')
$stagingDir = Resolve-ContainedPath `
    -Root $artifactDir `
    -RelativePath $stagingName
New-Item -ItemType Directory -Path $stagingDir | Out-Null
$stagingDir = (Resolve-Path -LiteralPath $stagingDir).Path

$manifestPath = Resolve-ContainedPath `
    -Root $stagingDir `
    -RelativePath 'manifest.csv'
$checksumsPath = Resolve-ContainedPath `
    -Root $stagingDir `
    -RelativePath 'checksums.sha256'
$downloadTempPath = Resolve-ContainedPath `
    -Root $stagingDir `
    -RelativePath '.page-download.tmp'

$cursor = '*'
$seenCursors = [Collections.Generic.HashSet[string]]::new(
    [StringComparer]::Ordinal
)
$seenIds = [Collections.Generic.HashSet[string]]::new(
    [StringComparer]::Ordinal
)
$duplicateCount = 0
$pageNumber = 0
$cumulativeResults = 0
$expectedMetaCount = $null
$manifestRows = [Collections.Generic.List[object]]::new()

try {
    while ($null -ne $cursor) {
        if (-not $seenCursors.Add($cursor)) {
            throw "Cursor loop detected before page $($pageNumber + 1)."
        }

        $pageNumber++
        $queryString = (
            'search={0}&filter={1}&select={2}&per-page={3}&cursor={4}' -f
            (Encode-QueryValue -Value $query),
            (Encode-QueryValue -Value $filter),
            (Encode-QueryValue -Value ($selectFields -join ',')),
            $perPage,
            (Encode-QueryValue -Value $cursor)
        )
        $requestedUrl = "$apiBase`?$queryString"
        $pageName = 'page-{0:D3}.json' -f $pageNumber
        $pagePath = Resolve-ContainedPath `
            -Root $stagingDir `
            -RelativePath $pageName

        if (Test-Path -LiteralPath $downloadTempPath -PathType Leaf) {
            Remove-Item -LiteralPath $downloadTempPath -Force
        }

        $response = Invoke-WebRequest `
            -Uri $requestedUrl `
            -Method Get `
            -Headers @{ Accept = 'application/json' } `
            -OutFile $downloadTempPath `
            -PassThru `
            -SkipHttpErrorCheck

        $httpStatus = [int]$response.StatusCode
        if ($httpStatus -lt 200 -or $httpStatus -ge 300) {
            throw (
                "OpenAlex returned HTTP $httpStatus for page $pageNumber. " +
                "URL: $requestedUrl"
            )
        }

        $rawJson = Get-Content -LiteralPath $downloadTempPath -Raw
        $payload = $rawJson | ConvertFrom-Json -AsHashtable
        $pageData = Get-ValidatedPageData `
            -Payload $payload `
            -PageNumber $pageNumber
        $pageResults = @($pageData.Results)
        $pageResultCount = $pageResults.Count
        $pageMetaCount = $pageData.MetaCount
        if ($pageNumber -eq 1) {
            $expectedMetaCount = $pageMetaCount
        }
        elseif ($pageMetaCount -ne $expectedMetaCount) {
            throw (
                "meta.count changed from $expectedMetaCount to " +
                "$pageMetaCount on page $pageNumber."
            )
        }

        foreach ($work in $pageResults) {
            if ($work -isnot [Collections.IDictionary]) {
                throw "Page $pageNumber contains a result that is not an object."
            }
            $openAlexId = [string]$work['id']
            if ([string]::IsNullOrWhiteSpace($openAlexId)) {
                throw "Page $pageNumber contains a result without an OpenAlex ID."
            }
            if (-not $seenIds.Add($openAlexId)) {
                $duplicateCount++
            }
        }

        $cumulativeResults += $pageResultCount
        $nextCursor = $pageData.NextCursor
        $nextCursorPresent = $null -ne $nextCursor

        Move-Item -LiteralPath $downloadTempPath -Destination $pagePath
        $pageSha256 = (Get-FileHash -LiteralPath $pagePath -Algorithm SHA256).
            Hash.ToLowerInvariant()

        $manifestRows.Add([pscustomobject][ordered]@{
                page_number = $pageNumber
                requested_url = $requestedUrl
                http_status = $httpStatus
                page_results = $pageResultCount
                cumulative_results = $cumulativeResults
                meta_count = $pageMetaCount
                next_cursor_present = $nextCursorPresent.ToString().ToLowerInvariant()
                filename = $pageName
                sha256 = $pageSha256
            })

        Write-Host ((
            "page={0:D3} http={1} results={2} cumulative={3} " +
            "next_cursor={4} url={5}"
        ) -f
            $pageNumber,
            $httpStatus,
            $pageResultCount,
            $cumulativeResults,
            $nextCursorPresent,
            $requestedUrl
        )

        if ($nextCursorPresent) {
            $cursor = [string]$nextCursor
        }
        else {
            $cursor = $null
        }
    }

    if ($cumulativeResults -ne $expectedMetaCount) {
        throw (
            "Exported result count $cumulativeResults does not match " +
            "first-page meta.count $expectedMetaCount."
        )
    }
    if ($duplicateCount -ne 0) {
        throw "Found $duplicateCount duplicate OpenAlex IDs."
    }

    $manifestRows | Export-Csv `
        -LiteralPath $manifestPath `
        -NoTypeInformation `
        -Encoding utf8

    $checksumLines = [Collections.Generic.List[string]]::new()
    foreach ($row in $manifestRows) {
        $checksumLines.Add("$($row.sha256)  $($row.filename)")
    }
    $manifestSha256 = (
        Get-FileHash -LiteralPath $manifestPath -Algorithm SHA256
    ).Hash.ToLowerInvariant()
    $checksumLines.Add("$manifestSha256  manifest.csv")
    Set-Content `
        -LiteralPath $checksumsPath `
        -Value $checksumLines `
        -Encoding utf8

    Assert-SnapshotIntegrity -SnapshotDir $stagingDir
    Commit-StagedSnapshot `
        -StagingDir $stagingDir `
        -TargetDir $artifactDir

    Write-Host (
        "PASS pages=$pageNumber meta.count=$expectedMetaCount " +
        "actual=$cumulativeResults delta=0 duplicates=$duplicateCount"
    )
}
finally {
    if (Test-Path -LiteralPath $downloadTempPath -PathType Leaf) {
        Remove-Item -LiteralPath $downloadTempPath -Force
    }
    if (Test-Path -LiteralPath $stagingDir -PathType Container) {
        try {
            Remove-Item -LiteralPath $stagingDir -Recurse -Force
        }
        catch {
            Write-Warning "Could not remove staging directory $stagingDir."
        }
    }
}
