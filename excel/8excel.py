#!/user/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 17:02:28 2018

@author: martin
"""

#%%
import sys
from datetime import date
from xlrd import open_book, xldate_as_tuple
from xlwt import Workbook
input_file = sys.argv[1]
output_file = sys.argv[2]
output_workbook = Workbook()
output_worsheet = output_workbook.add_sheet('jan_2013_output')
my_columns = ['Customer ID', 'Purchase Date']
with open_book(input_file) as workbook:
    worksheet = workbook.sheet_by_name('january_2013')
    data = [my_columns]
    header_list = worksheet.row_values(0)
    header_index_list = []
    for header_index in range(len(header_list)):
        if header_list[header_index] in my_columns:
            header_index_list.append(header_index)
            
