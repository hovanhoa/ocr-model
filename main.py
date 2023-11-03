import sys
import pytesseract
import preprocessing
from extraction import extraction
import text_similarity

# pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files\Tesseract-OCR\\tesseract.exe'


def main(img_path, text):
    img = preprocessing.preprocessing(img_path)
    str = pytesseract.image_to_string(img, lang="vie")
    str = extraction.extraction_text(str.lower())
    return text_similarity.text_similarity(str, text) > 0.5


if __name__ == '__main__':
    img_path = str(sys.argv[1])
    text = str(sys.argv[2])
    print(main(img_path, text))
