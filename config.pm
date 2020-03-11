#!/usr/bin/perl

use strict; use warnings;
package config;

BEGIN {

use Exporter ();
use vars qw($VERSION @ISA @EXPORT @EXPORT_OK %EXPORT_TAGS);

# set the version for version checking
$VERSION= 1.0;
@ISA= qw(Exporter);

# your exported functions go here
@EXPORT= qw( $cfg &config );
%EXPORT_TAGS= ();

# your exported package globals go here,
# as well as any optionally exported functions
@EXPORT_OK= qw( $cfg );
}

use vars @EXPORT_OK;

 #
 # Init package globals
 #
$cfg = {
  methods => {
    blast1 => {
      bin => 'blastp',
      query => '-query',
      db => '-db',
      param => '-outfmt 6 -max_target_seqs 10 -max_hsps 1 -evalue 1e-5',
      param_base => '-evalue 1e-3 -outfmt 6 -num_threads 10',
      out => '-out',
         },
    blastFast => {
      bin => 'blastp_fast',
      query => '-query',
      db => '-db',
      param => '-outfmt 6 -max_target_seqs 10 -max_hsps 1 -evalue 1e-5',
      param_base => '-evalue 1e-3 -outfmt 6 -num_threads 10',
      out => '-out',
         },
    makedb => {
      bin => 'makeblastdb',
      in => '-in',
      db => '-dbtype prot -parse_seqids -blastdb_version 5',
         },
    diamond => {
      bin => 'diamond',
      db => '-d',
      query => '-q',
      param => '-e 1e-5 -k 10 --sensitive',
      param1 => '-e 1e-5 -k 10 --more-sensitive',
      param2 => '-e 1e-3 --threads 10',
      out => '-a',
         },
    diamonddb => {
      bin => 'makedb',
      db => '-d',
      in => '--in',
         },
    usearch => {
      bin => 'usearch11',
      ublast => '-ublast',
      db => '-db',
      param => '-evalue 1e-5 -accel 0.5 -maxhits 10 -threads 10',
      param_base => '-evalue 1e-3 -threads 10',
      out => '-blast6out',
         },
    usearchdb => {
      bin => 'usearch11',
      db => '-makeudb_ublast',
      out => '-output',
         },
    use_local => {
      bin => 'usearch11',
      usearch => '-usearch_local',
      db => '-db',
      param => '-evalue 1e-3 -id 0.5 -maxaccepts 1000 -threads 10',
      param_base => '-evalue 1e-3 -threads 10',
      out => '-blast6out',
         },
    use_localdb => {
      bin => 'usearch11',
      db => '-makeudb_usearch',
      out => '-output',
         },
    mmseqdb => {
      bin => 'mmseq2db',
      db => 'createdb',
         },
    mmseq => { 
      bin => 'mmseq2',
      query => 'search',
      blast => 'convertalis',
         },
  },
};


#### sub ####
sub config() {

return $cfg->{$_[0]};

} #### config()


END { }


return 1;


__END__
