# pip install "camelot-py[cv]"

## Camelot
import camelot
table_c = camelot.read_pdf('file.pdf', pages='all')
df = pd.DataFrame()
for j in range(len(table_c)):
 df_c = table_c[j].df
df = df.append(remove_spaces(split_newline(df_c)))
