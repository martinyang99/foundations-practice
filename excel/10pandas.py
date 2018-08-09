#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 16:19:38 2018

@author: martin
"""

#%%
import pandas as pd
import sys
input_file = sys.argv[1]
output_file = sys.argv[2]
df = pd.read_excel(input_file, sheet_name=None, index_col=None)
print(df)
column_output = []
for worksheet_name, data in df.items():
    column_output.append(data.loc[:, ['Customer Name', 'Sale Amount']])
    #print(column_output)
selected_columns = pd.concat(column_output, axis=0, ignore_index=True)
#print(selected_columns)
writer = pd.ExcelWriter(output_file)
selected_columns.to_excel(writer, sheet_name='selected_columns_all_worksheets',\
                          index=False)
writer.save()