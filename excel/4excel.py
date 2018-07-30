#!/user/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 23:26:54 2018

@author: marti
"""

#%%
import sys
from datetime import date
from xlrd import open_book, xldate_as_tuple
from xlwt import Workbook
input_file = sys.argv[1]
output_file = sys.argv[2]
output_workbook = Workbook()
output_worksheet = output_workbook.add_sheet('jan_2013_output')
sale_amount_column_index = 3
with open_book(input_file) as workbook:
    worksheet = workbook.sheet_by_name('january_2013')
    data = []