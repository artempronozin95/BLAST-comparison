#!/usr/bin/bash

ORT_GROUPS='ortho_group.csv'
THR=13
RUN='./orto_db.sh'
OUT_DIR='./euk'

mkdir $OUT_DIR
cat $ORT_GROUPS | awk -F ',' '{print$1" "$2}' | parallel --verbose --colsep ' ' --jobs $THR "$RUN {2} > $OUT_DIR/{1}_Eukaryotal.fasta"


