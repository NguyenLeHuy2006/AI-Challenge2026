<<<<<<< HEAD
# AI_Challenge26
Làm việc ở đây nheee
=======
# 🗄️ AI Data Pipeline & Text Processing (Nhánh: AI Data)

Nhánh này chứa các công cụ xử lý dữ liệu đầu vào (Data Preparation) và chuẩn hóa ngôn ngữ tự nhiên (NLP) cho dự án Trợ lý ảo AI Challenge HCMC 2026.
**Người phụ trách:** Lê Huy (Leader / Data Pipeline)

---

## 🎯 Mục tiêu của Module
1. **Xử lý Video/Ảnh thô:** Tự động cắt video thành các frame ảnh rời, bỏ qua video trùng lặp và làm sạch tên file tiếng Việt.
2. **Crawl Dữ liệu:** Tự động tải ảnh mẫu theo chủ đề/từ khóa để phục vụ quá trình test mô hình.
3. **Chuẩn hóa Text:** Tiền xử lý câu lệnh tìm kiếm của người dùng (khử dấu, chuẩn hóa Unicode NFC, loại bỏ ký tự đặc biệt) trước khi đưa vào mô hình AI.

---

## 📂 Cấu trúc thư mục (Nhánh Data)

```text
core_ai/
│
├── data/                    # (⚠️ KHÔNG PUSH THƯ MỤC NÀY LÊN GIT)
│   ├── raw/                 # Chứa file video (.mp4, .avi) và ảnh hỗn hợp tải về
│   └── processed/           # Chứa ảnh (.jpg) đã được cắt frame & đổi tên an toàn
│
├── extract_frames.py        # Script quét thư mục raw và cắt frame từ video
├── extract_image.py         # Script tự động cào ảnh mẫu từ LoremFlickr
├── text_processing.py       # Script chứa hàm `clean_vietnamese_text`
├── requirements_data.txt    # Thư viện riêng cho nhánh này
└── README.md                # Tài liệu hướng dẫn nhánh Data
```

---

## ⚙️ Cài đặt Môi trường

Mở Terminal tại thư mục hiện tại và chạy lệnh cài đặt các thư viện cần thiết:

```bash
pip install opencv-python requests
```

*(Lưu ý: Không cần cài thêm các thư viện AI nặng nề ở nhánh này, chỉ cần thư viện xử lý ảnh và web tĩnh).*

---

## 🚀 Hướng dẫn Sử dụng (Cho AI 2 & AI 3)

### 1. Chuẩn bị ảnh mẫu (Chạy tự động)
Để tải nhanh các ảnh mẫu phục vụ test mô hình, chạy lệnh:
```bash
python extract_image.py
```
*Bạn có thể mở file code và đổi từ khóa `traffic` thành các từ khác như `food`, `office`, `people` để cào thêm ảnh.*

### 2. Cắt Frame từ Video thô
Bỏ tất cả các file video lẫn ảnh lộn xộn vào thư mục `data/raw/`. Sau đó chạy lệnh:
```bash
python extract_frames.py
```
*Hệ thống sẽ tự động:*
- Lọc ra các file video để xử lý.
- Làm sạch tên file tiếng Việt thành không dấu.
- Cứ 1 giây cắt ra 1 frame ảnh và lưu vào `data/processed/`.
- Tự động **BỎ QUA** những video đã từng được cắt trước đó để tiết kiệm thời gian.

### 3. Gọi hàm chuẩn hóa Text Tiếng Việt (Cho bạn AI 3)
Trong file xử lý của AI 3, hãy import hàm làm sạch chữ của nhánh này trước khi đưa chuỗi vào model CLIP:

```python
# Import hàm từ file của nhánh Data
from text_processing import clean_vietnamese_text

query = "  TÌM cho TÔI 1 chiếc XÊ ô tô!!!  "
clean_query = clean_vietnamese_text(query)

print(clean_query)
# Kết quả an toàn để model đọc: "tim cho toi 1 chiec xe o to"
```

---

## 🛑 Lưu ý Quan trọng
- **FILE `.gitignore` LÀ BẮT BUỘC:** Tuyệt đối không dùng lệnh `git add .` khi chưa cấu hình chặn thư mục `data/`. File ảnh/video sẽ làm sập repo Git.
- Dữ liệu `data/processed/` sau khi chạy xong sẽ được nén thành file `.zip` và đẩy lên Google Drive để team tải về. Không share data qua GitHub!
>>>>>>> 0275d73 (Hoàn thiện module AI Data: Xử lý frame video, crawl ảnh và chuẩn hóa Text Tiếng Việt)
