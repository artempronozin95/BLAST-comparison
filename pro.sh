#!/usr/bin/bash

OUT_DIR='./tab' #saving folder
wget -O $OUT/$1.fasta http://rest.kegg.jp/get/ath:$1/aaseq # download gene sequence from KEGG

wget 'https://v100.orthodb.org/tab?query='$1'&level=2759&species=2759&universal=all' -O $OUT_DIR/$1.csv # download table with ortho group info
a=$(awk -F '\t' 'NR==2{print $1}' $OUT_DIR/$1.csv) # extracts second word from first column of table
b=$(awk -F '\t' '{print $6}' $OUT_DIR/$1.csv |tail -n +2|  wc -l)
c=$(grep $1 age.csv | awk -F ',' '{print $2"\t"$3}')
paste <(printf %s "$1") <(printf %s "$c") <(printf %s "$a") <(printf %s "$b") >> tab.csv # combines id gene and id ortho group
rm $OUT_DIR/$1.csv # remove tables
sed -n '/[^ ]\t[^ ]/p;'  Euk_ortho.csv >> Euk_orthClean.csv # remove gene id with gaps 
