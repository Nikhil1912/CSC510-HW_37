# CSC510 Software Engineering Group 37 Presents: Column Summaries
[![DOI](https://zenodo.org/badge/545583203.svg)](https://zenodo.org/badge/latestdoi/545583203)
<a href="https://github.com/Nikhil1912/CSC510-HW_37/main/LICENSE.md"><img src="https://img.shields.io/github/license/Nikhil1912/CSC510-HW_37?style=plastic" /></a>
![GitHub issues](https://img.shields.io/github/issues/Nikhil1912/CSC510-HW_37)
![Repo Size](https://img.shields.io/github/repo-size/Nikhil1912/CSC510-HW_37?color=brightgreen)
![Test](https://github.com/Nikhil1912/CSC510-HW_37/main/actions/workflows/python-app.yml/badge.svg?maxAge=10000)

## Objective
The objective of this repository is to replicate, in python, [this code](https://github.com/txt/se22/blob/main/etc/pdf/csv.pdf), which was originally written in Lua. 

This code reads in a .csv file and generates summaries of the columns. For numeric (Num) columns, this is median (the middle value of a sorted list of numbers thus far seen) and standard deviation (a measure of the spread of numbers); note that Num is a reservoir sampler which keeps only a finite quantity of numbers. For symbolic (Sym) columns, this is mode (the most common symbol) and entropy (the effort required to recreate a signal). 

For an example .csv in the required format, check out `\data\auto93.csv`

## Running
* To install necessary packages, run `pip install -r requirements.txt`
* To run the program, navigate to `\CSC510-HW_37\code` and run `python Csv.py`
* Tests are contained in `\CSC510-HW_37\code\Tests.py`

Example output is shown below:


![hw_output_csv](https://user-images.githubusercontent.com/112109564/193937499-81c90369-a0e8-472b-bb4b-2a696a32ce6a.PNG)

![hw_output_csv_2](https://user-images.githubusercontent.com/112109564/193937508-f4f36d3e-8fa3-4df3-a798-5337af73f249.PNG)

## Testing
The output of running `\CSC510-HW_37\code\Tests.py` is shown below:

![hw_test](https://user-images.githubusercontent.com/112109564/193937316-195d8279-6969-42ed-87ed-9145cd62c780.PNG)
