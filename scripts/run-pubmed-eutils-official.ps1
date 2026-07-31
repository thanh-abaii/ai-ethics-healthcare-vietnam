[CmdletBinding()]
param(
    [string]$OutputRoot,
    [int]$BatchSize = 200
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

# Post-registration execution utility. It never reads a legacy search result and
# it never writes to protocol.md or the frozen OSF snapshot.
$repo = Split-Path -Parent $PSScriptRoot
$frozenStrategy = Join-Path $repo 'artifacts\protocol-registration-lock-2026-07-31\files\search-strategy.md'
if (-not (Test-Path -LiteralPath $frozenStrategy)) { throw 'FROZEN_SEARCH_STRATEGY_NOT_FOUND' }

$strategy = Get-Content -LiteralPath $frozenStrategy -Raw -Encoding utf8
$match = [regex]::Match($strategy, '(?s)### 4\.1\. Truy vấn nguyên văn\s*```text\s*(.*?)\s*```')
if (-not $match.Success) { throw 'LOCKED_PUBMED_QUERY_NOT_FOUND' }
$query = $match.Groups[1].Value.Trim()

if ([string]::IsNullOrWhiteSpace($OutputRoot)) {
    $OutputRoot = Join-Path $repo 'artifacts\official-search-rerun-01-2026-07-31\pubmed'
}
$stamp = (Get-Date).ToString('yyyyMMddTHHmmsszzz').Replace(':','')
$runDir = Join-Path $OutputRoot ("eutils-run-$stamp")
New-Item -ItemType Directory -Force -Path $runDir | Out-Null

function Get-Hash([string]$Path) {
    (Get-FileHash -LiteralPath $Path -Algorithm SHA256).Hash
}

function Invoke-EutilsGet([string]$Name, [string]$ArtifactPrefix, [hashtable]$Parameters) {
    $queryString = ($Parameters.GetEnumerator() | ForEach-Object {
        ('{0}={1}' -f [uri]::EscapeDataString($_.Key), [uri]::EscapeDataString([string]$_.Value))
    }) -join '&'
    $base = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/$Name.fcgi"
    $url = "$base`?$queryString"
    # The initial extension remains neutral. A failed request may return an HTML
    # diagnostic despite a requested JSON/XML format; renaming it would mislead an auditor.
    $body = Join-Path $runDir "$ArtifactPrefix-response.raw"
    $headers = Join-Path $runDir "$ArtifactPrefix-response.headers.txt"
    & curl.exe --fail-with-body --location --retry 2 --retry-all-errors --connect-timeout 30 --max-time 180 `
        --user-agent 'AI-ethics-healthcare-Vietnam-scoping-review/1.0' `
        --dump-header $headers --output $body $url
    $exit = $LASTEXITCODE
    [pscustomobject]@{ name=$Name; url=$url; body=$body; headers=$headers; exit_code=$exit }
}

$queryFile = Join-Path $runDir 'pubmed-query-verbatim.txt'
[System.IO.File]::WriteAllText($queryFile, $query + [Environment]::NewLine, [System.Text.UTF8Encoding]::new($false))
$manifest = [ordered]@{
    run_id = "official-search-rerun-01-2026-07-31-pubmed-eutils-$stamp"
    status = 'STARTED'
    source = 'NCBI E-utilities REST API'
    query_source = 'frozen OSF search-strategy.md section 4.1'
    query_file = 'pubmed-query-verbatim.txt'
    query_sha256 = Get-Hash $queryFile
    started_at_local = (Get-Date).ToString('o')
    steps = @()
    screening_or_extraction = 'NOT_STARTED'
}

try {
    # Step 1: eSearch preserves both the raw JSON and the history server handles.
    $search = Invoke-EutilsGet 'esearch' 'esearch' @{
        db='pubmed'; term=$query; usehistory='y'; retmax='100000'; retmode='json'; tool='ai_ethics_healthcare_vietnam_review'
    }
    if ($search.exit_code -ne 0) { throw "ESEARCH_HTTP_OR_TRANSPORT_FAILURE_EXIT_$($search.exit_code)" }
    $searchRaw = Get-Content -LiteralPath $search.body -Raw -Encoding utf8
    if ($searchRaw.TrimStart().StartsWith('<')) { throw 'ESEARCH_RETURNED_HTML_DIAGNOSTIC_NOT_JSON' }
    $searchJson = $searchRaw | ConvertFrom-Json
    Copy-Item -LiteralPath $search.body -Destination (Join-Path $runDir 'esearch-response.json') -Force
    $result = $searchJson.esearchresult
    if ($null -eq $result -or [string]::IsNullOrWhiteSpace($result.webenv) -or [string]::IsNullOrWhiteSpace($result.querykey)) {
        throw 'ESEARCH_MISSING_WEBENV_OR_QUERYKEY'
    }
    $pmids = @($result.idlist)
    $count = [int]$result.count
    if ($count -ne $pmids.Count) { throw "ESEARCH_PMID_COUNT_MISMATCH_count_$count`_idlist_$($pmids.Count)" }
    $pmidFile = Join-Path $runDir 'esearch-pmid-list.txt'
    [System.IO.File]::WriteAllLines($pmidFile, [string[]]$pmids, [System.Text.UTF8Encoding]::new($false))
    $manifest.steps += [ordered]@{step='esearch'; raw_response=(Split-Path $search.body -Leaf); parsed_json='esearch-response.json'; headers=(Split-Path $search.headers -Leaf); count=$count; webenv=$result.webenv; query_key=$result.querykey; sha256=Get-Hash $search.body}

    # Step 2: eSummary JSON and eFetch XML are retained in bounded history-server batches.
    for ($start = 0; $start -lt $count; $start += $BatchSize) {
        $size = [Math]::Min($BatchSize, $count - $start)
        Start-Sleep -Milliseconds 400
        $summary = Invoke-EutilsGet 'esummary' ("esummary-batch-{0:D6}" -f $start) @{
            db='pubmed'; WebEnv=$result.webenv; query_key=$result.querykey; retstart=$start; retmax=$size; retmode='json'; tool='ai_ethics_healthcare_vietnam_review'
        }
        if ($summary.exit_code -ne 0) { throw "ESUMMARY_HTTP_OR_TRANSPORT_FAILURE_START_$start`_EXIT_$($summary.exit_code)" }
        Start-Sleep -Milliseconds 400
        $fetch = Invoke-EutilsGet 'efetch' ("efetch-batch-{0:D6}" -f $start) @{
            db='pubmed'; WebEnv=$result.webenv; query_key=$result.querykey; retstart=$start; retmax=$size; retmode='xml'; tool='ai_ethics_healthcare_vietnam_review'
        }
        if ($fetch.exit_code -ne 0) { throw "EFETCH_HTTP_OR_TRANSPORT_FAILURE_START_$start`_EXIT_$($fetch.exit_code)" }
        $manifest.steps += [ordered]@{step='batch'; retstart=$start; retmax=$size; esummary_raw=(Split-Path $summary.body -Leaf); esummary_sha256=Get-Hash $summary.body; efetch_raw=(Split-Path $fetch.body -Leaf); efetch_sha256=Get-Hash $fetch.body}
    }
    $manifest.status = 'RAW_EXPORT_CAPTURED_NOT_SCREENED'
    $manifest.raw_record_count = $count
} catch {
    $manifest.status = 'FAIL_CLOSED_RAW_EXPORT_UNAVAILABLE'
    $manifest.failure = $_.Exception.Message
    $manifest.raw_record_count = $null
} finally {
    $manifest.completed_at_local = (Get-Date).ToString('o')
    $manifest.files = @(Get-ChildItem -LiteralPath $runDir -File | ForEach-Object {
        [ordered]@{file=$_.Name; bytes=$_.Length; sha256=Get-Hash $_.FullName}
    })
    $manifest | ConvertTo-Json -Depth 8 | Set-Content -LiteralPath (Join-Path $runDir 'manifest.json') -Encoding utf8
}

if ($manifest.status -ne 'RAW_EXPORT_CAPTURED_NOT_SCREENED') {
    Write-Error ("FAIL_CLOSED: {0}; evidence: {1}" -f $manifest.failure, $runDir)
    exit 2
}
Write-Output ("RAW_EXPORT_CAPTURED_NOT_SCREENED; PMID_COUNT={0}; evidence: {1}" -f $manifest.raw_record_count, $runDir)
