import pandas as pd
import numpy as np
import os
import sys
import csv
from collections import defaultdict
from goatools.associations import read_associations
from matplotlib import pyplot as plt
from itertools import islice
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


Len = []
num = []
#df = pd.read_csv('/sf/smpdata1/pronozinau/OrthoDB/odb10v0_gene_xrefs_onlyGO.tab', sep='\t', header=None)
#df.columns = ['ort', 'GO', 'term']
#zipbO = zip(df['ort'].to_list(), df['GO'].to_list())
#my_dict = defaultdict(list)
#for k, v in zipbO:
#     my_dict[k].append(v)

my_dict = read_associations('/sf/smpdata1/pronozinau/GO_slim/GO_slim.csv', 'id2gos')

def find_csv_filenames( path_to_dir, suffix=".csv" ):
    filenames = listdir(path_to_dir)
    return [ filename for filename in filenames if filename.endswith( suffix ) ]
df_list = []
files = find_csv_filenames(".","csv")
for file in files:
    print(file)
    d = pd.read_csv(file, sep='\t', header=None)
    d.columns = ['ort', 'id', 'num']
    zipbObj = zip(d['ort'].to_list(),d['id'].to_list())
    dictOf = dict(zipbObj)
    GO=[]
    n=1 
    while n <=100:
        inn = list(dictOf)[:n]
        for w in inn:
            if w in my_dict:
               f = my_dict[w]
            else:
               pass
        GO.extend(f)
        n=n+1
        new_list = []
        for w in GO:
            if w not in new_list:
               new_list.append(w)
        lenn = len(new_list)
        Len.append(lenn)
        num.append(n-1)
    #    print(n, lenn)
    #zip(num,Len)
    #base = os.path.basename(file)
    #base = os.path.splitext(base)[0]
    #prot, no = base.split("_", 1)
    #plt.plot(num, Len,  linewidth = 2, label='GO')
    #plt.legend(loc = 'best')
    #plt.xlabel('n')
    #plt.ylabel('GO')
    #plt.title('GO')
    #plt.savefig(prot + '.png')
f = open('ALL.csv' , 'w')
writer = csv.writer(f, delimiter='\t')
writer.writerows(zip(num,Len))