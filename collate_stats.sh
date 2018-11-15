#!/bin/bash

module load freesurfer
export SUBJECTS_DIR=/home/jt629/SCANS_FS/

aseg_bin=$(which asegstats2table)
aparc_bin=$(which aparcstats2table)

for hemi in lh rh; do
    for meas in volume thickness area meancurv gauscurv; do
	python2 $aparc_bin \
	    --subjectsfile=recon_check/completed.txt \
	    --hemi=$hemi \
	    --meas=$meas \
	    --parc=aparc \
	    --delimiter=comma \
	    --tablefile=${hemi}_${meas}.csv
    done
done

python2 $aseg_bin \
    --subjectsfile=recon_check/completed.txt \
    --delimiter=comma \
    --tablefile=aseg_stats.csv

paste -d, lh_volume.csv rh_volume.csv \
	lh_thickness.csv rh_thickness.csv \
	lh_area.csv rh_area.csv \
	lh_meancurv.csv rh_meancurv.csv \
	lh_gauscurv.csv rh_gauscurv.csv \
	aseg_stats.csv > fs_stats.csv

for hemi in lh rh; do
    for meas in volume thickness area meancurv gauscurv; do
        rm ${hemi}_${meas}.csv
    done
done
rm aseg_stats.csv
   
SED_ARGS='
s/lh_/L_/g
s/rh_/R_/g
s/_thickness/_CT/g
s/_area/_SA/g
s/_volume/_VOL/g
s/_meancurv/_MC/g
s/_gauscurv/_GC/g
s/Left-/L_/g
s/Right-/R_/g
s/bankssts/BSTS/g
s/caudalanteriorcingulate/cACG/g
s/caudalmiddlefrontal/cMFG/g
s/cuneus/CUN/g
s/entorhinal/ENT/g
s/fusiform/FUS/g
s/inferiorparietal/IPL/g
s/inferiortemporal/ITG/g
s/isthmuscingulate/iCG/g
s/lateraloccipital/LOG/g
s/lateralorbitofrontal/lOFG/g
s/lingual/LING/g
s/medialorbitofrontal/mOFG/g
s/middletemporal/MTG/g
s/parahippocampal/PHG/g
s/paracentral/paraCG/g
s/parsopercularis/pOPER/g
s/parsorbitalis/pORB/g
s/parstriangularis/pTRI/g
s/pericalcarine/CAL/g
s/postcentral/postCG/g
s/posteriorcingulate/pCC/g
s/precentral/preCG/g
s/precuneus/PCUN/g
s/rostralanteriorcingulate/rACG/g
s/rostralmiddlefrontal/rMFG/g
s/superiorfrontal/SFG/g
s/superiorparietal/SPL/g
s/superiortemporal/STG/g
s/supramarginal/SMAR/g
s/frontalpole/FP/g
s/temporalpole/TP/g
s/transversetemporal/TTG/g
s/insula/INS/g
s/Thalamus.Proper/THAL_VOL/g
s/Putamen/PUT_VOL/g
s/Pallidum/PALL_VOL/g
s/Caudate/CAUD_VOL/g
s/Hippocampus/HIPP_VOL/g
s/Amygdala/AMYG_VOL/g
s/Accumbens.area/ACCU_VOL/g
'

sed -i -e "${SED_ARGS}" fs_stats.csv
