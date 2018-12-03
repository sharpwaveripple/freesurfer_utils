#!/bin/bash

subj=$1

module load freesurfer

orig=$subj/mri/orig.mgz
parc=$subj/mri/aparc+aseg.mgz
aseg=$subj/mri/aseg.auto.mgz

if [ -e $parc ]; then
  freeview $orig $parc:colormap=lut:opacity=0.5
else
  echo "Aparc not found, loading aseg"
  freeview $orig $aseg:colormap=lut:opacity=0.5
fi

