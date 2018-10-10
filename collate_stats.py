import os
import sys
from collections import defaultdict
import pandas as pd

def ls_sub_dir(sub_dir):
    dir_contents = sorted(os.listdir(sub_dir))
    if "fsaverage" in dir_contents:
        dir_contents.remove("fsaverage")
    return dir_contents

def general_measures(hash_lines, hemi, results):
    measures = [i.split(', ') for i in hash_lines if 'Measure' in i]
    for stat in measures:
        clean_name = stat[1].replace(" ", "_")
        key = '_'.join([hemi, clean_name])
        val = stat[-2]
        results[key].append(val)
    return results

def areal_measures(hash_lines, unhashed_lines, hemi, results):
    headers = hash_lines[-1].split()[3:]
    struct = [i[0] for i in unhashed_lines]
    stats = [i[1:] for i in unhashed_lines]
    for i, j in zip(struct, stats):
        for k, val in zip(headers, j):
            key = '_'.join([hemi, i, k])
            results[key].append(val)
    return results

def read_stats(stats_file, hemi, results):
    commented = []
    uncommented = []
    with open(stats_file) as f:
        for line in f:
            if line.startswith('#'):
                commented.append(line.rstrip())
            else:
                uncommented.append(line.rstrip().split())
    results = general_measures(commented, hemi, results)
    results = areal_measures(commented, uncommented, hemi, results)
    return results

subjects_dir = os.path.abspath(sys.argv[1])
subjects = ls_sub_dir(subjects_dir)

parc_list = ['aparc.stats', 'aparc.a2009s.stats', 'aparc.DKTatlas.stats']

for parc in parc_list:
    results = defaultdict(list)
    failed_subj = []
    for sub in subjects:
        print("Reading {} data... ".format(sub), end='')
        try:
            for hemi in ['lh', 'rh']:
                stats_fname = '.'.join([hemi, parc])
                stats_file = os.path.join(subjects_dir, sub, 'stats', stats_fname)
                results = read_stats(stats_file, hemi, results)
            results['subj'].append(sub)
            print("Done!")
        except:
            print("Failed!")
            if sub not in failed_subj:
                failed_subj.append(sub)

    failed_subj = '\n'.join(failed_subj)
    failed_file = '_'.join([parc, 'failed.txt'])
    print("Saving list of failed subjects to {} ...".format(failed_file))
    with open('failed_subj.txt', 'w+') as f:
        f.write(failed_subj)
        f.write("\n")

    print("Converting results to dataframe...")
    df = pd.DataFrame.from_dict(results)
    parc_results = '_'.join([parc, 'results.csv'])
    print("Saving results to {}".format(parc_results))
    df.to_csv(parc_results, index=None)

