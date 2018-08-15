#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 12 14:14:56 2018

@author: Martin
"""

#%%
import pandas as pd
import sys
input_file = sys.argv[1]
output_file = sys.argv[2]
my_sheets = [0,1]
threshold = 1900
df = pd.read_excel(input_file, sheet_name=my_sheets, index_col=None)
row_list = []
for worksheet_name, data in df.items():
    row_list.append(data[data['Sale Amount'].astype(float) > threshold])
    #print(row_list)
filtered_rows = pd.concat(row_list, axis=0, ignore_index=True)
#print(filtered_rows)
writer = pd.ExcelWriter(output_file)
filtered_rows.to_excel(writer, sheet_name='set_of_worksheets', index=False)
writer.save()