#!/bin/bash

subj=$1
T1=$2
mri_dir=$1/mri
xfm=$mri_dir/transforms/fs2anat.mat 

if [ ! -f $xfm ]; then
  echo "$xfm not found!"
  exit 1
else
  for tissue in gm all-wm ventricles; do
    tissue_file=$mri_dir/${tissue}.nii.gz
    flirt \
      -datatype double \
      -interp nearestneighbour \
      -v \
      -in $tissue_file \
      -ref $T1 \
      -applyxfm \
      -init $xfm \
      -out $mri_dir/${tissue}_T1.nii.gz
  done
fi
