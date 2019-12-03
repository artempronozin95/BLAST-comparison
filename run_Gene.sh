#!/usr/bin/bash

ORT_GROUPS='/home/pronozinau/OrthoDB/old_gene/old.csv'
THR=25
RUN='./findGene.sh'
cat $ORT_GROUPS | awk -F ',' '{print $1}' |parallel --verbose --colsep ' ' --jobs $THR $RUN

