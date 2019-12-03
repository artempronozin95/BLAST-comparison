#!/usr/bin/perl -w

use config;
use Data::Dumper;
use Time::HiRes qw( time );

my $dbw = $ARGV[0];
my $q = $ARGV[1];
my $file = (split '/', $dbw)[-1];

#BLast
#my $query = $cfg->{'methods'}->{'blast1'}->{'query'};
#my $db = $cfg->{'methods'}->{'blast1'}->{'db'};
#my $param = $cfg->{'methods'}->{'blast1'}->{'param'};
#my $ortdb = $cfg->{'methods'}->{'makedb'}->{'in'};
#my $typedb = $cfg->{'methods'}->{'makedb'}->{'db'};
#my $base = $cfg->{'methods'}->{'blast1'}->{'param_base'};
#my $out = $cfg->{'methods'}->{'blast1'}->{'out'};
#system("makeblastdb $ortdb $dbw $typedb");

#DIAmond
#my $diaquery = $cfg->{'methods'}->{'diamond'}->{'query'};
#my $diadb = $cfg->{'methods'}->{'diamond'}->{'db'};
#my $diaparam = $cfg->{'methods'}->{'diamond'}->{'param2'};
#my $diamdb = $cfg->{'methods'}->{'diamonddb'}->{'in'};
#my $diaout = $cfg->{'methods'}->{'diamonddb'}->{'db'};
#system("diamond makedb $diamdb $dbw $diaout $file.dmnd ");

#usearch
#my $usequery = $cfg->{'methods'}->{'usearch'}->{'ublast'};
#my $usedb = $cfg->{'methods'}->{'usearch'}->{'db'};
#my $useparam = $cfg->{'methods'}->{'usearch'}->{'param'};
#my $usemdb = $cfg->{'methods'}->{'usearchdb'}->{'db'};
#my $usebase = $cfg->{'methods'}->{'usearch'}->{'param_base'};
#my $useout = $cfg->{'methods'}->{'usearch'}->{'out'};
#system("/sf/smpdata1/pronozinau/usearch/usearch11.0.667_i86linux64 $usemdb $dbw -output $file.udb");

#mmseq2
my $mmseqdb = $cfg->{'methods'}->{'mmseqdb'}->{'db'};
system("mmseqs createdb $dbw $dbw");
system("mmseqs createdb $q $q");

#open (FL, "+>" , $f) || die "Can't open c.csv $!";
#print FL $cfg->{'methods'}->{'usearch'}->{'bin'}, "\t";
#print $cfg->{'methods'}->{'usearch'}->{'param_base'},"\n";
#close FL;
