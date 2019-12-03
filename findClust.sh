#!/usr/bin/bash

THR=25
RUN='./clustalw.pl'
a=$(find /home/pronozinau/OrthoDB/Eukaryotalevel -name "$1_*")
b=$(find /home/pronozinau/OrthoDB/protein/ -name "$1*")
"$RUN" $b $a | sort -nrk 3 > $a.csv
rm *.dnd

