import pandas as pd
import numpy as np
import os
import sys
import csv
from sklearn.metrics import f1_score
from goatools.semantic import lin_sim
import os
from goatools.associations import dnld_assc
from goatools.semantic import TermCounts, get_info_content
from goatools.associations import read_associations
from collections import defaultdict
from goatools.obo_parser import GODag
from matplotlib import pyplot as plt
from itertools import islice
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

def sim_sem(x,y):
   term = []
   for w in x:
       for w1 in y:
         try:
           sim_l = lin_sim(w, w1, godag, termcounts)
           if sim_l == None:
               pass
           else:
               term.append(sim_l)
         except KeyError:
           continue
   return(np.mean(term))

mean=[]
num=[]
df = pd.read_csv('/storage/pronozinau/bigDATA/GO/odb10v0_gene_xrefs_onlyGO.tab', sep='\t', header=None)
df.columns = ['ort', 'GO', '3']
zipbO = zip(df['ort'].to_list(), df['GO'].to_list())
my_dict = defaultdict(list)
for k, v in zipbO:
     my_dict[k].append(v)
#my_dict = read_associations('/sf/smpdata1/pronozinau/GO_slim/GO_slim.csv', 'id2gos')

godag = GODag("go-basic.obo")
fin_gaf = os.path.join(os.getcwd(), "tair.gaf")
associations = dnld_assc(fin_gaf, godag)
termcounts = TermCounts(godag, associations)
godag = GODag("go-basic.obo")

def find_csv_filenames( path_to_dir, suffix=".csv" ):
    filenames = listdir(path_to_dir)
    return [ filename for filename in filenames if filename.endswith( suffix ) ]
blat = find_csv_filenames("/storage/pronozinau/bigDATA/clustalw/group1", "csv")
for file in blat:
  try:
    print(file)
    clust = pd.read_csv('/storage/pronozinau/bigDATA/clustalw/group1/' + file, sep='\t', header=None)
    blast = pd.read_csv('/storage/pronozinau/bigDATA/Methods/metout/group1_UseL/' + file, sep='\t', header=None)
    clust.columns = ['ort', 'id', 'num']
    blast.columns = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
    zipbClu = zip(clust['ort'].to_list(),clust['id'].to_list())
    dictClu = dict(zipbClu)
    zipbBla = zip(blast['2'].to_list(),blast['1'].to_list())
    dictBla = dict(zipbBla)
    GOC=[]
    GOB=[]
    wordC=[]
    wordB=[]
    n=1
    while n<=30:
       inn = list(dictClu)[:n]
       onn = list(dictBla)[:n]
       for w in inn:
            if w in my_dict:
               f = my_dict[w]
            else:
               pass
       GOC.extend(f)
       wordC.append(w)
       for w in onn:
            if w in my_dict:
               d = my_dict[w]
            else:
               pass
       GOB.extend(d)
       wordB.append(w)
       #test = f1_score(GOC, GOB, average='macro')
       sim=sim_sem(GOC,GOB)
       #print(sim)
       #test = TP_FP(GOC,GOB)
       n=n+1
       #print(test)
       mean.append(sim)
       num.append(n-1)
  except FileNotFoundError:
     continue
       #print(wordC, wordB, GOC, GOB, test)
q = open('UseL.csv' , 'w')
writer = csv.writer(q, delimiter='\t')
writer.writerows(zip(num,mean))