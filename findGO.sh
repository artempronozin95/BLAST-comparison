#!/usr/bin/bash

ORT='/home/pronozinau/OrthoDB/odb10v0_gene_xrefs_onlyGO.tab'
THR=25
RUN='python3 column.py'
FOLD='/home/pronozinau/OrthoDB/Eukaryotalevel'
a=$(find $FOLD -name "$1_*")
$RUN $ORT "$a" > "$a"_GO.csv

