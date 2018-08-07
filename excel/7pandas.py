#!/user/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 13:54:23 2018

@author: martin
"""

#%%
import pandas as pd
import sys
input_file = sys.argv[1]
output_file = sys.argv[2]
df = pd.read_excel(input_file, 'january_2013', column_index=None)
df_column_by_index = df.iloc[:, [1, 4]]
writer = pd.ExcelWriter(output_file)
df_column_by_index.to_excel(writer, sheet_name='jan_2013_output', index=False)
writer.save()