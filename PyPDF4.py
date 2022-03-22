# pip install PyPDF4 

from PyPDF4 import PdfFileReader, PdfFileWriter

file_path = 'RF210145.pdf'
pdf = PdfFileReader(file_path)
