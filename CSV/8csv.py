#!/user/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 09:10:20 2018

@author: martin
"""

#%%
import csv
import glob
import os
import sys
input_file = sys.argv[1]
file_counter = 0
for input_file in glob.glob(os.path.join(input_file, 'sales_*')):
    row_counter = 1
    with open(input_file, 'r', newline='') as csv_in_file:
        filereader = csv.reader(csv_in_file)
        header = next(filereader, None)
        for row in filereader:
            row_counter +=1
    print('{0!s}: \t{1:d} rows \t{2:d} columns'.format(os.path.basename(input_file), row_counter, len(header)))
    file_counter +=1
print('Number of files: {0:d}'.format(file_counter))