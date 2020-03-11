#!/usr/bin/bash

OUT='./protein'
OUT_DIR='./tab'
mkdir $OUT
wget -O $OUT/$1.fasta http://rest.kegg.jp/get/ath:$1/aaseq

