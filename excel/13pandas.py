#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 15:40:53 2018

@author: martin
"""

#%%
import pandas as pd
import sys
import os
import glob
input_path = sys.argv[1]
output_file = sys.argv[2]
all_workbooks = glob.glob(os.path.join(input_path, '*.xlsx'))
df = []
for workbook in all_workbooks:
    all_worksheets = pd.read_excel(workbook, sheet_name=None, index_col=False)
    for worksheet_name, data in all_worksheets.items():
        df.append(data)
all_data_concatenated = pd.concat(df, axis=0, ignore_index=True)
writer = pd.ExcelWriter(output_file)
all_data_concatenated.to_excel(writer, sheet_name='all_data_all_workbooks',\
                               index=False)
writer.save()