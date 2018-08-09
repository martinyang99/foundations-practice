#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 23:01:56 2018

@author: marti
"""

#%%
import sys
from datetime import date
from xlrd import open_workbook, xldate_as_tuple
from xlwt import Workbook
input_file = sys.argv[1]
output_file = sys.argv[2]
output_workbook = Workbook()
output_worksheet = output_workbook.add_sheet('set_of_worksheets')
my_sheet = [0,1]
threshold = 1900
sales_column_index = 3
first_worksheet = True
data = []
with open_workbook(input_file) as workbook:
    for sheet_index in range(workbook.nsheets):
        
    