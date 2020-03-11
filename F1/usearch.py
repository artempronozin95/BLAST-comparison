import numpy as np
import pandas as pd
import ml_metrics as metrics
import sys
import os


file1 = sys.argv[1]
file2 = sys.argv[2]
n=1

#base = os.path.basename(file3)
#base = os.path.splitext(base)[0]
#prot, no = base.split("_", 1)

clustal = pd.read_csv(file2, sep='\t', header=None)
usearch = pd.read_csv(file1, sep='\t', header=None)

clustal.columns = ['id_orth', 'id_prot', 'persent']
usearch.columns = ['id_prot', 'id_orth', 'persent', '3', '4', '5', '6', '7', '8', '9', '10', '11']

id_orth_clust = clustal['id_orth']
id_orth_use = usearch['id_orth']

print ("USEARCH")
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


while n <= 100:
    actual = id_orth_clust.to_list()[:n]
    usee = id_orth_use.to_list()[:n]
    use = stop(actual, usee, n)
    n = n + 1
    print (use)
