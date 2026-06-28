import requests
import os

def download_images(query, max_images=10, output_dir="data/raw/unsplash"):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    print(f"Đang tự động tải {max_images} ảnh về chủ đề '{query}'...")
    
    for i in range(max_images):
        # Thêm lock={i} để đảm bảo mỗi ảnh tải về là khác nhau
        url = f"https://loremflickr.com/800/600/{query}?lock={i}"
        try:
            # Thêm headers để giả lập trình duyệt, tránh bị web chặn
            headers = {'User-Agent': 'Mozilla/5.0'}
            response = requests.get(url, headers=headers, timeout=10)
            
            if response.status_code == 200:
                filename = f"{query}_{i:03d}.jpg"
                filepath = os.path.join(output_dir, filename)
                with open(filepath, 'wb') as f:
                    f.write(response.content)
                print(f"✅ Đã tải thành công: {filename}")
            else:
                print(f"❌ Lỗi mạng ở ảnh {i}, mã lỗi: {response.status_code}")
        except Exception as e:
            print(f"❌ Lỗi khi tải ảnh thứ {i}: {e}")
            

if __name__ == "__main__":
    download_images("street_food", max_images=50)