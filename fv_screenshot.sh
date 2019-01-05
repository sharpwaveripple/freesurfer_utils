#!/bin/bash

module load freesurfer

subj_folder=$1
output_file=$2
freeview_cmd_file=~/bin/freesurfer_utils/fv_cmd.txt
cd $subj_folder/mri

freeview -cmd $freeview_cmd_file
montage ax00.png ax01.png ax02.png ax03.png ax04.png ax05.png ax06.png ax07.png ax08.png ax09.png ax10.png ax11.png \
	-tile 4x3 -geometry +0+0 $output_file
rm ax*.png

