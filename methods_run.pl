#!/usr/bin/perl -w

use config;
use Data::Dumper;
use Time::HiRes qw( time );
use strict;           
use warnings; 

my $q = $ARGV[0];
my $dbw = $ARGV[1];
my $ublast = $ARGV[2];
my $local = $ARGV[3];
#my $mms = $ARGV[4];
my $file = (split '/', $q)[-1];

#BLast
my $query = $cfg->{'methods'}->{'blast1'}->{'query'};
my $db = $cfg->{'methods'}->{'blast1'}->{'db'};
my $param = $cfg->{'methods'}->{'blast1'}->{'param'};
my $base = $cfg->{'methods'}->{'blast1'}->{'param_base'};
my $out = $cfg->{'methods'}->{'blast1'}->{'out'};
open (FL, '+>' , "$file.param.csv") || die $!;
print FL  $cfg->{'methods'}->{'blast1'}->{'bin'}, "\t";
print FL $cfg->{'methods'}->{'blast1'}->{'param_base'},"\n";
system("time -p -o $file.timeB.csv blastp $query $q $db $dbw $base $out ./metout/$file.Blast.outfmt6");

#BLast_fast
my $querybf = $cfg->{'methods'}->{'blastFast'}->{'query'};
my $dbbf = $cfg->{'methods'}->{'blastFast'}->{'db'};
my $parambf = $cfg->{'methods'}->{'blastFast'}->{'param'};
my $basebf = $cfg->{'methods'}->{'blastFast'}->{'param_base'};
my $outbf = $cfg->{'methods'}->{'blastFast'}->{'out'};
open (FL, '+>' , "$file.param.csv") || die $!;
print FL  $cfg->{'methods'}->{'blastFast'}->{'bin'}, "\t";
print FL $cfg->{'methods'}->{'blastFast'}->{'param_base'},"\n";
system("time -p -o $file.timeBF.csv blastp -task blastp-fast $querybf $q $dbbf $dbw $basebf $outbf ./metout/$file.BlastFast.outfmt6");

#DIAmond
my $diaquery = $cfg->{'methods'}->{'diamond'}->{'query'};
my $diadb = $cfg->{'methods'}->{'diamond'}->{'db'};
my $diaparam = $cfg->{'methods'}->{'diamond'}->{'param2'};
print FL $cfg->{'methods'}->{'diamond'}->{'bin'}, "\t";
print FL $cfg->{'methods'}->{'diamond'}->{'param2'},"\n";
system("time -p -o $file.timeD.csv diamond blastp $diaquery $q  $diadb $dbw $diaparam -a ./metout/$file.Dia.daa");
system("diamond view -a ./metout/$file.Dia.daa -o ./metout/$file.Dia.outfmt6");

#usearch
my $usequery = $cfg->{'methods'}->{'usearch'}->{'ublast'};
my $usedb = $cfg->{'methods'}->{'usearch'}->{'db'};
my $useparam = $cfg->{'methods'}->{'usearch'}->{'param'};
my $usebase = $cfg->{'methods'}->{'usearch'}->{'param_base'};
my $useout = $cfg->{'methods'}->{'usearch'}->{'out'};
print FL $cfg->{'methods'}->{'usearch'}->{'bin'}, "\t";
print FL $cfg->{'methods'}->{'usearch'}->{'param_base'},"\n";
system("time -p -o $file.timeU.csv usearch11.0.667_i86linux64 $usequery $q $usedb $ublast $usebase $useout ./metout/$file.use.outfmt6");

#use_local
my $usequeryl = $cfg->{'methods'}->{'use_local'}->{'usearch'};
my $usedbl = $cfg->{'methods'}->{'use_local'}->{'db'};
my $useparaml = $cfg->{'methods'}->{'use_local'}->{'param'};
my $usebasel = $cfg->{'methods'}->{'use_local'}->{'param_base'};
my $useoutl = $cfg->{'methods'}->{'use_local'}->{'out'};
print FL $cfg->{'methods'}->{'use_local'}->{'bin'}, "\t";
print FL $cfg->{'methods'}->{'use_local'}->{'param'},"\n";
system("time -p -o $file.timeUL.csv usearch11.0.667_i86linux64 $usequeryl $q $usedbl $local $useparaml $useoutl ./metout/$file.useloc.outfmt6");

#mmseq2
#my $mmsequery = $cfg->{'methods'}->{'mmseq2'}->{'query'};
#my $mmseqform = $cfg->{'methods'}->{'mmseq2'}->{'blast'};
system("time -p -o $file.timeM.csv mmseqs search ./protein/$file.g ./library/All_libC.fasta.g --threads 10 ./metout/$file.mmseq.outfmt6 tmp");
system("mmseqs convertalis ./protein/$file.g ./library/All_libC.fasta.g ./metout/$file.mmseq.outfmt6 ./metout/$file.mmseqBla.tab");
