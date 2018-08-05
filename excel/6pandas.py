#!/user/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  5 23:31:19 2018

@author: Martin
"""

#%%
import pandas as pd
import sys
input_file = sys.argv[1]
output_file = sys.argv[2]
df = pd.read_excel(input_file, 'january_2013', index_col=None)
df_value_matches_pattern = df[df['Customer Name'].str.startswith('J')]
writer = pd.ExcelWriter(output_file)
df_value_matches_pattern.to_excel(writer, sheet_name='jan_2013_output', index=False)
writer.save()