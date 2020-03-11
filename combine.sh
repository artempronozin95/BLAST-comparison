#!/usr/bin/bash

cat ./euk/*.fasta > ./All_lib.fasta
awk '/^>/ { if (id[$1]++ == 0) printing = 1; else printing = 0 } { if (printing) print }' ./All_lib.fasta > ./All_libC.fasta
rm ./euk/*.fasta

