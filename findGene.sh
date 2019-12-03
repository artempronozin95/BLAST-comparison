#!/usr/bin/bash

THR=25
RUN='python3 metric.py'
FOLD='/home/pronozinau/OrthoDB/old_gene'
RUN2='python3 mapk.py'
RUN5='python3 recall.py'

a=$(find $FOLD -name "$1.fasta.Blast.outfmt6")
b=$(find $FOLD -name "$1.fasta.Dia.outfmt6")
c=$(find $FOLD -name "$1_*.fasta.csv")
d=$(find $FOLD -name "$1.fasta.use.outfmt6")
e=$(find $FOLD -name "$1.fasta.BlastFast.outfmt6")
r=$(find $FOLD -name "$1.csv")
$RUN5 "$a" "$b" "$c" "$d" "$e" > $1_Pre.BlaFa.csv
$RUN2 $1_Pre.Bla.csv $1_Pre.Dia.csv $1_Pre.Use.csv $1_Pre.BlaFa.csv
