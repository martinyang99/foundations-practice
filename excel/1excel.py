#!/user/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 16:44:25 2018

@author: martin
"""

#%%
import sys
from xlrd import open_workbook
input_file = sys.argv[1]
workbook = open_workbook(input_file)
print('Number of Worksheets:', workbook.nsheets)
for worksheet in workbook.sheets():
    print('Worksheet name:', worksheet.name, '\tRows:', worksheet.nrows, \
          '\tColumns:', worksheet.ncols )