#!user/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 23:10:19 2018

@author: marti
"""

#%%
import sys
import csv
inputfile = sys.argv[1]
outputfile = sys.argv[2]
important_dates = ['1/20/14', '1/30/14']
with open(inputfile, 'r', newline='') as csv_in_file:
    with open(outputfile, 'w', newline='') as csv_out_file:
        filereader = csv.reader(csv_in_file)
        filewriter = csv.writer(csv_out_file)
        header = next(filereader)
        filewriter.writerow(header)
        for row_list in filereader:
            a_date = row_list[4]
            if a_date in important_dates:
                filewriter.writerow(row_list)