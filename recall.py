import numpy as np
import pandas as pd
import ml_metrics as metrics
import sys
import os

# input all methods
file1 = sys.argv[1]
file2 = sys.argv[2]
file3 = sys.argv[3]
file4 = sys.argv[4]
file5 = sys.argv[5]
file6 = sys.argv[6]
file7 = sys.argv[7]
n=1

base = os.path.basename(file3)
base = os.path.splitext(base)[0]
prot, no = base.split("_", 1)

blast = pd.read_csv(file1, sep='\t', header=None)
diamond = pd.read_csv(file2, sep='\t', header=None)
clustal = pd.read_csv(file3, sep='\t', header=None)
usearch = pd.read_csv(file4, sep='\t', header=None)
blastfast = pd.read_csv(file5,sep='\t', header=None)
mmseq = pd.read_csv(file6,sep='\t', header=None)
uselocal = pd.read_csv(file7, sep='\t', header=None)

blast.columns = ['id_prot', 'id_orth', 'persent', '3', '4', '5', '6', '7', '8', '9', '10', '11']
diamond.columns = ['id_prot', 'id_orth', 'persent', '3', '4', '5', '6', '7', '8', '9', '10', '11']
clustal.columns = ['id_orth', 'id_prot', 'persent']
usearch.columns = ['id_prot', 'id_orth', 'persent', '3', '4', '5', '6', '7', '8', '9', '10', '11']
blastfast.columns = ['id_prot', 'id_orth', 'persent', '3', '4', '5', '6', '7', '8', '9', '10', '11']
mmseq.columns = ['id_prot', 'id_orth', 'persent', '3', '4', '5', '6', '7', '8', '9', '10', '11']
uselocal.columns = ['id_prot', 'id_orth', 'persent', '3', '4', '5', '6', '7', '8', '9', '10', '11']

id_orth_blast = blast['id_orth']
id_orth_diam = diamond['id_orth']
id_orth_clust = clustal['id_orth']
id_orth_use = usearch['id_orth']
id_orth_blastfast = blastfast['id_orth']
id_orth_mmseq = mmseq['id_orth']
id_orth_useloc = uselocal['id_orth']

k_bla = len(id_orth_blast.index)
k_dia = len(id_orth_diam)
k_use = len(id_orth_use.index)
k_blastf = len(id_orth_blastfast.index)

print ("BLAST")
print ("DIAMOND")
print ("USEARCH")
print ("BLAST_FAST", "k")
print ("MMSEQ2")
print ("USE_LOCAL")
# cases funcions recall pesicion and F1 
def Precision(x,y):
    if x+y == 0:
       return float(0)
    else:
       return x/(x+y)
def Sensitivity(x,y):
    if y == 0:
       return float(0)
    else:
       return x/y
def F1(x,y):
    if x+y == 0:
       return float(0)
    else:
       return 2*(x*y)/(x+y)
# calculation recall pesicion and F1 
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
    Pre = Precision(TP,FP)
    Sen = Sensitivity(TP,len(x))
    F = F1(Pre,Sen)
#    return (Pre , Sen , F1)
    return (Pre)
#    return (Sen)
#    return (F)
def stop (x,y,z):
    if z > len(y):
       sys.exit()
    else:
       return TP_FP(x,y)

# statistic for methods
while n <= 100:
    actual = id_orth_clust.to_list()[:n]
    blat = id_orth_blast.to_list()[:n]
    diam =id_orth_diam.to_list()[:n]
    usee = id_orth_use.to_list()[:n]
    blastf = id_orth_blastfast.to_list()[:n]
    mmsqq = id_orth_mmseq.to_list()[:n]
    usealoc = id_orth_useloc.to_list()[:n]
    bla = stop(actual, blat, n)
    dia = stop(actual, diam, n)
    use = stop(actual, usee, n)
    blaf = stop(actual, blastf, n)
    mmsq = stop(actual , mmsqq, n)
    uselo = stop(actual, usealoc, n)
    n = n + 1
    print (use)
    print (dia)
    print (bla)
    print (mmsq)
    print (blaf, n-1)
    print (useloc)



