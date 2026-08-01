$ErrorActionPreference = 'Stop'

# Official-portal run for the legal/council query IDs that MST's public search
# endpoint accepts. It writes raw HTML, SHA-256 and run metadata; it does not
# make relevance, eligibility, or legal-effect decisions.
$here = Split-Path -Parent $PSCommandPath
$queries = @(
    # Subqueries preserve the locked Boolean groups where this portal accepts
    # keywords only. They are logged separately and are not merged as proof of
    # saturation for their parent query ID.
    [pscustomobject]@{ Id = 'DQ-LAW-02-A'; Query = 'Luật Trí tuệ nhân tạo' },
    [pscustomobject]@{ Id = 'DQ-LAW-02-B'; Query = 'y tế' },
    [pscustomobject]@{ Id = 'DQ-LAW-02-C'; Query = 'người bệnh' },
    [pscustomobject]@{ Id = 'DQ-LAW-02-D'; Query = 'bệnh viện' },
    [pscustomobject]@{ Id = 'DQ-LAW-02'; Query = 'Luật Trí tuệ nhân tạo y tế người bệnh bệnh viện' },
    [pscustomobject]@{ Id = 'DQ-FRAME-02-A'; Query = 'Khung đạo đức trí tuệ nhân tạo quốc gia' },
    [pscustomobject]@{ Id = 'DQ-FRAME-02-B'; Query = 'y tế' },
    [pscustomobject]@{ Id = 'DQ-FRAME-02-C'; Query = 'bệnh viện' },
    [pscustomobject]@{ Id = 'DQ-FRAME-02-D'; Query = 'khám chữa bệnh' },
    [pscustomobject]@{ Id = 'DQ-FRAME-02'; Query = 'Khung đạo đức trí tuệ nhân tạo quốc gia y tế bệnh viện khám chữa bệnh' },
    [pscustomobject]@{ Id = 'DQ-REL-01-A'; Query = '134/2025/QH15' },
    [pscustomobject]@{ Id = 'DQ-REL-01-B'; Query = '142/2026/NĐ-CP' },
    [pscustomobject]@{ Id = 'DQ-REL-01-C'; Query = '05/2026/TT-BKHCN' },
    [pscustomobject]@{ Id = 'DQ-REL-01-D'; Query = 'sửa đổi thay thế hướng dẫn triển khai' },
    [pscustomobject]@{ Id = 'DQ-REL-01'; Query = '134/2025/QH15 142/2026/NĐ-CP 05/2026/TT-BKHCN sửa đổi thay thế hướng dẫn triển khai' },
    [pscustomobject]@{ Id = 'DQ-COUNCIL-NAME-01'; Query = 'Hội đồng đạo đức AI quốc gia' },
    [pscustomobject]@{ Id = 'DQ-COUNCIL-NAME-02'; Query = 'Hội đồng đạo đức trí tuệ nhân tạo quốc gia' },
    [pscustomobject]@{ Id = 'DQ-COUNCIL-NAME-03'; Query = 'Ủy ban đạo đức AI quốc gia' },
    [pscustomobject]@{ Id = 'DQ-COUNCIL-NAME-04'; Query = 'National AI Ethics Council Vietnam' },
    [pscustomobject]@{ Id = 'DQ-COUNCIL-NAME-05'; Query = 'National Council on AI Ethics Vietnam' },
    [pscustomobject]@{ Id = 'DQ-COUNCIL-NAME-06'; Query = 'AI ethics committee Vietnam' },
    [pscustomobject]@{ Id = 'DQ-COUNCIL-EST-01-A'; Query = 'hội đồng đạo đức AI' },
    [pscustomobject]@{ Id = 'DQ-COUNCIL-EST-01-B'; Query = 'quyết định thành lập' },
    [pscustomobject]@{ Id = 'DQ-COUNCIL-EST-01-C'; Query = 'quy chế' },
    [pscustomobject]@{ Id = 'DQ-COUNCIL-EST-01-D'; Query = 'chức năng nhiệm vụ' },
    [pscustomobject]@{ Id = 'DQ-COUNCIL-EST-01-E'; Query = 'thành viên' },
    [pscustomobject]@{ Id = 'DQ-COUNCIL-EST-01'; Query = 'hội đồng đạo đức AI quyết định thành lập quy chế chức năng nhiệm vụ thành viên' },
    [pscustomobject]@{ Id = 'DQ-COUNCIL-ACT-01-A'; Query = 'hội đồng đạo đức AI' },
    [pscustomobject]@{ Id = 'DQ-COUNCIL-ACT-01-B'; Query = 'phiên họp' },
    [pscustomobject]@{ Id = 'DQ-COUNCIL-ACT-01-C'; Query = 'biên bản' },
    [pscustomobject]@{ Id = 'DQ-COUNCIL-ACT-01-D'; Query = 'báo cáo hoạt động' },
    [pscustomobject]@{ Id = 'DQ-COUNCIL-ACT-01'; Query = 'hội đồng đạo đức AI phiên họp biên bản báo cáo hoạt động' },
    [pscustomobject]@{ Id = 'DQ-COUNCIL-ACT-02'; Query = 'National AI Ethics Council decision regulation mandate members meeting minutes activity report' }
)

$rows = foreach ($item in $queries) {
    $url = 'https://mst.gov.vn/tim-kiem.htm?keywords=' + [uri]::EscapeDataString($item.Query)
    $slug = $item.Id.ToLowerInvariant()
    $rawName = "mst-$slug-2026-07-31.html"
    $rawPath = Join-Path $here $rawName
    $now = [DateTime]::UtcNow.ToString('o')
    try {
        $response = Invoke-WebRequest -Uri $url -TimeoutSec 60 -MaximumRedirection 5
        [System.IO.File]::WriteAllText($rawPath, $response.Content, [System.Text.UTF8Encoding]::new($false))
        $countMatch = [regex]::Match($response.Content, 'Có\s*<span class="bold">\s*(?<count>\d+)\s*</span>\s*tin tức, video', [System.Text.RegularExpressions.RegexOptions]::IgnoreCase)
        $reportedCount = if ($countMatch.Success) { [int]$countMatch.Groups['count'].Value } else { $null }
        [pscustomobject]@{
            query_id = $item.Id; locked_query = $item.Query; portal = 'mst.gov.vn'; run_method = 'internal GET search endpoint';
            run_datetime_utc = $now; requested_url = $url; http_status = [int]$response.StatusCode; raw_file = $rawName;
            bytes = (Get-Item -LiteralPath $rawPath).Length; sha256 = (Get-FileHash -Algorithm SHA256 -LiteralPath $rawPath).Hash.ToLowerInvariant();
            reported_result_count = $reportedCount; run_status = 'RAW_RESULT_PAGE_CAPTURED_NOT_SCREENED';
            stopping_rule = 'FIRST_INTERNAL_RESULTS_PAGE_ONLY; NOT_COMPLETE: portal pagination/result-total not reliably machine-readable in this run.'
        }
    } catch {
        [pscustomobject]@{
            query_id = $item.Id; locked_query = $item.Query; portal = 'mst.gov.vn'; run_method = 'internal GET search endpoint';
            run_datetime_utc = $now; requested_url = $url; http_status = 'ERROR'; raw_file = ''; bytes = 0; sha256 = '';
            discovered_unique_article_links = 0; run_status = 'FAIL_CLOSED'; stopping_rule = ('REQUEST_FAILED: ' + $_.Exception.Message)
        }
    }
}

$rows | Export-Csv -LiteralPath (Join-Path $here 'mst-query-run-2026-07-31.csv') -NoTypeInformation -Encoding utf8
