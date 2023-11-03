import sys
 
# setting path
sys.path.append('../')

import pytesseract
from extraction import extraction
import preprocessing
import text_similarity
import time

from test import test_constants


# pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files\Tesseract-OCR\\tesseract.exe'

def main():
    data = test_constants.TEST_DATA

    fails = 0
    start = time.time()
    for idx, r in enumerate(data):
        img = preprocessing.preprocessing(r)
        str = pytesseract.image_to_string(img, lang="vie")
        str = extraction.extraction_text(str.lower())
        result = text_similarity.text_similarity(str, data[r])
        print('TEST # {:<2} - {:<15}: {:<20} - {}'.format(idx + 1, r, result, result > 0.5))
        fails = fails if result > 0.5 else fails + 1
    end = time.time()

    print("="*57)
    print("Ran {} tests in {}s".format(len(data), end - start))
    print("\nFAILED (wrong={})".format(fails) if fails else "OK")
