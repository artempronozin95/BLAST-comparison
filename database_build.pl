#!/usr/bin/perl -w

use config;
use Data::Dumper;

my $dbw = $ARGV[0];
my $q = $ARGV[1];
my $file = (split '/', $dbw)[-1];

#BLast
my $ortdb = $cfg->{'methods'}->{'makedb'}->{'in'};
my $typedb = $cfg->{'methods'}->{'makedb'}->{'db'};
system("makeblastdb $ortdb $dbw $typedb -out ./library/$file");

#DIAmond
my $diamdb = $cfg->{'methods'}->{'diamonddb'}->{'in'};
my $diaout = $cfg->{'methods'}->{'diamonddb'}->{'db'};
system("diamond makedb $diamdb $dbw $diaout ./library/$file.dmnd ");

#usearch
my $usemdb = $cfg->{'methods'}->{'usearchdb'}->{'db'};
system("usearch11.0.667_i86linux64 $usemdb $dbw -output ./library/$file.udb");

#use_local
my $usemdbl = $cfg->{'methods'}->{'use_localdb'}->{'db'};
system("usearch11.0.667_i86linux64 $usemdbl $dbw -output ./library/$file.use.udb");

#mmseq2
system("mmseqs createdb $dbw ./library/$file.g");
system("mmseqs createdb $q $q.g");


