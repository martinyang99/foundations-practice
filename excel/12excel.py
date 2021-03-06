#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 16:33:36 2018

@author: martin
"""

#%%
import glob
import os
import sys
from xlrd import open_workbook
input_directory = sys.argv[1]
workbook_counter = 0
for input_file in glob.glob(os.path.join(input_directory, '*.xlsx')):
    workbook = open_workbook(input_file)
    print('Workbook: {:s}'.format(os.path.basename(input_file)))
    print('Number of worksheet: {:d}'.format(workbook.nsheets))
    for worksheet in workbook.sheets():
        print('Worksheet name: {:s}'.format(worksheet.name),\
              '\tRows: {:d}'.format(worksheet.nrows), '\tColumns: {:d}'.format(worksheet.ncols))
    workbook_counter+=1
print('Number of Excel workbooks: {:d}'.format(workbook_counter))