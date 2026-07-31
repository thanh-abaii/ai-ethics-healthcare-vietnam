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
    'REC_DIR_0086': 'Khảo sát Kiến thức - Thái độ - Thực hành (KAP) về AI của sinh viên ngành y tế và độ sẵn sàng cho AI.',
    # Batch 5
    'REC_DIR_0088': 'Trực tiếp nghiên cứu khung năng lực và chuẩn mực đạo đức điều dưỡng tại Việt Nam (Chấp thuận bởi Đào Trung Thành: Khung năng lực chứa thành tố đạo đức hành nghề).',
    'REC_DIR_0089': 'Đánh giá công cụ dịch thuật AI cho hướng dẫn xuất viện khoa cấp cứu — an toàn bệnh nhân và giao tiếp y tế.',
    'REC_DIR_0090': 'Tổng quan ứng dụng AI trong Chẩn đoán trong ống nghiệm (IVD) — thiết bị y tế và hỗ trợ quyết định lâm sàng.',
    'REC_DIR_0091': 'Nghiên cứu bối cảnh về hạ tầng thu thập và quản trị dữ liệu bệnh nhân ung thư tại Châu Á/Việt Nam (Chấp thuận bởi Đào Trung Thành: Quản trị dữ liệu bệnh nhân là nền tảng cho AI).',
    'REC_DIR_0092': 'Trực tiếp xây dựng bộ benchmark ML tiếng Việt (Neurai-VN) cho phân loại kiểu hình số sức khỏe tâm thần tại Việt Nam.',
    'REC_DIR_0093': 'Phát triển và đánh giá trợ lý giảng dạy AI Socratic cho đào tạo Y học cổ truyền Việt Nam.',
    'REC_DIR_0094': 'Trực tiếp khảo sát thực trạng sử dụng ChatGPT và các yếu tố ảnh hưởng đối với sinh viên Đại học Y Hà Nội.',
    'REC_DIR_0095': 'EX02_NOT_HEALTHCARE (Ứng dụng AI trong ngành xây dựng - Xây dựng/Hạ tầng, không thuộc y tế).',
    'REC_DIR_0096': 'Trực tiếp khảo sát KAP về AI trong học tập và nghiên cứu của sinh viên y khoa trên toàn quốc tại Việt Nam.',
    'REC_DIR_0097': 'Khoa học dữ liệu và bình đẳng dữ liệu (Data Equity) trong ứng phó tình huống y tế khẩn cấp.',
    'REC_DIR_0098': 'Chẩn đoán COVID-19 thời gian thực bằng kỹ thuật Học máy (ML) — nhóm nghiên cứu Việt Nam.',
    'REC_DIR_0099': 'EX01_NOT_AI (Diễn đàn hô hấp nhi khoa toàn cầu về COVID-19, không có nội dung công nghệ AI/ML).',
    'REC_DIR_0100': 'EX02_NOT_HEALTHCARE (Bài tòa soạn Tạp chí Kỹ thuật, Thiết kế và Công nghệ - Xây dựng/Kỹ thuật).',
    'REC_DIR_0101': 'EX02_NOT_HEALTHCARE (Nghiên cứu các phương pháp truy xuất thông tin tiếng Việt đa miền chung, không tập trung y tế).',
    'REC_DIR_0102': 'EX02_NOT_HEALTHCARE (Dùng ChatGPT hỗ trợ học tiếng Anh - Ngôn ngữ học/Giáo dục đại cương, không thuộc y tế).',
    'REC_DIR_0103': 'Xây dựng bộ dữ liệu sóng não EEG (UET175) cho nhiệm vụ tưởng tượng vận động ở bệnh nhân đột quỵ Việt Nam.',
    'REC_DIR_0104': 'EX01_NOT_AI (Xuyên quốc gia hóa giáo dục đại học chung, không có nội dung AI/ML hay y tế).',
    'REC_DIR_0105': 'Trực tiếp xây dựng công cụ AI tiên lượng cá thể hóa triệu chứng bệnh lý tâm thần tại Việt Nam.',
    'REC_DIR_0107': 'EX02_NOT_HEALTHCARE (Dự báo bụi PM2.5 trong mỏ đồng mỏ hở - Khai thác mỏ/Môi trường, không thuộc y tế).',
    'REC_DIR_0108': 'EX01_NOT_AI (Bằng chứng cho y học dựa trên bằng chứng EBM chung, không có ứng dụng hay quản trị AI/ML).',
    # Batch 6
    'REC_DIR_0109': 'Sử dụng VLM và ML hiểu tài liệu yêu cầu bồi thường (Bảo hiểm y tế/Tài chính y tế) — tác giả Việt Nam.',
    'REC_DIR_0111': 'EX02_NOT_HEALTHCARE (Mô hình Học liên tục ước tính bụi PM2.5 môi trường tại Việt Nam, không thuộc y tế lâm sàng).',
    'REC_DIR_0112': 'EX01_NOT_AI (Công cụ nhắm mục tiêu giảm nghèo cho đồng bào dân tộc thiểu số Việt Nam - An sinh xã hội chung).',
    'REC_DIR_0113': 'EX03_NOT_VIETNAM_HEALTH_CONTEXT (Thư quyết định về mô hình ML ước tính tiêu thụ muối 54 quốc gia, không có bối cảnh VN).',
    'REC_DIR_0114': 'EX03_NOT_VIETNAM_HEALTH_CONTEXT (Phản hồi tác giả về mô hình ML ước tính tiêu thụ muối 54 quốc gia).',
    'REC_DIR_0115': 'Kiểm định niềm tin và chứng nhận tin cậy (Trust Certification) cho Enterprise AI Agents trước khi triển khai.',
    'REC_DIR_0117': 'Thiết kế đánh giá và dịch chuyển lâm sàng cho AI y sinh đáng tin cậy (Trustworthy Biomedical AI).',
    'REC_DIR_0119': 'EX02_NOT_HEALTHCARE (Ngoại giao số và chính trị quốc tế đối với Việt Nam - Chính trị/Ngoại giao, không thuộc y tế).',
    'REC_DIR_0122': 'Nhận thức và sự sẵn lòng của phụ huynh Việt Nam khi dùng ứng dụng sức khỏe tâm thần dựa trên Internet cho trẻ em.',
    'REC_DIR_0123': 'EX01_NOT_AI (Mở đầu đối thoại về tự do ngôn luận - Tạp chí Daedalus, không có nội dung AI hay y tế VN).',
    'REC_DIR_0124': 'Chương trình quản lý triệu chứng và bài tập kỹ thuật số (i-CanManage) cho phụ nữ Việt Nam sau điều trị ung thư.',
    'REC_DIR_0125': 'EX02_NOT_HEALTHCARE (Ước tính sinh khối trên mặt đất của rừng ở Đắk Lắk - Lâm nghiệp/Môi trường).',
    'REC_DIR_0126': 'EX02_NOT_HEALTHCARE (Chuyển đổi số trong phát triển thể dục thể thao trường học tại Việt Nam - Giáo dục thể chất).',
    'REC_DIR_0127': 'Khôi phục bất bình đẳng sức khỏe (Health Disparities) khi thiếu hụt dữ liệu — liên quan đạo đức dữ liệu y tế.',
    'REC_DIR_0129': 'Đánh giá độ chính xác chẩn đoán và tiết kiệm nguồn lực cho xét nghiệm lao phổi tại Việt Nam.',
    'REC_DIR_0131': 'Nghiên cứu định tính về thực trạng và tương lai chấp nhận AI trong hệ thống y tế Đông Nam Á (bao gồm Việt Nam).',
    'REC_DIR_0134': 'EX02_NOT_HEALTHCARE (An toàn tâm lý và việc chấp nhận AI ảnh hưởng đến kiệt sức nghề nghiệp của giáo viên phổ thông).',
    'REC_DIR_0136': 'Cảm biến sinh hiệu đeo phát hiện sớm sốt xuất huyết nặng và nhiễm trùng huyết tại vùng nguồn lực hạn chế (LMIC/Việt Nam).',
    'REC_DIR_0137': 'EX01_NOT_AI (Đo lường tình cảm chủng tộc trên mạng xã hội - Xã hội học/Truyền thông).',
    'REC_DIR_0138': 'EX02_NOT_HEALTHCARE (Mô hình dự báo chất lượng không khí dựa trên AI tại TP.HCM - Môi trường).',
    # Batch 7
    'REC_DIR_0139': 'Ý định sử dụng AI trong giáo dục sức khỏe sinh sản và tình dục của giáo viên tiểu học tại Việt Nam.',
    'REC_DIR_0140': 'Hệ thống trí tuệ địa không gian AI dự báo sớm bệnh sốt xuất huyết khu vực Đông Nam Á (bao gồm Việt Nam).',
    'REC_DIR_0141': 'Định hướng ứng dụng công nghệ cao và y tế số tại Bệnh viện Thống Nhất (Trung tâm Lão khoa hàng đầu Việt Nam).',
    'REC_DIR_0142': 'EX01_NOT_AI (Mục lục chỉ mục tạp chí, không có nội dung nghiên cứu).',
    'REC_DIR_0143': 'Đề cương mô hình tiên lượng và kế hoạch phân tích thống kê bệnh viêm gan B mạn tính tại Việt Nam.',
    'REC_IND_0001': 'EX02_NOT_HEALTHCARE (Đánh giá rủi ro ngập lụt tại Quảng Nam bằng AI - Môi trường/Địa lý).',
    'REC_IND_0002': 'Đánh giá khả năng cung cấp thông tin ung thư đa ngôn ngữ của Generative AI Chatbots — giao tiếp y tế bệnh nhân.',
    'REC_IND_0003': 'Trực tiếp sử dụng ML tiên lượng rủi ro loãng xương ở phụ nữ cao tuổi Việt Nam.',
    'REC_IND_0004': 'Tiên lượng kết cục bệnh sốt xuất huyết tại Việt Nam (Dữ liệu lâm sàng/Dịch tễ Việt Nam).',
    'REC_IND_0005': 'EX02_NOT_HEALTHCARE (Tổng quan IoT và AI tác động đến các ngành công nghiệp chung - Kinh tế/An ninh mạng).',
    'REC_IND_0006': 'Trực tiếp áp dụng ML tiên lượng bệnh tăng huyết áp tại vùng Tây Bắc Việt Nam.',
    'REC_IND_0008': 'So sánh các yếu tố tử vong do đột quỵ tại Việt Nam với mô hình Học máy có thể giải thích (Explainable AI - XAI).',
    'REC_IND_0010': 'Trực tiếp xây dựng thang điểm rủi ro ML tiên lượng thở máy cho trẻ em sốc sốt xuất huyết tại Bệnh viện Nhi đồng TP.HCM.',
    'REC_IND_0011': 'EX02_NOT_HEALTHCARE (Sử dụng GIS và ML dự báo bệnh trên tôm nuôi vùng ĐBSCL - Thủy sản/Nông nghiệp).',
    'REC_IND_0012': 'Trực tiếp ứng dụng thuật toán ML hỗ trợ bác sĩ chẩn đoán bệnh đái tháo đường tại Việt Nam.',
    'REC_IND_0013': 'Thẩm định mô hình ML đa chiều đánh giá các thông số liên quan đến COVID-19 tại Việt Nam.',
    'REC_IND_0014': 'Trực tiếp đánh giá hiệu quả của AI trong sàng lọc bệnh lý võng mạc đái tháo đường tại cộng đồng tỉnh Bình Định, Việt Nam.',
    'REC_IND_0015': 'Mô hình ML dự báo rủi ro dịch bệnh dựa trên khí hậu - sức khỏe tại Bà Rịa - Vũng Tàu, Việt Nam.',
    'REC_IND_0016': 'Thuật toán ML tiên lượng tử vong nội viện cho bệnh nhân cao tuổi nhồi máu cơ tim tại Việt Nam.',
    'REC_IND_0017': 'Rà soát phạm vi sử dụng AI trong chương trình sàng lọc ung thư tại các nước ASEAN (bao gồm Việt Nam).'
}

overrides = ['REC_DIR_0088', 'REC_DIR_0091']

rows = []
with open(csv_path, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    for r in reader:
        if r['record_id'] in rich_reasons:
            reason = rich_reasons[r['record_id']]
            r['screening_reason'] = reason
            if r['record_id'] in overrides:
                r['human_approval'] = 'OVERRIDDEN_BY_DAO_TRUNG_THANH'
                r['screening_recommendation'] = 'INCLUDE_ROUND_1'
                r['screening_status_round_1'] = 'PASSED_TO_ROUND_2'
            else:
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

print(f"Successfully updated CSV workspace with rich reasons and approvals for {len(rich_reasons)} records.")
