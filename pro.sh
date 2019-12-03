#!/usr/bin/bash

OUT='./protein'
OUT_DIR='./tab'
wget -O $OUT/$1.fasta http://rest.kegg.jp/get/ath:$1/aaseq

wget 'https://v100.orthodb.org/tab?query='$1'&level=2759&species=2759&universal=all' -O $OUT_DIR/$1.csv
a=$(awk -F '\t' 'NR==2{print $1}' $OUT_DIR/$1.csv)
paste <(printf %s "$1") <(printf %s "$a") >> Euk_ortho.csv
rm $OUT_DIR/$1.csv
sed -n '/[^ ]\t[^ ]/p;'  Euk_ortho.csv >> Euk_orthClean.csv
