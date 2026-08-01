$ErrorActionPreference = 'Stop'
$runRoot = Split-Path -Parent $PSCommandPath
$rawRoot = Join-Path $runRoot 'raw'
New-Item -ItemType Directory -Force -Path $rawRoot | Out-Null
$queries = Import-Csv (Join-Path $runRoot 'query-catalog.csv')

# Each endpoint is a prospective access attempt.  Its response is preserved even
# when it cannot establish a usable internal-search session; then a separately
# labelled site: discovery fallback is captured.  Neither response is screened.
$channels = @(
  [pscustomobject]@{ id='MOH'; domain='moh.gov.vn'; endpoint='https://moh.gov.vn/tim-kiem?query=' },
  [pscustomobject]@{ id='MOH-ASTT'; domain='asttmoh.vn'; endpoint='https://asttmoh.vn/?s=' },
  [pscustomobject]@{ id='MOH-KCB'; domain='kcb.vn'; endpoint='https://kcb.vn/?site=2005611&page=search&keyword=' },
  [pscustomobject]@{ id='MOH-HTTB'; domain='imda.moh.gov.vn'; endpoint='https://imda.moh.gov.vn/?s=' },
  [pscustomobject]@{ id='MOH-NHIC'; domain='ttyqg.vn'; endpoint='https://ttyqg.vn/?s=' },
  [pscustomobject]@{ id='MOH-PC'; domain='vuphapche.moh.gov.vn'; endpoint='https://vuphapche.moh.gov.vn/?s=' },
  [pscustomobject]@{ id='MOH-HSPI'; domain='hspi.org.vn'; endpoint='https://hspi.org.vn/news/find?txtKw=' },
  [pscustomobject]@{ id='UNESCO-RAM'; domain='www.unesco.org/ethics-ai'; endpoint='https://www.unesco.org/ethics-ai/en/search?category=Global%20AI%20Ethics%20and%20Governance%20Observatory&query=' },
  [pscustomobject]@{ id='WHO-VNM'; domain='www.who.int/vietnam'; endpoint='https://www.who.int/vietnam/search?query=' }
)

function Invoke-Capture([string]$url, [string]$base, [string]$label) {
  $hdr = "$base.headers.txt"; $body = "$base.html"; $err = "$base.stderr.txt"
  & curl.exe --insecure --location --max-time 12 --connect-timeout 8 --dump-header $hdr --output $body --write-out '%{http_code}' $url 2> $err | Set-Content -LiteralPath "$base.httpstatus.txt" -NoNewline
  $code = (Get-Content -LiteralPath "$base.httpstatus.txt" -Raw).Trim()
  $bodyBytes = if (Test-Path -LiteralPath $body) { (Get-Item -LiteralPath $body).Length } else { 0 }
  [pscustomobject]@{ status=$code; bytes=$bodyBytes; headers=$hdr; body=$body; stderr=$err; label=$label }
}

$ledger = @()
foreach ($channel in $channels) {
  foreach ($query in $queries) {
    $safeId = $query.query_id.ToLowerInvariant()
    $q = [uri]::EscapeDataString($query.verbatim_query)
    $attemptUrl = "$($channel.endpoint)$q"
    $base = Join-Path $rawRoot "$($channel.id.ToLowerInvariant())-$safeId-internal"
    $started = (Get-Date).ToString('o')
    $attempt = Invoke-Capture $attemptUrl $base 'INTERNAL_SEARCH_ATTEMPT'
    $accepted = ($attempt.status -eq '200' -and $attempt.bytes -gt 500)
    $fallback = $null
    if (-not $accepted) {
      $fallbackUrl = 'https://www.bing.com/search?q=' + [uri]::EscapeDataString("site:$($channel.domain) $($query.verbatim_query)") + '&first=1'
      $fallbackBase = Join-Path $rawRoot "$($channel.id.ToLowerInvariant())-$safeId-site-fallback"
      $fallback = Invoke-Capture $fallbackUrl $fallbackBase 'SITE_FALLBACK_DISCOVERY'
    }
    $allArtifacts = @($attempt.body,$attempt.headers,$attempt.stderr,"$base.httpstatus.txt")
    if ($null -ne $fallback) { $allArtifacts += @($fallback.body,$fallback.headers,$fallback.stderr,"$((Split-Path $fallback.body -Parent))\$((Split-Path $fallback.body -LeafBase)).httpstatus.txt") }
    foreach($artifact in $allArtifacts) { if(Test-Path -LiteralPath $artifact) { Get-FileHash -Algorithm SHA256 -LiteralPath $artifact | ForEach-Object { "$($_.Hash),$($_.Path)" } | Add-Content -LiteralPath (Join-Path $runRoot 'sha256.csv') } }
    $ledger += [pscustomobject]@{
      query_id=$query.query_id; channel_id=$channel.id; domain=$channel.domain; query_family=$query.query_family; query_verbatim=$query.verbatim_query; started_at=$started
      internal_url=$attemptUrl; internal_http_status=$attempt.status; internal_body_bytes=$attempt.bytes; internal_body_file=(Split-Path $attempt.body -Leaf); internal_headers_file=(Split-Path $attempt.headers -Leaf)
      fallback_used=($null -ne $fallback); fallback_http_status=if($null -ne $fallback){$fallback.status}else{''}; fallback_body_bytes=if($null -ne $fallback){$fallback.bytes}else{''}; fallback_body_file=if($null -ne $fallback){Split-Path $fallback.body -Leaf}else{''}
      disposition=if($accepted){'RAW_INTERNAL_RESPONSE_CAPTURED_UNSCREENED'}elseif($null -ne $fallback){'RAW_INTERNAL_FAILURE_AND_SITE_FALLBACK_CAPTURED_UNSCREENED'}else{'RAW_INTERNAL_FAILURE_CAPTURED_UNSCREENED'}
      interpretation='No absence, relevance, eligibility, saturation, or count inference. Pagination and result-level acquisition require separate verification.'
    }
  }
}
$ledger | Export-Csv -LiteralPath (Join-Path $runRoot 'query-provenance.csv') -NoTypeInformation -Encoding utf8
