#!/usr/bin/bash

ORT_GROUPS='./ortho_group.csv'
THR=1
RUN='./Methods.sh'

cat $ORT_GROUPS | awk -F ',' '{print $1}' |parallel --verbose --colsep ' ' --jobs $THR $RUN

