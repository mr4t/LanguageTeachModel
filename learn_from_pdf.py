from pdfminer.high_level import extract_text
import re, os
def txt(name):
    if re.findall(".pdf$", name) and os.path.exists(name):
        text = extract_text(name)
        return text.split()
    else:
        print("Wrong file type or file not exists.")
