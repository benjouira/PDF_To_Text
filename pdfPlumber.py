# pip install pdfplumber -q

import pdfplumber

pdf = pdfplumber.open('file.pdf')

page = pdf.pages[1]

text = page.extract_text()

print(text)
