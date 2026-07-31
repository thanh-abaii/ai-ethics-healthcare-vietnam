Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
$files = Get-ChildItem -LiteralPath $PSScriptRoot -File |
  Where-Object { $_.Name -notin @('manifest.json', 'record-fail-closed.ps1') } |
  ForEach-Object { [pscustomobject]@{ file = $_.Name; bytes = $_.Length; sha256 = (Get-FileHash -LiteralPath $_.FullName -Algorithm SHA256).Hash } }
$manifest = [ordered]@{
  run_id = 'official-search-rerun-01-2026-07-31-pubmed'
  status = 'FAIL_CLOSED_RAW_EXPORT_UNAVAILABLE'
  source = 'PubMed official web interface'
  query_file = 'query-verbatim.txt'
  attempt_timestamp_local = (Get-Date).ToString('o')
  failure = 'Automated PubMed UI endpoints returned a non-NBIB access-control response; Chrome direct navigation was blocked by client policy. No eligible raw export was obtained.'
  raw_record_count = $null
  screening_or_extraction = 'NOT_STARTED'
  action_required = 'Do not create a registry or PRISMA count from this attempt. Reattempt the official UI export in an accessible browser environment; retain this manifest and response files as failed-attempt provenance.'
  files = @($files)
}
$manifest | ConvertTo-Json -Depth 4 | Set-Content -LiteralPath (Join-Path $PSScriptRoot 'manifest.json') -Encoding utf8
