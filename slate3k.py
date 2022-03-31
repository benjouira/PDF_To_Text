# pip install slate3k

import slate3k as slate
text  = (slate.PDF(open('file.pdf', 'rb')))

print(text)



# ***************************

# pip install tabula-py

import tabula


# Read pdf into a list of DataFrame
dfs = tabula.read_pdf("file.pdf", pages='all')
print(dfs)

print(type(dfs[0]))

print(dfs[0].info() )

print(dfs[0]["columnName"][1])

# every pdf file hase his personal template
