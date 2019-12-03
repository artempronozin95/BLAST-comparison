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
# 5 stage
BLAST, BLAST fast, Diamond, Usearch (local, ublast) and Mmseq2 alignment.
config.pm, contains run configurations for every programm BLAST, BLAST fast, Diamond, Usearch (local, ublast), Mmseq2.
id database.pl, builds indexed databases which are necessary for BLAST, BLAST fasta, Diamond и Usearch (local, ublast), Mmseqs2 work.
test_cfg.pl, executes alignment of proteine sequence against  ortho groups whole database with aplication BLAST, BLAST fasta, Diamond and Usearch (local, ublast), Mmseqs2 methods. Parameters take from config.pm script.
run_blast.sh, parallel obtaining of the protein identifier from table 1, passes find.sh to the script.
a database file of all Eukaryot orthogroups, as well as test_cfg.pl protein sequence and an indexed database of all Eukaryot orthogroups. Generates a common file.
rm.sh, forms as a result of the work of the Diamond program).
# 6 stage
Statistics, the following metrics were used: APK, MAPK, F1 score.
APK, MAKP, F1 score: https://towardsdatascience.com/choosing-the-right-metric-is-a-huge-issue-99ccbe73de61
The metric.py script provides statistics on the APK metric, uses the pandas, numpy, ml_metrics packages, input files are alignment results from the BLAST, BLAST fast, Diamond, Usearch (local, ublast), Mmseq2 and clustalW programs. The script selects the columns containing the gene id from each file, loads the given sample into the ml_metrics package, uses clustalW as the actual reference, and BLAST, BLAST fast, Diamond, Usearch (local, ublast), Mmseq2 as the studied one (predicted).

The aver.py script provides statistics on the MAPK metric, uses the pandas, numpy, ml_metrics packages, input files are alignment results from the BLAST, BLAST fast, Diamond, Usearch (local, ublast), Mmseq2 and clustalW programs. The script selects the columns containing the gene id from each file, loads the given sample into the ml_metrics package, uses clustalW as the actual reference, and BLAST, BLAST fast, Diamond, Usearch (local, ublast), Mmseq2 as the studied one (predicted).

The recall.py script provides statistics on the F1 score metric, files of alignment results for the BLAST, BLAST fast, Diamond, Usearch (local, ublast), Mmseq2 and clustalW programs are input. The script selects the columns containing the gene identifiers from each file, calculates Precision (accuracy) and Recall (completeness) using the created functions, and calculates the F1 score metric based on the received data. At the output we get 3 charts Precision, Recall, F1 score.

run_Gene.sh, parallel obtaining of protein IDs from table 1, passes findGene.sh to the script.
findGene.sh, searches for a file with the orthogroup of the corresponding protein ID, transfers the found files to the recall.py, aver.py, metric.py script.
