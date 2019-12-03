#!/usr/bin/bash

THR=25
RUN='./test_cfg.pl'
RUN2='./id_database.pl'
ALL='/home/pronozinau/OrthoDB/mmseq/*'
#a=$(find /home/pronozinau/OrthoDB/Viridiplantaelevel -name "$1_*")
#a=$(find /home/pronozinau/OrthoDB/Eukaryotalevel -name "$1_*")
b=$(find /home/pronozinau/OrthoDB/protein/ -name "$1.fasta")
#$RUN2 $ALL $b
$RUN $b

#wc $1.fasta.Blast.outfmt6 >> $1.fasta.param.csv
#wc $1.fasta.Dia.outfmt6 >> $1.fasta.param.csv
#wc $1.fasta.use.outfmt6 >> $1.fasta.param.csv
wc $1.fasta.mmseqBla.tab >> $1.fasta.param.csv

for file in `ls *.fasta.timeB.csv *.fasta.timeD.csv *.fasta.timeU.csv *.fasta.timeM.csv`; do echo $file; cat $file; done > time_all.csv;
for file in `ls *.fasta.param.csv`; do echo $file; cat $file; done > param_all.csv;
