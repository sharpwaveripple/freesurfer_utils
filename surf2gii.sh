#!/bin/bash

subj=$1

surfdir=$subj/surf

for surf in pial white; do
  mris_convert \
    --combinesurfs $surfdir/lh.${surf} $surfdir/rh.${surf} $surfdir/$surf.gii
done
