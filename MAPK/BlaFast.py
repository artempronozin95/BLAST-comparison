import numpy as np
import pandas as pd
import ml_metrics as metrics
import sys
import os


file1 = sys.argv[1]
file2 = sys.argv[2]
n=1

#base = os.path.basename(file1)
#base = os.path.splitext(base)[0]
#prot, no = base.split("_", 1)

blastfast = pd.read_csv(file1,sep='\t', header=None)
clustal = pd.read_csv(file2, sep='\t', header=None)

blastfast.columns = ['id_prot', 'id_orth', 'persent', '3', '4', '5', '6', '7', '8', '9', '10', '11']
clustal.columns = ['id_orth', 'id_prot', 'persent']

id_orth_clust = clustal['id_orth']
id_orth_blastfast = blastfast['id_orth']

k_blastfast = len(id_orth_blastfast.index)

print ("BLAST_FAST", "k")

def stop (x,y,z,a):
    if z > len(y):
       sys.exit()
    else:
       return metrics.apk(x,y,a)


while n < 100:
    actual = id_orth_clust.to_list()[:n]
    blafa = id_orth_blastfast.to_list()[:n]
    apk_blastfast = stop(actual,blafa, n, k_blastfast)
    n = n + 1
    print (apk_blastfast, n-1)


