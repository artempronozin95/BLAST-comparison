#!/usr/bin/bash

THR=25
RUN='python3 metric.py'
FOLD='./metout'
RUN2='python3 aver.py'
RUN3='python3 mean.py'
RUN4='python3 TP_FP.py'
RUN5='python3 recall.py'
OUT='./Methods'
Pre='./Pre'
F1='./F1'

mkdir $OUT
mkdir $Pre

a=$(find $FOLD -name "$1.fasta.Blast.outfmt6")
b=$(find $FOLD -name "$1.fasta.Dia.outfmt6")
c=$(find ./clust -name "$1.csv")
d=$(find $FOLD -name "$1.fasta.use.outfmt6")
e=$(find $FOLD -name "$1.fasta.BlastFast.outfmt6")
f=$(find $FOLD -name "$1.fasta.mmseqBla.tab")
g=$(find $FOLD -name "$1.fasta.useloc.outfmt6")
python3 $F1/blast.py "$a" "$c" > $OUT/$1_Pre.Bla.csv
python3 $F1/diam.py "$b" "$c" > $OUT/$1_Pre.Dia.csv
python3 $F1/usearch.py "$d" "$c" > $OUT/$1_Pre.Use.csv
python3 $F1/mmseq2.py "$f" "$c" > $OUT/$1_Pre.Mmseq.csv
python3 $F1/uselocal.py "$g" "$c" > $OUT/$1_Pre.UseLoc.csv
python3 $F1/blastfast.py "$e" "$c" > $OUT/$1_Pre.BlastF.csv
$RUN2 $OUT/$1_Pre.Bla.csv $OUT/$1_Pre.Dia.csv $OUT/$1_Pre.Use.csv $OUT/$1_Pre.BlastF.csv $OUT/$1_Pre.Mmseq.csv $OUT/$1_Pre.UseLoc.csv
mv $1.csv Pre/
