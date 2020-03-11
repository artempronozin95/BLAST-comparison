import numpy as np
import pandas as pd
import ml_metrics as metrics
import sys
from statistics import mean
import seaborn as sns
from matplotlib import pyplot as plt
import os
from os import listdir
def set_size(w,h, ax=None):
    if not ax: ax=plt.gca()
    l = ax.figure.subplotpars.left
    r = ax.figure.subplotpars.right
    t = ax.figure.subplotpars.top
    b = ax.figure.subplotpars.bottom
    figw = float(w)/(r-l)
    figh = float(h)/(t-b)
    ax.figure.set_size_inches(figw, figh)

df = pd.read_csv('Blastmean.csv', sep='\t', header=None)
df1 = pd.read_csv('Diamean.csv', sep='\t', header=None)
df2 = pd.read_csv('Usemean.csv', sep='\t', header=None)
df3 = pd.read_csv('Mmseqmean.csv', sep='\t', header=None)
df4 = pd.read_csv('UseLmean.csv', sep='\t', header=None)
df5 = pd.read_csv('BlastFmean.csv', sep='\t', header=None)

df.columns = ['n', 'Blast']
df1.columns = ['n', 'Diamond']
df2.columns = ['n', 'Usearch']
df3.columns = ['n', 'Mmseq2']
df4.columns = ['n', 'UseLocal']
df5.columns = ['n', 'BlastFast']

blast = df['Blast']
blastf = df5['BlastFast']
dia = df1['Diamond']
use = df2['Usearch']
mmseq = df3['Mmseq2']
useloc = df4['UseLocal']
k = df4['n']


plt.plot(k, blast, color='green', linewidth = 2, label='Blast')
plt.plot(k, dia, color='red', linewidth = 2,  label='Diamond')
plt.plot(k, use, color='blue', linewidth = 2,  label='Usearch ublast')
plt.plot(k, blastf, color='black', linewidth = 2, label='Blast-fast')
plt.plot(k, mmseq, color='pink', linewidth = 2, label='Mmseq2')
plt.plot(k, useloc, color='orange' , linewidth = 2, label='Usearch local')
plt.tick_params(labelsize=20)
plt.legend(fontsize='xx-large', title_fontsize='20')
plt.xticks(np.arange(0, 31, 5))
plt.ylabel('Metric', size=25)
plt.xlabel('k', size=25)
plt.xlim(0, 30)
#plt.ylim(0.48,0.55)
plt.title('Semantic similarity Old group', size=25)
set_size(15,7)
plt.savefig('Mean_GO_sem_gr1.png')


