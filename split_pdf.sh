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

# split
pdftk $SOURCE burst output $TEMP/$PREFIX%04d.pdf

# merge
i=1
python3 $BASE_DIR/partition.py $TEMP | 
while read line
do
    pdftk $line cat output f$i.pdf
    i=$((i+1))
done

# clean
rm $TEMP -rf
