#!/bin/bash

dictionary_file=/usr/share/dict/words

myvar=$(wc -l < $dictionary_file)

random_line_number=${RANDOM}

echo no of lines: $myvar

echo random_line_number: $random_line_number

sed -n ${random_line_number}p ${dictionary_file}
