#!/bin/bash

# export SUBJECTS_DIR=/home/sharpwaveripple/ukb/fs
# export SUBJECTS_DIR=/home/sharpwaveripple
# SUBJECT=001_2006

subj=$1
fsdir=$(dirname "$1")
fsdir=$(readlink -f $fsdir)
mri_dir=$fsdir/$subj/mri

for surf in pial white; do
  for hemi in lh rh; do
    mri_surf2vol \
      --mkmask \
      --hemi ${hemi} \
      --surf ${surf} \
      --identity $subj \
      --template $mri_dir/orig.mgz \
      --o $mri_dir/${hemi}_${surf}.nii.gz \
      --sd $fsdir
  done
  fslmaths $mri_dir/lh_${surf}.nii.gz \
    -add $mri_dir/rh_${surf}.nii.gz -bin \
    $mri_dir/${surf}_surf.nii.gz
  rm $mri_dir/lh_${surf}.nii.gz $mri_dir/rh_${surf}.nii.gz  
done
