#!/bin/bash

# INPUT: Freesurfer subject dir
# INPUT2: Output transformation matrix name
# OUTPUT: Conformed to raw anat transform in mri/transforms/fs2anat.mat

# Uses tkregister2 to register orig to rawavg using header info 

subj=$1
out_xfm=$2

echo "Subject is $subj"

mri_dir=$1/mri

rawavg=$mri_dir/rawavg.mgz
orig=$mri_dir/orig.mgz

echo "Registering $orig to $rawavg..."

tkregister2 \
    --mov $orig \
    --targ $rawavg \
    --regheader \
    --fslregout $out_xfm \
    --identity \
    --noedit \
    --reg register.dat

echo "Saved $out_xfm"
rm register.dat
