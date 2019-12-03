# BLAST-comparison-
BLAST comparison with faster programs, like BLAST, BLAST fast, Diamond, Usearch (local and ublast), Mmseq2.
Include seven stage
# 1 stage:
Download table from ortho db, this table consist of information about orthogroups:
https://v100.orthodb.org/tab?query=AT1G68120&level=2759&species=2759&universal=all.
Build file with id gene and id orthogroup of this gene (script pro.sh).
Download genes from KEGG, example: http://rest.kegg.jp/get/ath:AT1G68120/aaseq (script pro.sh).
Automatic run of pro.sh script with parallel processes, execute run_ortho2fasta.sh.
# 2 stage 
Script orto2fasta.sh, search id orthogroup taken from file with id gene and id orthogroup of this gene in odb10v0_OG2genes.tab (download from https://www.orthodb.org/?page=filelist, contains unique identified genotypes), after finding the identifier of the orthogroup, selects all identifiers of the genes related to the selected orthogroup, next searches for selected gene sequences from the complete ortholog database odb10_all_fasta.tab.gz (as well as downloaded from https://www.orthodb.org/?page=filelist), uses the samtools faidx program.
The run_orto2fasta.sh script performs automatic selection of orthogroup identifiers from the file () and submits them to the orto2fasta.sh script.
# 3 stage
The formation of a common base for all Eukaryot orthogroups (uses the combine.sh script), due to the presence of similar sequences for some orthogroups, a duplication error occurs in the output file, this problem is fixed by the following line awk '/ ^> / {if (id [$ 1] ++ = = 0) printing = 1; else printing = 0} {if (printing) print} 'filename.fasta.
# 4 stage
clustalW pair alignment, script clustalw.pl execute pair aligment of proteine sequence with every single correspond ortho group secuence. Scrips form temporary file with single proteine sequence and single sequence from ortho group, next clustalW use this file as output. (clustalW create documents with .dnd.
The run_clustalw.sh script, parallel obtaining the protein identifier from table 1, passes the findClust.sh script to the script.
findClust.sh, searching a file with an orthogroup of the corresponding protein identifiers, searching for found files using the clustalw.pl script, solves the problem with files with the .dnd extension (deletes).
