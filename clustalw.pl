#!/usr/bin/perl -w

use strict;
use Bio::SeqIO;
use File::Temp qw/ tempfile /;

my $prot_file = $ARGV[0] || die "input prot fasta file not find\n";
my $orto_file = $ARGV[1] || die "input prot fasta file not find\n";

my $prot   = Bio::SeqIO->new(-file => $prot_file, -format  => "fasta")->next_seq;
my $ortoio = Bio::SeqIO->new(-file => $orto_file, -format  => "fasta"); 

while (my $seq = $ortoio->next_seq) {
  my ($fh, $tmp) = tempfile( DIR => ".", UNLINK => 1 );
  print $fh
              ">",$prot->id,"\n",
              $prot->seq,"\n",
              ">",$seq->id,"\n",
              $seq->seq,"\n";
my $id = print $seq->id, "\t";
my $cmd = "clustalw -MATRIX=BLOSUM -INFILE=$tmp -ALIGN -OUTFILE=/dev/null";
open F, "$cmd |" || die $!;
my ($s1,$s2,$s);
while (<F>) {
    $s1 = $1 if /Sequence 1: (.+?) /;
    $s2 = $id;
#    $s2 = $1 if /Sequence 2: (.+?) /;
    $s  = $1 if /Sequences \(1:2\) Aligned. Score:\s*(\d+)/;
 }
close F;
print "$s1\t$s\n";
close $fh;
}


__END__
Sequence format is Pearson
Sequence 1: 981085_0_003db1   109 aa
Sequence 2: ath_AT2G41840     285 aa
Start of Pairwise alignments
Aligning...

Sequences (1:2) Aligned. Score:  73
Guide tree file created:   [prot_ort.dnd]

There are 1 groups
Start of Multiple Alignment

Aligning...
Group 1: Sequences:   2      Score:1558
Alignment Score 438
