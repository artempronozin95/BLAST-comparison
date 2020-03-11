import numpy as np
import pandas as pd
import ml_metrics as metrics
import sys
from statistics import mean
from matplotlib import pyplot as plt
import os
from os import listdir

file1 = sys.argv[1] # blast
file2 = sys.argv[2] # Diamond
file3 = sys.argv[3] # usearch
file4 = sys.argv[4] # Blastfast
file5 = sys.argv[5] # MMseq2
file6 = sys.argv[6] # UseLocal

df1 = pd.read_csv(file1, sep=' ')
df2 = pd.read_csv(file2, sep=' ')
df3 = pd.read_csv(file3, sep=' ')
df4 = pd.read_csv(file4, sep=' ')
df5 = pd.read_csv(file5, sep=' ')
df6 = pd.read_csv(file6, sep=' ')

data = pd.concat([df1,df2], ignore_index=True, axis=1)
data2 = pd.concat([df3,df5], ignore_index=True, axis=1)
data3 = pd.concat([df6,df4], ignore_index=True, axis=1)
data4 = pd.concat([data,data2], ignore_index=True, axis=1)
dataall = pd.concat([data4,data3], ignore_index=True, axis=1)
dataall.columns = ['Blast', 'Diamond', 'Usearch', 'Mmseq2', 'UseLocal', 'BlastFast', 'k']

#print (dataall)
#K =100

#def find_csv_filenames( path_to_dir, suffix=".csv" ):
#    filenames = listdir(path_to_dir)
#    return [ filename for filename in filenames if filename.endswith( suffix ) ]

#df_list = []
#files = find_csv_filenames(".","csv")
#for file in files:
#    print(file)
#    df = pd.read_csv(file, sep='\t')
#    df_list.append(df)
#df = pd.concat(df_list)
#ort.columns = ['BLAST','num_seqB','DIAMOND','num_seqD', 'USEARCH','num_seqU','BLAST-FAST','num_seqBF', 'k']
#r = pd.DataFrame(df).groupby(df.k).mean()


base = os.path.basename(file1)
base = os.path.splitext(base)[0]
prot, no = base.split("_", 1)

f = len(dataall.index)
pd.options.display.max_rows = f
dataall.to_csv(prot + '.csv', sep='\t', )

df1.columns = ['Bla']
df2.columns = ['Dia']
df3.columns = ['Use']
df4.columns = ['Blaf', 'k']
df5.columns = ['Mmseq2']
df6.columns = ['UseLocal']


blast = df1['Bla']
blastf = df4['Blaf']
dia = df2['Dia']
use = df3['Use']
k = df4['k']
mmseq = df5['Mmseq2']
useloc = df6['UseLocal']
bla = len(blast)
blaf = len(blastf)
diam = len(dia)
usee = len(use)
mmsq = len(mmseq)
uselo = len(useloc)


#plt.plot(k[:bla], blast, color='green', linewidth = 2, label='Blast')
#plt.plot(k[:diam], dia, color='red', linewidth = 2,  label='Diamond')
#plt.plot(k[:usee], use, color='blue', linewidth = 2,  label='Usearch')
#plt.plot(k[:blaf], blastf, color='black', linewidth = 2, label='Blast-fast')
#plt.plot(k[:mmsq], mmseq, color='pink', linewidth = 2, label='Mmseq2')
#plt.plot(k[:uselo], useloc, color='orange' , linewidth = 2, label='UseLocal')
#plt.legend(loc = 'best')
#plt.xlabel('k')
#plt.ylabel('methods')
#plt.title(prot)
#plt.savefig(prot)


