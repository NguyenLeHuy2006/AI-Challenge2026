import re
import unicodedata

def clean_vietnamese_text(text: str) -> str:
    if not text:
        return ""
        
    # Bước 1: Chuẩn hóa Unicode tiếng Việt về chuẩn NFC (Dựng sẵn)
    text = unicodedata.normalize('NFC', text)
    
    # Bước 2: Chuyển toàn bộ thành chữ thường
    text = text.lower()
    
    # Bước 3: Loại bỏ các ký tự đặc biệt, dấu câu, emoji (chỉ giữ lại chữ cái, số và khoảng trắng)
    # Regex [^\w\s] có nghĩa là: xóa mọi thứ KHÔNG PHẢI là chữ (\w) và KHÔNG PHẢI là khoảng trắng (\s)
    text = re.sub(r'[^\w\s]', ' ', text)
    
    # Bước 4: Xóa các khoảng trắng thừa (ví dụ: "  áo    đỏ  " -> "áo đỏ")
    text = re.sub(r'\s+', ' ', text).strip()
    
    return text

# --- ĐOẠN NÀY ĐỂ TEST THỬ ---
if __name__ == "__main__":
    # Một câu test có đủ các thể loại lỗi: Viết hoa, dấu câu, nhiều khoảng trắng, emoji
    cau_lenh_nguoi_dung = "   TÌM cho TÔI 1  chiếc XÊ ô  tô  màu Đỏ!!! 🚗🚥   "
    
    cau_da_chuan_hoa = clean_vietnamese_text(cau_lenh_nguoi_dung)
    
    print(f"Câu gốc: '{cau_lenh_nguoi_dung}'")
    print(f"Sau khi chuẩn hóa: '{cau_da_chuan_hoa}'")