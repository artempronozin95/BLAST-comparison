import pandas as pd
import numpy as np
import os
import sys
import phylopandas as ph

file1 = sys.argv[1]
file2 = sys.argv[2]

df = pd.read_csv(file1, sep='\t')
df.columns = ['id' , 'GOid' , 'GOterm']

dd = ph.read_fasta(file2)

result = pd.merge(dd, df, how='left', on=['id'])
result = result[['id' , 'GOid', 'GOterm']]

f = len(result.index)

pd.options.display.max_rows = f
print (result)
#result = result.dropna()
#result.to_csv( file2.csv, sep ='\t')
