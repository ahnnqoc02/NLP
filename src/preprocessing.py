import re
import fitz
import underthesea
import unicodedata
def read_pdf(path: str) -> str:
    reader = fitz.open(path)
    print(f'Đã đọc từ {path}, tổng số trang: {len(reader)}')
    
    all_text = '\n'.join([page.get_text().replace('\x00', '') for _,page in enumerate(reader)])
    
    all_text = unicodedata.normalize('NFC', all_text)
    return all_text



def clean_administrative_text(text: str) -> str:
    """
    Dọn dẹp các thành phần thừa trong văn bản hành chính Việt Nam.
    """
    # 1. Xóa tiêu ngữ "CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM" và "Độc lập - Tự do - Hạnh phúc"
    text = re.sub(r'(?i)CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM\s*', '', text)
    text = re.sub(r'(?i)Độc lập\s*-\s*Tự do\s*-\s*Hạnh phúc\s*', '', text)
    
    
    # 3. Xóa các dòng "Căn cứ..." (Xóa toàn bộ dòng bắt đầu bằng Căn cứ cho đến dấu chấm hoặc xuống dòng)
    text = re.sub(r'(?m)^Căn cứ\s+.*?(?:\.|\n|$)', '', text)
    
    # 4. Xóa số trang (Thường đứng độc lập ở đầu/cuối dòng hoặc có chữ "Trang ...")
    text = re.sub(r'(?m)^\s*\d+\s*$', '', text) # Số trang chỉ là số đứng cô lập một dòng
    
    # 5. Xóa các ký tự đặc biệt, ký tự rác không mang ý nghĩa (giữ lại chữ, số, khoảng trắng và dấu câu cơ bản)
    # Loại bỏ các ký tự lạ phát sinh do lỗi đọc PDF như:  ,  , , █, ░, ❖, các dấu gạch trang trí...
    text = re.sub(r'[^\w\s,.:;\-\?!\(\)à-ỹÀ-ỸđĐ]', '', text)
    
    # 6. Chuẩn hóa khoảng trắng (Xóa dòng trống thừa, xóa dấu cách thừa)
    text = re.sub(r'\n\s*\n+', '\n', text)  # Gom nhiều dòng trống thành 1 dòng trống
    text = re.sub(r'[ \t]+', ' ', text)     # Gom nhiều dấu cách thành 1 dấu cách
    
    return text.strip()


def sentence_segment(text: str) -> str:
    patterns = r'(?<=[.:;])\s+'
    sentences = re.split(patterns, text)
    cleaned_sentences = '\n'.join([sent.strip() for sent in sentences if sent.strip()])
    return cleaned_sentences

def print_text(text: str) -> None:
    chunk_size = 2000
    for i in range(0, len(text), chunk_size):
        print(text[i:i+chunk_size])
    return None
text = read_pdf('data/raw/luat116-2025.pdf')
text = clean_administrative_text(text)
print_text(sentence_segment(text))
print('hehe')
