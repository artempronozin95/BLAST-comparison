#!/usr/bin/bash

ORT_GROUPS='./ortho_group.csv'
THR=25
RUN='./metric.sh'
cat $ORT_GROUPS | awk -F ',' '{print $1}' |parallel --verbose --colsep ' ' --jobs $THR $RUN

