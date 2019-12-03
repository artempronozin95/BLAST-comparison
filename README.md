# BLAST-comparison-
BLAST comparison with faster programs, like BLAST, BLAST fast, Diamond, Usearch (local and ublast), Mmseq2.
Include seven stage
# 1 stage:
Download table from ortho db, this table consist of information about orthogroups:
https://v100.orthodb.org/tab?query=AT1G68120&level=2759&species=2759&universal=all
Build file with id gene and id orthogroup of this gene (script pro.sh)
Download genes from KEGG, example: http://rest.kegg.jp/get/ath:AT1G68120/aaseq (script pro.sh)
Automatic run of pro.sh script with parallel processes, execute run_ortho2fasta.sh
# 2 stage 
Script orto2fasta.sh, search id orthogroup
