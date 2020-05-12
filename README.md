# BLAST-comparison
Annotation of the protein sequences by homology search and GO term transfer from highly homologous sequences is an important task for current genome and transcriptome sequencing projects. However, large size of sequence databases make homologous sequence search difficult in reasonable time. There exist tools that apply fast and ultrafast database search algorithms to find sequence homologs. These tools usually apply various heuristics for fast determining possible sequence matches. This result in different results of these programs with respect to returned set of homologous sequences and their rankings. These differences may lead to differences in the sets of GO terms and lead to errors in query sequence function annotation. 
We compare performance of the highly homologous sequence detection by several fast search tools (BLASTP fast, Diamond, Usearch ublast, Usearch local, Mmseq2) applied for A.thaliana protein sequences represented in OrthoDB database. We compared their results with the sequence ranking obtained by ClustalW program for various number k of returned best hits. 
## 1 stage
+ Download *Arabidopsis thaliana* genes from KEGG, example: [http://rest.kegg.jp/get/ath:AT1G68120/aaseq] (**script protein_db.sh**).
+ **run_protein_db.sh** execute automatic run.
## 2 stage 
+ Script **orto_db.sh**, search id orthogroup taken from file with id gene and id orthogroup of this gene in odb10v0_OG2genes.tab (download from [https://www.orthodb.org/?page=filelist], contains unique identified genotypes), after finding the identifier of the orthogroup, selects all identifiers of the genes related to the selected orthogroup, next searches for selected gene sequences from the complete ortholog database odb10_all_fasta.tab.gz (as well as downloaded from [https://www.orthodb.org/?page=filelist]), uses the samtools faidx program.
+ **run_orto_db.sh** script performs automatic selection of orthogroup identifiers from the file (odb10v0_OG2genes.tab) and submits them to the **orto_db.sh** script.
## 3 stage
The formation of a common base for all orthogroups (uses the **combine.sh** script), due to the presence of similar sequences for some orthogroups, a duplication error occurs in the output file, this problem is fixed by the following line `awk '/ ^> / {if (id [$ 1] ++ = = 0) printing = 1; else printing = 0} {if (printing) print} 'filename.fasta`.
## 4 stage
+ clustalW pair alignment, script **clustalw.pl** execute pair aligment of proteine sequence with every single correspond orthogroup secuence. Scrips form temporary file with single proteine sequence and single sequence from ortho group, next clustalW use this file as output. (clustalW create documents with .dnd.)
+ **run_clustalw.sh** script, parallel obtaining the protein identifier from table 1, passes the findClust.sh script to the script.
+ **ClustalW.sh**, searching a file with an orthogroup of the corresponding protein identifiers, searching for found files using the **clustalw.pl** script, solves the problem with files with the .dnd extension (deletes).
+ **percentage_id.py**, becouse of ClustalW alignment algorithm use a fast approximate alignment method. A similarity score (percent identity) is calculated from each alignment between every pair of sequences . 
## 5 stage
BLAST, BLAST fast, Diamond, Usearch (local, ublast) and Mmseq2 alignment.
+ **config.pm**, contains run configurations for every programm BLAST, BLAST fast, Diamond, Usearch (local, ublast), Mmseq2.
+ **database_build.pl**, builds indexed databases which are necessary for BLAST, BLAST fasta, Diamond и Usearch (local, ublast), Mmseqs2 work.
+ **Methods.sh** , run id database building for A.thaliana database and for orthogroup database as well as run alignment for all programs.
## 6 stage
Statistics, the following metrics were used: APK, MAPK, F1 score.
APK, MAKP, F1 score: [https://towardsdatascience.com/choosing-the-right-metric-is-a-huge-issue-99ccbe73de61]
+ **MAPK scripts** provides statistics on the MAPK metric, uses the pandas, numpy, ml_metrics packages, input files are alignment results from the BLAST, BLAST fast, Diamond, Usearch (local, ublast), Mmseq2 and clustalW programs. The script selects the columns containing the gene id from each file, loads the given sample into the ml_metrics package, uses clustalW as the actual reference, and BLAST, BLAST fast, Diamond, Usearch (local, ublast), Mmseq2 as the studied one (predicted).
+ **F1 scripts** provides statistics on the F1 score metric, files of alignment results for the BLAST, BLAST fast, Diamond, Usearch (local, ublast), Mmseq2 and clustalW programs are input. The script selects the columns containing the gene identifiers from each file, calculates Precision (accuracy).
+ **run_metric.sh**, parallel obtaining of protein IDs, passes **metric.sh** to the script.
+ **metric.sh**, searches for a file with the orthogroup of the corresponding protein ID, transfers the found files to the MAPK or F1 scripts.
## 7 stage 
+ **GOfind.py** script, used to find GO term for "k" best hits of BLAST, BLAST fasta, Diamond и Usearch (local, ublast), Mmseqs2 and ClustalW. Task, find point when number of GO term stand on plato.
+ **termGO.py** script, finds GO terms for "k" best hits of BLAST, BLAST fasta, Diamond и Usearch (local, ublast), Mmseqs2 and ClustalW. For this GO terms set calculets F1 metric.
+ **termGO_sem.py** script, finds GO terms for "k" best hits of BLAST, BLAST fasta, Diamond и Usearch (local, ublast), Mmseqs2 and ClustalW. For this GO terms set calculets semantic similarity (SS) metric. To calculate SS metric we use goatools packcage ([https://github.com/tanghaibao/goatools/blob/master/notebooks/semantic_similarity.ipynb]).
Output file of termGO.py and termGO_sem.py consist computing data for every orthogroup, **mean.py** script calculate average for every "k".
+ **aver.py** script build graf.
