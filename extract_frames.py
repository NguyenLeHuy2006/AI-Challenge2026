import cv2
import os
import unicodedata
import re

def make_safe_filename(text):
    """Hàm khử dấu tiếng Việt và làm sạch tên file"""
    text = unicodedata.normalize('NFD', text)
    text = re.sub(r'[\u0300-\u036f]', '', text)
    text = text.replace('đ', 'd').replace('Đ', 'D')
    text = re.sub(r'[^\w\s-]', '', text).strip().replace(' ', '_')
    return text.lower()

def extract_frames(video_path, output_dir, interval_seconds=1):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"❌ Lỗi: Không thể mở video tại {video_path}")
        return

    fps = int(cap.get(cv2.CAP_PROP_FPS))
    if fps == 0: fps = 30 
        
    frame_interval = fps * interval_seconds
    frame_count = 0
    saved_count = 0

    while True:
        ret, frame = cap.read()
        if not ret: break

        if frame_count % frame_interval == 0:
            video_name = os.path.splitext(os.path.basename(video_path))[0]
            safe_video_name = make_safe_filename(video_name) 
            filename = f"{safe_video_name}_frame_{saved_count:04d}.jpg"
            filepath = os.path.join(output_dir, filename)
            
            cv2.imwrite(filepath, frame)
            saved_count += 1

        frame_count += 1

    cap.release()
    print(f" -> Hoàn thành! Đã trích xuất {saved_count} ảnh.")

# --- BỘ LỌC THÔNG MINH: TRÁNH CẮT TRÙNG LẶP ---
if __name__ == "__main__":
    RAW_FOLDER = "data/raw/"
    PROCESSED_FOLDER = "data/processed/"
    VIDEO_EXTENSIONS = ('.mp4', '.avi', '.mov', '.mkv')
    
    if not os.path.exists(PROCESSED_FOLDER):
        os.makedirs(PROCESSED_FOLDER)

    print(f"🔍 Đang quét tìm video mới trong thư mục: {RAW_FOLDER}")
    
    # Lấy danh sách tất cả các file đang có sẵn trong thư mục processed để check cho nhanh
    already_processed_files = os.listdir(PROCESSED_FOLDER)
    
    video_found = 0
    for filename in os.listdir(RAW_FOLDER):
        if filename.lower().endswith(VIDEO_EXTENSIONS):
            video_found += 1
            video_path = os.path.join(RAW_FOLDER, filename)
            
            # 1. Lấy tên video và làm sạch để check
            video_name = os.path.splitext(filename)[0]
            safe_video_name = make_safe_filename(video_name)
            
            # 2. KIỂM TRA: Nếu đã có bất kỳ file ảnh nào bắt đầu bằng tên video này thì BỎ QUA
            # Ví dụ: nếu trong folder đã có file "bao_trai_cay_frame_0000.jpg" -> Bỏ qua video Bão Trái Cây
            is_done = any(f.startswith(safe_video_name) for f in already_processed_files)
            
            if is_done:
                print(f"⏩ [{video_found}] Bỏ qua: Video '{filename}' đã được xử lý trước đó.")
                continue
                
            print(f"\n🚀 [{video_found}] Đang xử lý video mới: {filename}...")
            extract_frames(video_path, PROCESSED_FOLDER, interval_seconds=1)
            
    if video_found == 0:
        print("Không tìm thấy file video nào!")
    else:
        print("\n🎉 Kiểm tra đồng bộ dữ liệu hoàn tất!")