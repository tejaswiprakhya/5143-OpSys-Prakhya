#!/bin/bash
file=$1
#passed file name as parameter: $file
pattern=$(date +"%m_%d_%y")
new_file=$pattern'_'$file
#creating copy of file after adding date to the given parameter
touch $new_file
