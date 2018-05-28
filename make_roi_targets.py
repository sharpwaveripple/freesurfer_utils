#!/usr/bin/env python 

import os
import sys
import numpy as np
import nibabel as nib


def get_basename(fpath):
    base = os.path.basename(fpath)
    first = os.path.splitext(base)[0]
    second = os.path.splitext(first)[0]
    return second

def save_voxel_counts(roi_data, roi_names, outfile):
    voxels = [str(np.count_nonzero(x)) for x in roi_data]
    voxel_counts = [x + ',' + y for x, y in zip(roi_names, voxels)]
    voxel_counts = '\n'.join(voxel_counts)
    with open(outfile, 'w+') as f:
        f.write(voxel_counts)
        f.write('\n')
    print(f"Saved voxel counts to {outfile}")


roi_list = sys.argv[1]

with open(roi_list) as f:
    rois = f.read().splitlines()

roi_names = [get_basename(x) for x in rois]
aff = nib.load(rois[0]).get_affine()
data = [nib.load(x).get_data() for x in rois]
print("Loaded all roi data")
work_dir = os.path.dirname(rois[0])
save_voxel_counts(data, roi_names, os.path.join(work_dir, 'voxel_counts.csv'))
base = np.zeros(data[0].shape)
for roi in data:
    base += roi

fullmask = (base > 0).astype(int)

for name, roi in zip(roi_names, data):
    target = fullmask - roi
    target_img = nib.Nifti1Image(target, aff)
    target_name = os.path.join(work_dir, name + '_target.nii.gz')
    nib.save(target_img, target_name)
    print(f"Saved {target_name}")

# for roi in rois:
#     target = fullmask - nib.load(roi).get_data()
#     target_name = os.path.join(os.path.dirname(first), get_basename(roi) + '_target.nii.gz')
#     target_mask = nib.Nifti1Image(target, aff)
#     nib.save(target_mask, target_name)

# fullmask = nib.Nifti1Image(mask, init.get_affine())
# out_file = os.path.join(os.path.dirname(first), 'fullmask.nii.gz')
# print(f"Saving as {out_file}")
# nib.save(mask, out_file)
