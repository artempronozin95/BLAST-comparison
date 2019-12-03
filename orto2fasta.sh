#!/usr/bin/bash

a=$(zcat odb10v0_OG2genes.tab.gz | grep $1 | awk '{print $2}')
/storage/progs/samtools-1.7/samtools faidx  odb10_all_fasta.tab.gz $a
