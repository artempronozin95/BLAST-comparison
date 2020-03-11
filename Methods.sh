#!/usr/bin/bash

THR=5
RUN1='./methods_run.pl'
metout='./metout'
LIB='./library/All_libC.fasta'
ublast='./library/All_libC.fasta.udb'
local='./library/All_libC.fasta.use.udb'
RUN2='./database_build.pl'
lib='./library'
ALL='./All_libC.fasta'

mkdir $lib
mkdir $metout

b=$(find ./protein -name "$1.fasta")

$RUN2 $ALL $b
$RUN1 $b $LIB $ublast $local

for file in `ls *.fasta.timeB.csv *.fasta.timeD.csv *.fasta.timeU.csv *.fasta.timeM.csv *.fasta.timeUL.csv *.fasta.timeBF.csv`; do echo $file; cat $file; done > time_all_maine.csv;
