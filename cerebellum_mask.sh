#!/bin/bash

# INPUT: Freesurfer subject dir
# OUTPUT: Whole cerebellum mask in mri/

# Todo: make RH or LH selectable

subj=$1
mri_dir=$subj/mri

mri_binarize \
  --i $mri_dir/aseg.mgz \
  --o $mri_dir/cerebellum.nii.gz \
  --match 6 7 8 45 46 47

# first 3 are left, second 3 are right
