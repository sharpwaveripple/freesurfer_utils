#!/bin/bash

# INPUT: Freesurfer subject dir
# OUTPUT: Binary masks for grey matter, white matter, and ventricles in mri/

subj=$1
mri_dir=$subj/mri

for mask_opt in gm all-wm ventricles; do
  mri_binarize \
    --i $mri_dir/aparc+aseg.mgz \
    --${mask_opt} \
    --o $mri_dir/${mask_opt}.nii.gz
done

