# utils/ocr_utils.py
from PIL import Image
import pytesseract
# 🛠 Set the full path to tesseract.exe here
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
def extract_text(image_path):
    img = Image.open(image_path)
    return pytesseract.image_to_string(img)
