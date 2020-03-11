#!/usr/bin/bash


ORT_GROUPS='ortho_group.csv'
THR=1
RUN='./protein_db.sh'
OUT_DIR='./protein'

cat $ORT_GROUPS | awk -F ',' '{print $1}' | parallel --verbose --colsep ' ' --jobs $THR "$RUN {1}"

