param(
    [Parameter(Mandatory = $true)][string]$ItemId,
    [Parameter(Mandatory = $true)][string]$RunDirectory,
    [switch]$ForceIPv4
)

$ErrorActionPreference = 'Stop'
$url = "https://vbpl.vn/TW/Pages/vbpq-van-ban-goc.aspx?ItemID=$ItemId"
$run = [System.IO.Path]::GetFullPath($RunDirectory)
New-Item -ItemType Directory -Force -Path $run | Out-Null
$body = Join-Path $run 'response-body.html'
$headers = Join-Path $run 'response-headers.txt'
$stderr = Join-Path $run 'transport-stderr.txt'
$request = Join-Path $run 'request.json'

@{
    item_id = $ItemId
    requested_url = $url
    method = 'GET'
    retrieval_utc = [DateTime]::UtcNow.ToString('o')
    user_agent = 'AI-ethics-healthcare-Vietnam-protocol-audit/1.0 (+https://osf.io/62b8w)'
    force_ipv4 = [bool]$ForceIPv4
    scope = 'Raw official-source retrieval only; no screening, coding, deduplication, citation chasing or PRISMA event.'
} | ConvertTo-Json | Set-Content -LiteralPath $request -Encoding utf8

$curlArgs = @('--fail', '--location', '--http1.1', '--max-time', '30', '--connect-timeout', '10', '--tlsv1.2')
if ($ForceIPv4) { $curlArgs += '--ipv4' }
$curlArgs += @(
    '--header', 'User-Agent: AI-ethics-healthcare-Vietnam-protocol-audit/1.0 (+https://osf.io/62b8w)',
    '--dump-header', $headers, '--output', $body, '--stderr', $stderr, $url
)
& curl.exe @curlArgs
$curlExit = $LASTEXITCODE

if (-not (Test-Path -LiteralPath $body)) { [System.IO.File]::WriteAllBytes($body, [byte[]]@()) }
if (-not (Test-Path -LiteralPath $headers)) { [System.IO.File]::WriteAllBytes($headers, [byte[]]@()) }
if (-not (Test-Path -LiteralPath $stderr)) { [System.IO.File]::WriteAllBytes($stderr, [byte[]]@()) }

$files = @('request.json', 'response-body.html', 'response-headers.txt', 'transport-stderr.txt') | ForEach-Object {
    $path = Join-Path $run $_
    $item = Get-Item -LiteralPath $path
    $hash = Get-FileHash -LiteralPath $path -Algorithm SHA256
    [pscustomobject]@{ file = $_; bytes = $item.Length; sha256 = $hash.Hash.ToLowerInvariant() }
}
$files | Export-Csv -LiteralPath (Join-Path $run 'checksums.csv') -NoTypeInformation -Encoding utf8
$status = if ($curlExit -eq 0 -and (Get-Item -LiteralPath $body).Length -gt 0) { 'RAW_OFFICIAL_RESPONSE_CAPTURED_NOT_SCREENED' } else { 'FAIL_CLOSED_RETRIEVAL_FAILED' }
@{
    status = $status
    curl_exit_code = $curlExit
    item_id = $ItemId
    requested_url = $url
    artifacts = $files
} | ConvertTo-Json -Depth 4 | Set-Content -LiteralPath (Join-Path $run 'capture-manifest.json') -Encoding utf8
Write-Output $status
