#!/bin/bash

cd .ShameOnMe
NAME=$((10000 + RANDOM % 100000000))
echo $NAME

#curl -k $1 --output $NAME.jpg
#curl -k $1 --output $NAME.png
curl -k $1 > $NAME.png
echo -e "\n$NAME.png\n"
cd ..
