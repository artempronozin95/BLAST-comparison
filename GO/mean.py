import numpy as np
import pandas as pd
import seaborn as sns
import ml_metrics as metrics
import sys
import csv
from statistics import mean
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

df = pd.read_csv('Dia.csv', sep='\t', header=None)
df.columns = ['n', 'GO']
r = pd.DataFrame(df).groupby(df.n).mean()

f = len(r.index)
pd.options.display.max_rows = f
r['GO'].to_csv('Diamean.csv', sep='\t')



#plt.plot(r['n'], r['len'], linewidth = 2, label='GO')
#plt.legend(loc = 'best')
#plt.xlabel('n')
#plt.ylabel('GO')
#plt.title('GO')
#plt.savefig('GO.png')


