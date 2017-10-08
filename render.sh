#!/bin/bash
rm -rf test.data
g++ main.cpp functions.cpp functions.h
./a.out
python imshow.py test.data
