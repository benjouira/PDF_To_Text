# pip install pdftables

import pdftables

dir(pdftables)

pdf = pdftables.get_pdf_page(open('file.pdf'))

print (pdf)
