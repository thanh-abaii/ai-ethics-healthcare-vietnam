import csv
import os

root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
csv_path = os.path.join(root_dir, 'artifacts', 'official-search-run-2026-07-31', 'official-screening-workspace-round-1.csv')

rich_reasons = {
    # Batch 1
    'REC_DIR_0001': 'Trực tiếp nghiên cứu chính sách y tế số và chương trình triển khai tại các bệnh viện Việt Nam.',
    'REC_DIR_0002': 'Đánh giá độ sẵn sàng cho AI trong hệ thống thông tin y tế Việt Nam, liên quan trực tiếp đến thể chế và hạ tầng.',
    'REC_DIR_0003': 'Tinh chỉnh LLM cho giao tiếp y tế ngôn ngữ nguồn lực thấp (tiếng Việt), chạm đến an toàn và văn hóa tiếp cận.',
    'REC_DIR_0004': 'Tổng quan ứng dụng AI và công nghệ y tế số trực tiếp tại Việt Nam công bố trên Tạp chí WHO.',
    'REC_DIR_0005': 'Trực tiếp nghiên cứu giảm thiểu thiên vị (bias) và tăng tính công bằng (fairness) của thuật toán ML cho Việt Nam.',
    'REC_DIR_0006': 'Ứng dụng ML hỗ trợ ra quyết định lâm sàng (CDS) cho bệnh nhân sốt xuất huyết tại bệnh viện Việt Nam.',
    'REC_DIR_0007': 'EX02_NOT_HEALTHCARE (Áp dụng ML dự báo ô nhiễm không khí môi trường TP.HCM, không thuộc bối cảnh y tế lâm sàng).',
    'REC_DIR_0008': 'EX02_NOT_HEALTHCARE (Nghiên cứu đại số đại lượng và LLM chung, không đề cập đến bối cảnh y tế hay quản trị y tế).',
    'REC_DIR_0009': 'EX02_NOT_HEALTHCARE (Bản đồ rủi ro ngập lụt thiên tai, không thuộc bối cảnh y tế bệnh nhân).',
    'REC_DIR_0010': 'Giám sát sinh hiệu tự động tại khoa hồi sức tích cực (ICU) bệnh viện Việt Nam — dữ liệu lâm sàng thực tế.',
    'REC_DIR_0011': 'Trực tiếp nghiên cứu mối đe dọa nhận thức và sự chấp nhận triển khai Generative AI tại các bệnh viện Việt Nam.',
    'REC_DIR_0012': 'Tiên lượng tử vong do nhiễm trùng huyết bằng thiết bị đeo tại Việt Nam (LMIC) — ứng dụng CDS.',
    'REC_DIR_0013': 'Khía cạnh đạo đức (ethical), tính bao hàm và dữ liệu trong y học cổ truyền bằng Generative AI.',
    'REC_DIR_0014': 'Bài báo trọng tâm về Đạo đức AI, quản trị (governance), niềm tin và thể chế tại Việt Nam.',
    'REC_DIR_0016': 'EX02_NOT_HEALTHCARE (Mô hình dự báo bụi PM2.5 môi trường, không thuộc bối cảnh y tế bệnh nhân).',
    'REC_DIR_0017': 'Mô hình AI phân loại cấp cứu ngoại viện có tính giải thích được (Interpretable AI) áp dụng tại Việt Nam.',
    'REC_DIR_0018': 'Thử nghiệm lâm sàng tiến cứu về ML hỗ trợ phân loại mức độ sốt xuất huyết tại Việt Nam.',
    'REC_DIR_0019': 'EX01_NOT_AI (Nghiên cứu kinh tế y tế và chi tiêu nghèo năng lượng, không liên quan đến công nghệ AI/ML).',
    'REC_DIR_0020': 'Giải quyết vấn đề bảo mật dữ liệu y tế (Differential Privacy) trong AI phân loại X-quang ngực.',
    'REC_DIR_0021': 'Đánh giá an toàn và độ chính xác của LLM khi dịch tóm tắt tư vấn y khoa.',
    # Batch 2
    'REC_DIR_0022': 'Trực tiếp nghiên cứu cơ hội và thách thức khi sử dụng AI trong đào tạo y khoa tại Việt Nam.',
    'REC_DIR_0023': 'Đánh giá độ chính xác của AI dịch hướng dẫn xuất viện (bao gồm bản tiếng Việt), liên quan an toàn bệnh nhân.',
    'REC_DIR_0024': 'EX01_NOT_AI (Nghiên cứu chênh lệch giới trong đại dịch COVID-19 chung, không liên quan đến công nghệ hay quản trị AI/ML).',
    'REC_DIR_0025': 'EX02_NOT_HEALTHCARE (Ứng dụng AI trong sinh thái học Ecology, không thuộc bối cảnh y tế hay chăm sóc sức khỏe).',
    'REC_DIR_0026': 'Nhân văn hóa chăm sóc hô hấp bằng AI âm thanh và công bằng sức khỏe toàn cầu.',
    'REC_DIR_0027': 'EX02_NOT_HEALTHCARE (Giám sát sức khỏe kết cấu công trình cầu đường/bê tông, không phải y tế con người).',
    'REC_DIR_0028': 'EX02_NOT_HEALTHCARE (Dự báo chất lượng không khí PM2.5 môi trường, không thuộc bối cảnh y tế lâm sàng).',
    'REC_DIR_0029': 'EX02_NOT_HEALTHCARE (Tài chính xanh và AI - Kinh tế/Tài chính, không thuộc bối cảnh y tế).',
    'REC_DIR_0030': 'EX02_NOT_HEALTHCARE (Mô hình LASSO tiên lượng kiệt quệ tài chính doanh nghiệp niêm yết, không thuộc y tế).',
    'REC_DIR_0031': 'Trực tiếp nghiên cứu thực trạng và tương lai chấp nhận AI trong hệ thống y tế Đông Nam Á (bao gồm Việt Nam).',
    'REC_DIR_0032': 'Sử dụng ML tiên lượng nồng độ ức chế tối thiểu kháng sinh (kháng kháng sinh) — vi sinh lâm sàng và quản trị thuốc.',
    'REC_DIR_0033': 'EX02_NOT_HEALTHCARE (Tiên lượng biến dạng cầu bê tông - Xây dựng/Hạ tầng, không thuộc y tế).',
    'REC_DIR_0034': 'EX02_NOT_HEALTHCARE (Phân tích tiến hóa đa dạng sinh học loài rắn san hô - Sinh học/Động vật học, không thuộc y tế).',
    'REC_DIR_0035': 'EX02_NOT_HEALTHCARE (Chỉ số sức khỏe thảm thực vật - Nông nghiệp/Địa lý, không phải y tế con người).',
    'REC_DIR_0036': 'Suy luận cảm xúc AI ứng dụng trong y tế (Healthcare) — nhóm tác giả Việt Nam.',
    'REC_DIR_0037': 'Phân tích ML dịch tễ học sinh thái bệnh sán lá gan tại Việt Nam.',
    'REC_DIR_0038': 'AI hỗ trợ dịch thuật giao tiếp với bệnh nhân rào cản ngôn ngữ trong chăm sóc y tế.',
    'REC_DIR_0039': 'Vai trò điều tiết của dịch vụ AI trong ngành y tế và chất lượng dịch vụ bệnh viện tại Việt Nam.',
    'REC_DIR_0040': 'EX02_NOT_HEALTHCARE (Tiên lượng độ võng của cầu đường - Xây dựng/Hạ tầng, không thuộc y tế).',
    'REC_DIR_0041': 'Xây dựng và thẩm định hệ thống hỗ trợ quyết định lâm sàng (CDSS) dựa trên ML cho bệnh nhân tâm thần phân liệt tại Việt Nam.',
    # Batch 3
    'REC_DIR_0043': 'Trực tiếp nghiên cứu thách thức pháp lý và quyền người bệnh trong kỷ nguyên AI đối với sinh viên y khoa Việt Nam.',
    'REC_DIR_0045': 'Khung Agentic AI điều phối luồng công việc lâm sàng thích ứng tại các cơ sở y tế Việt Nam.',
    'REC_DIR_0046': 'Tích hợp AI trong đào tạo y khoa tại Việt Nam dưới các chiều kích con người - tổ chức - công nghệ (HOT).',
    'REC_DIR_0047': 'Khảo sát góc nhìn của sinh viên y tế Việt Nam về AI và robot trong chăm sóc bệnh nhân và nhu cầu cải cách chương trình.',
    'REC_DIR_0048': 'EX01_NOT_AI (Bài báo tổng quan chung về Mục tiêu phát triển bền vững LHQ, không có nội dung AI hay y tế VN).',
    'REC_DIR_0049': 'Trực tiếp nghiên cứu ứng dụng AI trong ngành y tế và các thách thức pháp lý tại Việt Nam.',
    'REC_DIR_0050': 'Ứng dụng LLM đánh giá năng lực bác sĩ qua tình huống đối thoại lâm sàng thử nghiệm tại Việt Nam.',
    'REC_DIR_0051': 'Bản thảo rà soát phạm vi chính sách và chương trình y tế số cho bệnh viện Việt Nam.',
    'REC_DIR_0052': 'Trực tiếp nghiên cứu AI có trách nhiệm (Responsible AI) và điểm tựa quyết định trong ứng phó dịch bệnh tại Việt Nam.',
    'REC_DIR_0053': 'Thử nghiệm lâm sàng tiến cứu ứng dụng thiết bị đeo và mạng Nơ-ron cho bệnh nhân sốt xuất huyết tại Việt Nam.',
    'REC_DIR_0054': 'EX02_NOT_HEALTHCARE (Rà soát nghiên cứu hạn hán dựa trên quan sát Trái Đất - Môi trường/Địa lý).',
    'REC_DIR_0055': 'Kết hợp Học sâu và LLM tự động phân loại thoái hóa khớp gối từ dữ liệu Nghiên cứu Loãng xương Việt Nam.',
    'REC_DIR_0056': 'EX02_NOT_HEALTHCARE (Định lượng chỉ số diện tích lá rừng ngập mặn từ ảnh vệ tinh - Lâm nghiệp/Môi trường).',
    'REC_DIR_0057': 'Bản thảo so sánh LLM và công cụ dịch thuật truyền thống trong dịch tóm tắt khám bệnh.',
    'REC_DIR_0058': 'Phân loại mức độ nghiêm trọng bệnh uốn ván bằng cảm biến đeo tại khoa hồi sức tích cực bệnh viện Việt Nam.',
    'REC_DIR_0059': 'Khung quản trị dựa trên dữ liệu cho chất lượng y tế đồng tạo lập tại các bệnh viện công Việt Nam.',
    'REC_DIR_0060': 'Trực tiếp xây dựng bộ benchmark AI hỏi đáp đa chặng về quy định và pháp luật y tế Việt Nam.',
    'REC_DIR_0062': 'EX03_NOT_VIETNAM_HEALTH_CONTEXT (Bảo vệ thành quả loại trừ sốt rét tại Trung Quốc, không có bối cảnh Việt Nam).',
    'REC_DIR_0063': 'Đánh giá thực chứng việc chấp nhận công nghệ y tế số tại 5 bệnh viện Việt Nam.',
    'REC_DIR_0064': 'EX02_NOT_HEALTHCARE (Áp dụng ML đánh giá sức khỏe kinh tế tư nhân địa phương - Kinh tế/Doanh nghiệp).',
    # Batch 4
    'REC_DIR_0066': 'Thẩm định công cụ giám sát trực tuyến và tiên lượng dựa trên ML cho bệnh nhân lọc máu chạy thận nhân tạo tại Việt Nam.',
    'REC_DIR_0067': 'EX02_NOT_HEALTHCARE (Dự báo phát thải khí Mê-tan từ ruộng lúa - Nông nghiệp/Môi trường, không thuộc y tế con người).',
    'REC_DIR_0068': 'Kỷ yếu Hội nghị Sinh học Đạo đức Quốc tế (International Association of Bioethics) — thảo luận đạo đức sinh học và AI y tế.',
    'REC_DIR_0069': 'EX02_NOT_HEALTHCARE (Thúc đẩy nông nghiệp bền vững tại Việt Nam qua công nghệ sinh học và AI - Nông nghiệp).',
    'REC_DIR_0070': 'Tổng quan ứng dụng AI trong nghiên cứu y sinh và y học chính xác (Precision Medicine).',
    'REC_DIR_0072': 'EX02_NOT_HEALTHCARE (Nhận diện sự hiện diện của ong chúa bằng âm thanh AI - Nông nghiệp/Động vật học).',
    'REC_DIR_0073': 'Trực tiếp so sánh các phương pháp ML phân loại bệnh Alzheimer cho bệnh nhân Việt Nam.',
    'REC_DIR_0074': 'EX02_NOT_HEALTHCARE (Đánh giá rủi ro hạn hán tại Quảng Trị bằng viễn thám và ML - Môi trường/Địa lý).',
    'REC_DIR_0075': 'Mô hình đánh giá rủi ro cho ngành bảo hiểm y tế — liên quan thể chế chi trả và quản trị dữ liệu y tế.',
    'REC_DIR_0076': 'Tiên lượng rủi ro tim mạch bằng AI kết hợp cảm biến sinh học đeo — ứng dụng CDS từ tác giả Việt Nam.',
    'REC_DIR_0077': 'EX02_NOT_HEALTHCARE (Xung đột đạo đức AI và sức khỏe tâm thần của kế toán viên FinTech tài chính, không thuộc y tế bệnh nhân).',
    'REC_DIR_0078': 'Trực tiếp xây dựng khung nghiên cứu thiên vị thuật toán (Algorithmic Bias) như một yếu tố xã hội quyết định sức khỏe tại LMICs.',
    'REC_DIR_0079': 'EX02_NOT_HEALTHCARE (Dự báo độ lún công trình xây dựng tại Việt Nam bằng ML - Xây dựng/Hạ tầng).',
    'REC_DIR_0080': 'Trực tiếp xây dựng bộ dữ liệu hỏi đáp AI tiếng Việt trong lĩnh vực sức khỏe tâm thần (Mental Health).',
    'REC_DIR_0081': 'Tổng quan ứng dụng AI Agent trong vận hành dược bệnh viện tại Việt Nam.',
    'REC_DIR_0082': 'EX02_NOT_HEALTHCARE (Cơ hội việc làm do AI tạo ra - Lao động/Kinh tế chung, không thuộc y tế).',
    'REC_DIR_0083': 'EX03_NOT_VIETNAM_HEALTH_CONTEXT (Mô hình nhận dạng hoạt động con người bằng Học sâu chung, không có bối cảnh y tế hay thể chế Việt Nam).',
    'REC_DIR_0084': 'EX02_NOT_HEALTHCARE (Viễn thám ước tính năng suất và rủi ro khí hậu cho cây cà phê ở Tây Nguyên - Nông nghiệp).',
    'REC_DIR_0085': 'Tổng quan nghiên cứu phát triển dữ liệu lớn Dữ liệu gen (Genomics & Big Data) tại Việt Nam — liên quan đạo đức dữ liệu gen y tế.',
    'REC_DIR_0086': 'Khảo sát Kiến thức - Thái độ - Thực hành (KAP) về AI của sinh viên ngành y tế và độ sẵn sàng cho AI.'
}

rows = []
with open(csv_path, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    for r in reader:
        if r['record_id'] in rich_reasons:
            reason = rich_reasons[r['record_id']]
            r['screening_reason'] = reason
            r['human_approval'] = 'APPROVED_BY_DAO_TRUNG_THANH'
            if reason.startswith('EX0') or 'EX0' in reason:
                r['screening_recommendation'] = 'EXCLUDE_ROUND_1'
                r['screening_status_round_1'] = 'EXCLUDED_ROUND_1'
            else:
                r['screening_recommendation'] = 'INCLUDE_ROUND_1'
                r['screening_status_round_1'] = 'PASSED_TO_ROUND_2'
        rows.append(r)

with open(csv_path, 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print(f"Successfully updated CSV workspace with rich Vietnamese reasons and APPROVED_BY_DAO_TRUNG_THANH for {len(rich_reasons)} records.")
