#!/bin/bash

# INPUT: Freesurfer subject dir
# OUTPUT: Conformed to raw anat transform in mri/transforms/fs2anat.mat

# Uses tkregister2 to register orig to rawavg using header info 

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
