#!user/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 17:26:08 2018

@author: martin
"""

#%%
import csv
import sys
input_file = sys.argv[1]
output_file = sys.argv[2]
my_columns = [0, 3]
with open(input_file, 'r', newline='') as csv_in_file:
    with open(output_file, 'w', newline='') as csv_out_file:
        filereader = csv.reader(csv_in_file)
        filewriter = csv.writer(csv_out_file)
        for row_list in filereader:
            row_list_out = []
            for index_value in my_columns:
                row_list_out.append(row_list[index_value])
            filewriter.writerow(row_list_out)
        