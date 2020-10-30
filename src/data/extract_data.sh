#!/bin/bash
FILE=../../data/raw/MICRODADOS_ENEM_$1.csv
if test -f "$FILE"; then
    rm $FILE
fi

unzip -j ../../data/external/microdados_enem$1.zip DADOS/MICRODADOS_ENEM_$1.csv -d ../../data/raw