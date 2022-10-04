# CSC510-HW_37
[![DOI](https://zenodo.org/badge/545583203.svg)](https://zenodo.org/badge/latestdoi/545583203)

<a href="https://github.com/Nikhil1912/CSC510-HW_37/main/LICENSE.md"><img src="https://img.shields.io/github/license/Nikhil1912/CSC510-HW_37?style=plastic" /></a>

The objective of this repo is to replicate, in python, [this code](https://github.com/txt/se22/blob/main/etc/pdf/csv.pdf), which was originally written in Lua. 

This code takes in a CSV file and generates summaries of the columns. For numeric (Num) columns, this is median (the middle value of a sorted list of numbers thus far seen) and standard deviation (a measure of the spread of numbers); note that Num is a reservoir sampler which keeps only a finite quantity of numbers. For symbolic (Sym) columns, this is mode (the most common symbol) and entropy (the effort required to recreate a signal). 

## Running
* To run the program, navigate to `\CSC510-HW_37\code\Csv.py` and run using python (`python Csv.py`)
* Tests are contained in `\CSC510-HW_37\code\Tests.py`
