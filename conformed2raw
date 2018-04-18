#!/bin/bash

# Simple wrapper for tkregister2 to get fsl .mat output
subj=$1
mri_dir=$1/mri

rawavg=$mri_dir/rawavg.mgz
orig=$mri_dir/orig.mgz

tkregister2 \
    --mov $orig \
    --targ $rawavg \
    --regheader \
    --fslregout $mri_dir/transforms/fs2anat.mat \
    --identity \
    --noedit \
    --reg register.dat

rm register.dat
