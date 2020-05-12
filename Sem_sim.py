import pandas as pd
import numpy as np
import os
import sys
import csv
from goatools.semantic import lin_sim
import os
import itertools
from goatools.associations import dnld_assc
from goatools.semantic import TermCounts, get_info_content
from goatools.associations import read_associations
from collections import defaultdict
from goatools.obo_parser import GODag
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
df = pd.read_csv('/sf/smpdata1/pronozinau/Blast_test/odb10v0_gene_xrefs_onlyGO.tab', sep='\t', header=None)
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

#def find_csv_filenames( path_to_dir, suffix=".csv" ):
#    filenames = listdir(path_to_dir)
#    return [ filename for filename in filenames if filename.endswith( suffix ) ]
#blat = find_csv_filenames("/storage/pronozinau/ALL_base_OtrhoDB/metout/group3_bla/", "csv")
blat = pd.read_csv('/storage/pronozinau/OrthoDB/mono_sp.csv', sep=',')
for w in blat['0']:
  try:
    clustal = pd.read_csv('/storage/pronozinau/OrthoDB/clustalw/group_3/' + w + '.csv', sep='\t', header=None)
    blast = pd.read_csv('/storage/pronozinau/ALL_base_OtrhoDB/metout/group3_bla/' + w + '.csv', sep='\t', header=None)
    first = pd.read_csv('first_prot.csv', sep='\t', header=None)

    blast.columns = ['id_prot', 'id_orth', 'persent', '3', '4', '5', '6', '7', '8', '9', '10', '11']
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
    while n<=5:
       inn = list(dictCluOrt)[:n]
       onn = list(dictBla)[:n]
       for w in inn:
           if w in my_dict:
               f = my_dict[w]
           else:
               f= np.nan
       GOC.append(f)
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
       sim=sim_sem(GOC_ap,GOB_ap)
       n=n+1
       mean.append(sim)
       num.append(n-1)
       print(wordC, wordB, GOC_ap, GOB_ap, sim)
  except FileNotFoundError:
     continue
q = open('Bla_gr3_5.csv' , 'w')
writer = csv.writer(q, delimiter='\t')
writer.writerows(zip(num,mean))
