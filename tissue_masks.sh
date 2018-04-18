#!/bin/bash

subj=$1
mri_dir=$1/mri


for mask_opt in gm all-wm ventricles; do
  mri_binarize \
    --i $mri_dir/aparc+aseg.mgz \
    --${mask_opt} \
    --o $mri_dir/${mask_opt}.nii.gz
done

