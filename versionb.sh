#!/bin/bash
file=$1
file_name=$(basename $file)
extension="${file_name##*.}"
file_name="${file_name%.*}"
#given file name without extension : $file_name
#given file name extension : $extension
now=$(date +"%m_%d_%y")
#Required date after the file name is
touch $file_name'_'$now'.'$extension

