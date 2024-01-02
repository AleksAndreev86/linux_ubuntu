#!/bin/bash

dir=$1
if [ -d $dir ]
then 
        rm -f $dir/*.bak
        rm -f $dir/*.tmp
        rm -f $dir/*.backup
        echo "Операция успешно завершена!"
        exit 0
else
        echo "Директория не найдена"
        exit 1
fi
