#!/user/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 14:48:04 2018

@author: martin
"""

#%%
import pandas as pd
import sys
input_file = sys.argv[1]
output_file = sys.argv[2]
df = pd.read_excel(input_file, 'january_2013', index_col=None)
df_column_by_name = df.loc[:, ['Customer ID', 'Purchase Date']]
writer = pd.ExcelWriter(output_file)
df_column_by_name.to_excel(writer, sheet_name = 'jan_2013_output', index=False)
writer.save()