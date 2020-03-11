#!/usr/bin/bash


RUN='./clustalw.pl'
OUT='./clust'
mkdir $OUT
a=$(find ./euk -name "$1_*")
b=$(find ./protein -name "$1*")
$RUN $b $a | sort -nrk 3 > $OUT/$1.csv
rm *.dnd


