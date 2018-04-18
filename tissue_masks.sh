#!/bin/bash

subj=$1

for mask_opt in gm all-wm ventricles; do
  mri_binarize \
    --i $subj/mri/aparc+aseg.mgz \
    --${mask_opt} \
    --o $subj/mri/${mask_opt}.nii.gz
done

