#!/usr/bin/bash

THR=5
RUN1='./methods_run.pl'
metout='./metout'
LIB='./library/odb10_all_fasta.tab'
ublast='./library/odb10_all_fasta.tab.udb'
local='./library/odb10_all_fasta.tab.use.udb'
RUN2='./database_build.pl'
lib='./library'
ALL='./odb10_all_fasta.tab'
b='./Protein.fasta'

mkdir $lib
mkdir $metout

$RUN2 $ALL $b
$RUN1 $b $LIB $ublast $local

for file in `ls *.fasta.timeB.csv *.fasta.timeD.csv *.fasta.timeU.csv *.fasta.timeM.csv *.fasta.timeUL.csv *.fasta.timeBF.csv`; do echo $file; cat $file; done > time_all_maine.csv;
