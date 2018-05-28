#!/usr/bin/env python 

import os
import sys
import numpy as np
import nibabel as nib


roi_list = sys.argv[1]
with open(roi_list) as f:
    rois = f.read().splitlines()

first = rois[0]
init = nib.load(first)
base = init.get_data()
print(f"Loaded {first} as a base")
for roi in rois[1:]:
    base += nib.load(roi).get_data()
    print(f"Added {roi}")

mask = (base > 0) + 0
mask = nib.Nifti1Image(mask, init.get_affine())
out_file = os.path.join(os.path.dirname(first), 'fullmask.nii.gz')
print(f"Saving as {out_file}")
nib.save(mask, out_file)
