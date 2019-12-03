#!/usr/bin/bash

ORT_GROUPS='ortho_group.csv' # file with id gene and id ortho group of this gene
THR=1 # number of streams  
RUN='./pro.sh' # script that run automatically
OUT_DIR='./protein' # savig folder 

cat $ORT_GROUPS | awk -F ',' '{print $1}' | tail -n +2 | parallel --verbose --colsep ' ' --jobs $THR "$RUN {1}"

