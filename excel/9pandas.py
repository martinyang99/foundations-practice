#!usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 22:49:57 2018

@author: marti
"""

#%%
import pandas as pd
import sys
input_file = sys.argv[1]
output_file = sys.argv[2]
df = pd.read_excel(input_file, sheet_name=None, index_col=None)
row_output = []
for worksheet_name, data in df.items():
    row_output.append(data[data['Sale Amount'].astype(float) > 2000])
    print(row_output)
filtered_rows = pd.concat(row_output, axis=0, ignore_index=True)
print(filtered_rows)
writer = pd.ExcelWriter(output_file)
filtered_rows.to_excel(writer, sheet_name='sale_amount_gt2000', index=False)
writer.save()