#! /bin/bash

BASE_DIR=$(pwd)
SOURCE=$1
if [ "$SOURCE" == "" ]
then
    echo precisa de argumento
    exit
fi

TEMP=$(/usr/bin/mktemp -d)
PREFIX=a

# resize
JAM=$(basename $SOURCE .pdf)jam.pdf
pdfjam $SOURCE --a4paper --outfile $JAM

# split
pdftk $JAM burst output $TEMP/$PREFIX%04d.pdf

# process
ls $TEMP/$PREFIX*.pdf | parallel gs -dBATCH -dNOPAUSE -sDEVICE=pdfwrite -sColorConversionStrategy=Gray -sPDFSETTINGS=prepress -sOutputFile=$TEMP/{/}gs.pdf -I $BASE_DIR $BASE_DIR/PDFX_def.ps {}

# merge
pdftk  $TEMP/$PREFIX*gs.pdf cat output FINAL.pdf

# clean
rm $JAM
rm $TEMP -rf
