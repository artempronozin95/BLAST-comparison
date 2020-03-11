#!/usr/bin/bash

./run_protein_db.sh
./run_orto_db.sh
./run_clustalw.sh
./combine.sh
./run_blast.sh
./rm.sh
./run_metric.sh