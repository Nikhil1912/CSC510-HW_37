# CSC510-HW_37
The objective of this repo is to replicate, in python, [this code](https://github.com/txt/se22/blob/main/etc/pdf/csv.pdf), which was originally written in Lua. 

This code takes in a CSV file and generates summaries of the columns. For numeric (Num) columns, this is median (the middle value of a sorted list of numbers thus far seen) and standard deviation (a measure of the spread of numbers); note that Num is a reservoir sampler which keeps only a finite quantity of numbers. For symbolic (Sym) columns, this is mode (the most common symbol) and entropy (the effort required to recreate a signal). 

To access tests, run `tests.py`. 
