#!/usr/bin/perl -w

use config;
use Data::Dumper;
use Time::HiRes qw( time );

my $dbw = $ARGV[0];
my $q = $ARGV[1];
my $file = (split '/', $dbw)[-1];

#BLast
my $ortdb = $cfg->{'methods'}->{'makedb'}->{'in'};
my $typedb = $cfg->{'methods'}->{'makedb'}->{'db'};
system("makeblastdb $ortdb $dbw $typedb");

#DIAmond
my $diamdb = $cfg->{'methods'}->{'diamonddb'}->{'in'};
my $diaout = $cfg->{'methods'}->{'diamonddb'}->{'db'};
system("diamond makedb $diamdb $dbw $diaout $file.dmnd ");

#usearch
my $usemdb = $cfg->{'methods'}->{'usearchdb'}->{'db'};
system("/sf/smpdata1/pronozinau/usearch/usearch11.0.667_i86linux64 $usemdb $dbw -output $file.udb");

#use_local
my $usemdb = $cfg->{'methods'}->{'use_localdb'}->{'db'};
system("/sf/smpdata1/pronozinau/usearch/usearch11.0.667_i86linux64 $usemdb $dbw -output $file.use.udb");

#mmseq2
my $mmseqdb = $cfg->{'methods'}->{'mmseqdb'}->{'db'};
system("mmseqs createdb $dbw $dbw");
system("mmseqs createdb $q $q");

#open (FL, "+>" , $f) || die "Can't open c.csv $!";
#print FL $cfg->{'methods'}->{'usearch'}->{'bin'}, "\t";
#print $cfg->{'methods'}->{'usearch'}->{'param_base'},"\n";
#close FL;
