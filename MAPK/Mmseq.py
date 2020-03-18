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

mmseq = pd.read_csv(file1,sep='\t', header=None)
clustal = pd.read_csv(file2, sep='\t', header=None)

mmseq.columns = ['id_prot', 'id_orth', 'persent', '3', '4', '5', '6', '7', '8', '9', '10', '11']
clustal.columns = ['id_orth', 'id_prot', 'persent']

id_orth_clust = clustal['id_orth']
id_orth_mmseq = mmseq['id_orth']

k_mmseq = len(id_orth_mmseq.index)

print ("MMSEQ2")

def stop (x,y,z,a):
    if z > len(y):
       sys.exit()
    else:
       return metrics.apk(x,y,a)


while n < 100:
    actual = id_orth_clust.to_list()[:n]
    mmsq = id_orth_mmseq.to_list()[:n]
    apk_mmseq = stop(actual, mmsq, n, k_mmseq)
    n = n + 1
    print (apk_mmseq)

