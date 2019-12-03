#!/usr/bin/perl -w

use config;
use Data::Dumper;
use Time::HiRes qw( time );
use strict;           
use warnings; 

my $q = $ARGV[0];
#my $dbw = $ARGV[1];
#my $file = (split '/', $dbw)[-1];
my $file = (split '/', $q)[-1];

#BLast
#my $query = $cfg->{'methods'}->{'blast1'}->{'query'};
#my $db = $cfg->{'methods'}->{'blast1'}->{'db'};
#my $param = $cfg->{'methods'}->{'blast1'}->{'param'};
#my $ortdb = $cfg->{'methods'}->{'makedb'}->{'in'};
#my $typedb = $cfg->{'methods'}->{'makedb'}->{'db'};
#my $base = $cfg->{'methods'}->{'blast1'}->{'param_base'};
#my $out = $cfg->{'methods'}->{'blast1'}->{'out'};
#open (FL, '+>' , "$file.param.csv") || die $!;
#print FL  $cfg->{'methods'}->{'blast1'}->{'bin'}, "\t";
#print FL $cfg->{'methods'}->{'blast1'}->{'param_base'},"\n";
#system("time -p -o $file.timeB.csv  blastp $query $q $db $dbw $base $out $file.Blast.outfmt6");

#BLast_fast
#my $query = $cfg->{'methods'}->{'blast1'}->{'query'};
#my $db = $cfg->{'methods'}->{'blast1'}->{'db'};
#my $param = $cfg->{'methods'}->{'blast1'}->{'param'};
#my $ortdb = $cfg->{'methods'}->{'makedb'}->{'in'};
#my $typedb = $cfg->{'methods'}->{'makedb'}->{'db'};
#my $base = $cfg->{'methods'}->{'blast1'}->{'param_base'};
#my $out = $cfg->{'methods'}->{'blast1'}->{'out'};
#open (FL, '+>' , "$file.param.csv") || die $!;
#print FL  $cfg->{'methods'}->{'blast1'}->{'bin'}, "\t";
#print FL $cfg->{'methods'}->{'blast1'}->{'param_base'},"\n";
#system("time -p -o $file.timeBF.csv blastp -task blastp-fast $query $q $db $dbw $base $out $file.BlastFast.outfmt6");

#DIAmond
#my $diaquery = $cfg->{'methods'}->{'diamond'}->{'query'};
#my $diadb = $cfg->{'methods'}->{'diamond'}->{'db'};
#my $diaparam = $cfg->{'methods'}->{'diamond'}->{'param2'};
#my $diamdb = $cfg->{'methods'}->{'diamonddb'}->{'in'};
#my $diaout = $cfg->{'methods'}->{'diamonddb'}->{'db'};
#print FL $cfg->{'methods'}->{'diamond'}->{'bin'}, "\t";
#print FL $cfg->{'methods'}->{'diamond'}->{'param2'},"\n";
#system("diamond makedb $diamdb $dbw $diaout $file.dmnd ");
#system("time -p -o $file.timeD.csv diamond blastp $diaquery $q  $diadb $dbw $diaparam -a $file.Dia.daa");
#system("diamond view -a $file.Dia.daa -o $file.Dia.outfmt6");

#usearch
#my $usequery = $cfg->{'methods'}->{'usearch'}->{'ublast'};
#my $usedb = $cfg->{'methods'}->{'usearch'}->{'db'};
#my $useparam = $cfg->{'methods'}->{'usearch'}->{'param'};
#my $usemdb = $cfg->{'methods'}->{'usearchdb'}->{'db'};
#my $usebase = $cfg->{'methods'}->{'usearch'}->{'param_base'};
#my $useout = $cfg->{'methods'}->{'usearch'}->{'out'};
#print FL $cfg->{'methods'}->{'usearch'}->{'bin'}, "\t";
#print FL $cfg->{'methods'}->{'usearch'}->{'param_base'},"\n";
#system("/sf/smpdata1/pronozinau/usearch/usearch11.0.667_i86linux64 $usemdb $dbw -output $file.udb");
#system("time -p -o $file.timeU.csv /sf/smpdata1/pronozinau/usearch/usearch11.0.667_i86linux64 $usequery $q $usedb $dbw $usebase $useout $file.use.outfmt6");

#mmseq2
#my $mmsequery = $cfg->{'methods'}->{'mmseq2'}->{'query'};
#my $mmseqform = $cfg->{'methods'}->{'mmseq2'}->{'blast'};
system("time -p -o $file.timeM.csv mmseqs search $q /home/pronozinau/OrthoDB/mmseq/All_euk $file.mmseq.outfmt6 tmp");
system("mmseqs convertalis $q /home/pronozinau/OrthoDB/mmseq/All_euk $file.mmseq.outfmt6 $file.mmseqBla.tab");