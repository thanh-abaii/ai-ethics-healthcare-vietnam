Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

# Official PubMed UI retrieval. This script intentionally reads the frozen
# search strategy and does not import any legacy search artifact.
$repo = Split-Path -Parent (Split-Path -Parent (Split-Path -Parent $PSScriptRoot))
$strategyPath = Join-Path $repo 'search-strategy.md'
$strategy = Get-Content -LiteralPath $strategyPath -Raw -Encoding utf8
$match = [regex]::Match(
    $strategy,
    '(?s)### 4\.1\. Truy vấn nguyên văn\s*```text\s*(.*?)\s*```'
)
if (-not $match.Success) { throw 'LOCKED_PUBMED_QUERY_NOT_FOUND' }
$query = $match.Groups[1].Value.Trim()

$queryPath = Join-Path $PSScriptRoot 'query-verbatim.txt'
[System.IO.File]::WriteAllText($queryPath, $query + [Environment]::NewLine, [System.Text.UTF8Encoding]::new($false))

$encoded = [uri]::EscapeDataString($query)
$uiResultsUrl = "https://pubmed.ncbi.nlm.nih.gov/?term=$encoded"
$uiExportUrl = "https://pubmed.ncbi.nlm.nih.gov/?term=$encoded&format=pubmed&size=200"
$htmlPath = Join-Path $PSScriptRoot 'official-ui-results.html'
$htmlHeadersPath = Join-Path $PSScriptRoot 'official-ui-results.headers.txt'
$nbibPath = Join-Path $PSScriptRoot 'official-ui-export.nbib'
$nbibHeadersPath = Join-Path $PSScriptRoot 'official-ui-export.headers.txt'

& curl.exe --fail --location --retry 2 --retry-all-errors --connect-timeout 30 --max-time 180 --user-agent 'Mozilla/5.0 (compatible; PRISMA-ScR-reproducibility/1.0)' --dump-header $htmlHeadersPath --output $htmlPath $uiResultsUrl
if ($LASTEXITCODE -ne 0) { throw "PUBMED_UI_RESULTS_FETCH_FAILED_EXIT_$LASTEXITCODE" }
& curl.exe --fail --location --retry 2 --retry-all-errors --connect-timeout 30 --max-time 180 --user-agent 'Mozilla/5.0 (compatible; PRISMA-ScR-reproducibility/1.0)' --dump-header $nbibHeadersPath --output $nbibPath $uiExportUrl
if ($LASTEXITCODE -ne 0) { throw "PUBMED_UI_EXPORT_FETCH_FAILED_EXIT_$LASTEXITCODE" }

$nbib = Get-Content -LiteralPath $nbibPath -Raw -Encoding utf8
$pmids = [regex]::Matches($nbib, '(?m)^PMID-\s+(\d+)\s*$')
if ($pmids.Count -eq 0) { throw 'PUBMED_UI_EXPORT_NOT_NBIB_OR_EMPTY' }
$duplicates = @($pmids | ForEach-Object { $_.Groups[1].Value } | Group-Object | Where-Object Count -gt 1)
if ($duplicates.Count -gt 0) { throw 'PUBMED_UI_EXPORT_CONTAINS_DUPLICATE_PMIDS' }

$hashes = Get-ChildItem -LiteralPath $PSScriptRoot -File |
    Where-Object { $_.Name -notin @('manifest.json', 'run-pubmed-official.ps1') } |
    ForEach-Object { [pscustomobject]@{ file = $_.Name; sha256 = (Get-FileHash -LiteralPath $_.FullName -Algorithm SHA256).Hash } }

$manifest = [ordered]@{
    run_id = 'official-search-rerun-01-2026-07-31-pubmed'
    status = 'RAW_EXPORT_CAPTURED_NOT_SCREENED'
    source = 'PubMed official web interface'
    query_source = 'search-strategy.md section 4.1; frozen pre-registered search strategy'
    query_file = 'query-verbatim.txt'
    ui_results_url = $uiResultsUrl
    ui_export_url = $uiExportUrl
    retrieved_at_local = (Get-Date).ToString('o')
    raw_export = 'official-ui-export.nbib'
    raw_export_format = 'NBIB / PubMed format'
    raw_record_count_from_nbib = $pmids.Count
    query_translation_status = 'NOT_CAPTURED_FROM_OFFICIAL_UI_IN_THIS_RUN; consult frozen search-strategy.md section 4.2 for pre-specified translation and do not infer a post-hoc translation from NBIB.'
    screening_or_extraction = 'NOT_STARTED'
    files = @($hashes)
}
$manifest | ConvertTo-Json -Depth 4 | Set-Content -LiteralPath (Join-Path $PSScriptRoot 'manifest.json') -Encoding utf8
Write-Output ("RAW_EXPORT_CAPTURED; PMID_COUNT={0}" -f $pmids.Count)
