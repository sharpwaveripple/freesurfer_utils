#!/bin/bash

subj=$1

module load freesurfer

orig=$subj/mri/orig.mgz
parc=$subj/mri/aparc+aseg.mgz
aseg=$subj/mri/aseg.auto.mgz
brainmask=$subj/mri/brainmask.mgz

if [ -e $parc ]; then
  freeview $orig $parc:colormap=lut:opacity=0.5
elif [ -e $aseg ]; then
  echo "Aparc not found"
  freeview $orig $aseg:colormap=lut:opacity=0.5
else 
  echo "Aseg not found"
  freeview $orig $brainmask
fi

