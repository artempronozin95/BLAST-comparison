#!/usr/bin/bash

#ORT_GROUPS='ortho_group.csv'
#THR=13
#RUN='./orto2fasta.sh'
#OUT_DIR='./tmp'

#cat $ORT_GROUPS | awk -F ',' '{print $1" "$2}' | tail -n +2 |  parallel --verbose --colsep ' ' --jobs $THR "$RUN {2} > $OUT_DIR/{1}_{2}_Viridiplantae.fasta"
#cat $ORT_GROUPS | awk -F ',' '{print $1" "$3}' | tail -n +2 | parallel --verbose --colsep ' ' --jobs $THR "$RUN {2} > $OUT_DIR/{1}_{2}_Eukaryotal.fasta"

ORT_GROUPS='ortho_group.csv'
THR=1
RUN='./pro.sh'
OUT_DIR='./protein'

cat $ORT_GROUPS | awk -F ',' '{print $1}' | tail -n +2 | parallel --verbose --colsep ' ' --jobs $THR "$RUN {1}"
#> $OUT_DIR/{1}.fasta" 
