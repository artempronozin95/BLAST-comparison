#!/usr/bin/bash

THR=25
RUN='./test_cfg.pl'
RUN2='./id_database.pl'
ALL='/home/pronozinau/OrthoDB/mmseq/All_euk.fasta'

b=$(find /home/pronozinau/OrthoDB/protein/ -name "$1.fasta") #searching protein
$RUN2 $ALL $b #run id_database.pl
$RUN $b #run test_cfg.pl

wc $1.fasta.Blast.outfmt6 >> $1.fasta.param.csv #form file with input parameters
wc $1.fasta.Dia.outfmt6 >> $1.fasta.param.csv
wc $1.fasta.use.outfmt6 >> $1.fasta.param.csv
wc $1.fasta.mmseqBla.tab >> $1.fasta.param.csv
wc $1.fasta.uselocal.outfmt6 >> $1.fasta.param.csv

for file in `ls *.fasta.timeB.csv *.fasta.timeD.csv *.fasta.timeU.csv *.fasta.timeM.csv *.fasta.timeUL.csv`; do echo $file; cat $file; done > time_all.csv;
for file in `ls *.fasta.param.csv`; do echo $file; cat $file; done > param_all.csv;
