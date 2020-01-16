#!/usr/bin/bash

cat *.fasta > test.fasta # combine all data bases in one
grep '^>' AllAge.fasta | sort | uniq -c > test.csv # check on duplication of headers in fasta file
awk '/^>/ { if (id[$1]++ == 0) printing = 1; else printing = 0 } { if (printing) print }' test.fasta > new.fasta #filter duplicatication sequenses

