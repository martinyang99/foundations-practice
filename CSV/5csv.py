#!uset/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 09:42:19 2018

@author: martin
"""

#%%
import csv
import re
import sys
input_file = sys.argv[1]
output_file = sys.argv[2]
pattern = re.compile(r'(?P<my_pattern_group>^001-.*)', re.I)
with open(input_file, 'r', newline='') as csv_in_file:
    with open(output_file, 'w', newline='') as csv_out_file:
        filereader = csv.reader(csv_in_file)
        filewriter = csv.writer(csv_out_file)
        header = next(filereader)
        filewriter.writerow(header)
        for row_list in filereader:
            invoice_number = row_list[1]
            if pattern.search(invoice_number):
                filewriter.writerow(row_list)
                print(pattern.search(invoice_number).group('my_pattern_group'))