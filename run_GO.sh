#!/usr/bin/bash

ORT_GROUPS='/home/pronozinau/OrthoDB/ortho_group.csv'
THR=25
RUN='./findGO.sh'
cat $ORT_GROUPS | awk -F ',' '{print $1}' |parallel --verbose --colsep ' ' --jobs $THR $RUN

