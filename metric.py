import numpy as np
import pandas as pd
import ml_metrics as metrics
import sys
import os


file1 = sys.argv[1]
file2 = sys.argv[2]
file3 = sys.argv[3]
file4 = sys.argv[4]
file5 = sys.argv[5]
n=0

base = os.path.basename(file1)
base = os.path.splitext(base)[0]
#prot, no = base.split("_", 1)

blast = pd.read_csv(file1, sep='\t', header=None)
diamond = pd.read_csv(file2, sep='\t', header=None)
clustal = pd.read_csv(file3, sep='\t', header=None)
usearch = pd.read_csv(file4, sep='\t', header=None)
blastfast = pd.read_csv(file5,sep='\t', header=None)

blast.columns = ['id_prot', 'id_orth', 'persent', '3', '4', '5', '6', '7', '8', '9', '10', '11']
diamond.columns = ['id_prot', 'id_orth', 'persent', '3', '4', '5', '6', '7', '8', '9', '10', '11']
clustal.columns = ['id_orth', 'id_prot', 'persent']
usearch.columns = ['id_prot', 'id_orth', 'persent', '3', '4', '5', '6', '7', '8', '9', '10', '11']
blastfast.columns = ['id_prot', 'id_orth', 'persent', '3', '4', '5', '6', '7', '8', '9', '10', '11']

id_orth_blast = blast['id_orth']
id_orth_diam = diamond['id_orth']
id_orth_clust = clustal['id_orth']
id_orth_use = usearch['id_orth']
id_orth_blastfast = blastfast['id_orth']

k_blast = len(id_orth_blast.index)
k_dia = len(id_orth_diam.index)
k_use = len(id_orth_use.index)
k_blastfast = len(id_orth_blastfast.index)

print ("BLAST",'\t',"BLAST-FAST", '\t', "DIAMOND",'\t', "USEARCH",'\t', "k")
while n < 100:
    actual = id_orth_clust.to_list()[:n]
    n = n + 1
    apk_blast = metrics.apk(actual,id_orth_blast.to_list(), k_blast)
    apk_blastfast = metrics.apk(actual,id_orth_blastfast.to_list(), k_blastfast)
    apk_dia = metrics.apk(actual,id_orth_diam.to_list(), k_dia)
    apk_use = metrics.apk(actual,id_orth_use.to_list(), k_use)
    print (apk_blast,'\t',apk_blastfast,'\t', apk_dia,'\t',apk_use,'\t', n)

