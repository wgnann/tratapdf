#! /bin/bash

DEPS="
    libgs10-common
    icc-profiles
    poppler-utils
    texlive-extra-utils
    python3-tk
"

for i in $DEPS
do
    dpkg -s $i > /dev/null
    if [ $? -ne 0 ]
    then
        echo "não encontrei o pacote $i"
        exit
    fi
done

BASE_DIR=$(pwd)
PDFX=$(dpkg -S PDFX_def.ps | cut -d: -f2)
ICC=$(dpkg -S ISOuncoated.icc | cut -d: -f2)
cp $PDFX $BASE_DIR
cp $ICC $BASE_DIR

ICCPATH=$BASE_DIR/ISOuncoated.icc
sed -i "s|^/ICCProfile.*|/ICCProfile ($ICCPATH) def|g" $BASE_DIR/PDFX_def.ps
