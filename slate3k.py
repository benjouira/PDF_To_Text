# pip install slate3k

import slate3k as slate
text  = (slate.PDF(open('file.pdf', 'rb')))

print(text)



# ***************************

# pip install tabula-py

import tabula


# Read pdf into a list of DataFrame
dfs = tabula.read_pdf("file.pdf", pages='all')
dfs

type(dfs[0])

dfs[0].info() 

dfs[0]["columnName"][1]
