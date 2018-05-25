#!/bin/bash

for filename in pos/*.jpg; do
    opencv_createsamples -img "$filename" -bg bg.txt -info info/info.lst -pngoutput info -maxxangle 0.5 -maxyangle 0.5 -maxzangle 0.5 -num 1950
done