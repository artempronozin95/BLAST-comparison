import pandas as pd
import numpy as np
import os
import sys
import csv
import itertools
from goatools.associations import read_associations
from collections import defaultdict
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

def empt(x):
  for k in x.keys():
      try:
         if len(x[k])<1:
            del x[k]
      except: pass
  return (x)

def Precision(x,y):
    if x+y == 0:
       return float(0)
    else:
       return x/(x+y)
def Sensitivity(x,y):
    if x+y == 0:
       return float(0)
    else:
       return x/(x+y)
def F1(x,y):
    if x+y == 0:
       return float(0)
    else:
       return 2*(x*y)/(x+y)
def TP_FP(x,y):
  if not x:
     return(np.nan)
  if not y:
     return(np.nan)
  else:
    TP = 0
    FP = 0
    FN = 0
    TN = 0
    for w in y:
        if w in x:
           TP = TP+1
        else:
           FP = FP+1
    for w in x:
       if w in y:
          TN = TN+1
       else:
          FN = FN+1
    #print(w, TP , FP , FN)
    Pre = Precision(TP,FP)
    Sen = Sensitivity(TP,FN)
    F = F1(Pre,Sen)
    #    return (Pre , Sen , F1)
    #return (Pre)
    #return (Sen)
    return (F)
mean=[]
num=[]
#df = pd.read_csv('/sf/smpdata1/pronozinau/OrthoDB/odb10v0_gene_xrefs_onlyGO.tab', sep='\t', header=None)
#df.columns = ['ort', 'GO', '3']
#zipbO = zip(df['ort'].to_list(), df['GO'].to_list())
#my_dict = defaultdict(list)
#for k, v in zipbO:
#     my_dict[k].append(v)
my_dict = read_associations('/sf/smpdata1/pronozinau/Blast_test/GO_slim/GO_slim.csv', 'id2gos')

#def find_csv_filenames( path_to_dir, suffix=".csv" ):
#    filenames = listdir(path_to_dir)
#    return [ filename for filename in filenames if filename.endswith( suffix ) ]
#ba = find_csv_filenames("/sf/smpdata1/pronozinau/clust/group3", "csv")
ba = pd.read_csv('/storage/pronozinau/OrthoDB/mono_sp.csv', sep=',')
for w in ba['0']:
   try:    
    clustal = pd.read_csv('/storage/pronozinau/OrthoDB/clustalw/group_1/' + w + '.csv', sep='\t', header=None)
    blast = pd.read_csv('/storage/pronozinau/ALL_base_OtrhoDB/metout/group1_bla/' + w + '.csv', sep='\t', header=None)
    first = pd.read_csv('first_prot.csv', sep='\t', header=None)

    blast.columns = ['id_prot', 'id_orth', 'persent', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
    clustal.columns = ['id_orth', 'id_prot', 'persent', '4']
    first.columns = ['ort', 'id',  'gr']

    zipbClu = zip(clustal['id_orth'].to_list(),clustal['persent'].to_list())
    dictClu = dict(zipbClu)
    zipbCluOrt = zip(clustal['id_orth'].to_list(),clustal['id_orth'].to_list())
    dictCluOrt = dict(zipbCluOrt)
    zipbBla = zip(blast['id_orth'].to_list(),blast['id_orth'].to_list())
    dictBla = dict(zipbBla)
    zipfir = zip(first['ort'].to_list(),first['ort'].to_list())
    dictfir = dict(zipfir)

    for w in dictfir:
        if w in dictBla:
           del dictBla[w]
        if w in dictCluOrt:
           del dictCluOrt[w]
                                              
    GOC=[]
    GOB=[]
    wordC=[]
    wordB=[]
    n=1
    while n<=30:
       inn = list(dictCluOrt)[:n]
       onn = list(dictBla)[:n]
       for w in inn:
            if w in my_dict:
               p = my_dict[w]
            else:
               p = np.nan
       GOC.append(p)
       GOC_nan = [x for x in GOC if str(x) != 'nan']
       GOC_ap = list(itertools.chain.from_iterable(GOC_nan))
       wordC.append(w)
       for w in onn:
            if w in my_dict:
               d = my_dict[w]
            else:
               d = np.nan
       GOB.append(d)
       GOB_nan = [x for x in GOB if str(x) != 'nan']
       GOB_ap = list(itertools.chain.from_iterable(GOB_nan))
       wordB.append(w)
       test = TP_FP(GOC_ap,GOB_ap)
       n=n+1
       mean.append(test)
       num.append(n-1)
   except FileNotFoundError:
     continue
q = open('Bla_gr1.csv' , 'w')
writer = csv.writer(q, delimiter='\t')
writer.writerows(zip(num,mean))
