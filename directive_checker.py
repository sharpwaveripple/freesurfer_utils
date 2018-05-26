#!/usr/bin/env python 

import os
import argparse

# todo: read all contents into memory, then compare strings

def parse_input():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", type=str, required=True,
                        help="Input directory")
    args = parser.parse_args()
    return args


def reconall_table(directives):
    ar1 = {"motioncorr": "mri/orig.mgz",
           "talairach":  "mri/transforms/talairach_avi.log",
           "nuintensitycor": "mri/nu.mgz",
           "normalization": "mri/T1.mgz",
           "skullstrip": "mri/brainmask.mgz"}
    ar2_subcort = {"gcareg": "mri/transforms/talairach.lta",
                   "canorm": "mri/norm.mgz",
                   "careg": "mri/transforms/talairach.m3z",
                   "calabel": "mri/aseg.presurf.mgz"}
    ar2_subcort2fix = {"normalization2": "mri/brain.mgz",
                       "maskbfs": "mri/brain.finalsurfs.mgz",
                       "segmentation": "mri/wm.mgz",
                       "fill": "mri/filled.mgz",
                       "tessellate": "surf/rh.orig.nofix",
                       "smooth1": "surf/rh.smoothwm.nofix",
                       "inflate1": "surf/rh.inflated.nofix",
                       "qsphere": "surf/rh.qsphere.nofix"}
    ar2_fix = {"fix": "surf/rh.orig"}
    ar2_postfix = {"white": "label/rh.cortex.label",
                   "smooth2": "surf/rh.smoothwm",
                   "inflate2": "surf/rh.sulc",
                   "curvHK": "surf/rh.inflated.K",
                   "curvstats": "stats/rh.curv.stats"}
    ar3 = {"sphere": "surf/rh.sphere",
           "surfreg": "surf/rh.sphere.reg",
           "jacobian_white": "surf/rh.jacobian_white",
           "avgcurv": "surf/rh.avg_curv",
           "cortparc": "label/rh.aparc.annot",
           "pial": "surf/rh.thickness",
           "cortribbon": "mri/ribbon.mgz",
           "parcstats": "label/aparc.annot.ctab",
           "cortparc2": "label/rh.aparc.a2009s.annot",
           "parcstats2": "label/aparc.annot.a2009s.ctab",
           "cortparc3": "label/rh.aparc.DKTatlas.annot",
           "parcstats3": "label/aparc.annot.DKTatlas.ctab",
           "pctsurfcon": "stats/rh.w-g.pct.stats",
           "hyporelabel": "mri/aseg.presurf.hypos.mgz",
           "aparc2aseg": "mri/aparc.DKTatlas+aseg.mgz",
           "apas2aseg": "mri/aseg.mgz",
           "segstats": "stats/aseg.stats",
           "wmparc": "mri/wmparc.mgz",
           "balabels": "label/rh.entorhinal_exvivo.label"}
    if directives == "all":
        return {**ar1, **ar2_subcort, **ar2_subcort2fix,
                **ar2_fix, **ar2_postfix, **ar3}


def sub_dir_contents(sub_dir):
    dir_contents = sorted(os.listdir(sub_dir))
    if "fsaverage" in dir_contents:
        dir_contents.remove("fsaverage")
    return dir_contents


def recon_check_dir():
    if not os.path.exists("recon_check"):
        os.makedirs("recon_check")
    else:
        check_files = os.listdir("recon_check")
        [os.remove(os.path.join("recon_check", x)) for x in check_files]


def directive_checker(directives, base_path, sub_list, print_check=None):
    directive_dict = reconall_table(directives)
    recon_check_dir()
    for sub in sub_list:
        if print_check is not None:
            print(f"Checking {sub}... ", end="")
        running_status = os.path.join(base_path, sub,
                                      "scripts/IsRunning.lh+rh")
        # if os.path.isfile(running_status):
        #     print("Is running")
        #     continue
        last_file = os.path.join(base_path, sub,
                                 "label/rh.entorhinal_exvivo.label")
        if os.path.isfile(last_file):
            print("Finished main recon-all stream")
            with open("recon_check/completed.txt", "a+") as f:
                f.write(sub + '\n')
        else:
            for directive, output in directive_dict.items():
                directive_file = os.path.join(base_path, sub, output)
                if os.path.isfile(directive_file):
                    pass
                else:
                    print(f"Stopped at {directive}")
                    with open(f"recon_check/{directive}.txt", "a+") as f:
                        f.write(sub + '\n')
                    break


def io_stream():
    args = parse_input()
    subj_list = sub_dir_contents(args.i)
    directive_checker("all", args.i, subj_list, '')
    print("Done")


if __name__ == "__main__":
    io_stream()
