#!/bin/bash

subj=$1

module load freesurfer

orig=$subj/mri/orig.mgz
parc=$subj/mri/aparc+aseg.mgz
freeview $orig $parc:colormap=lut:opacity=0.5
