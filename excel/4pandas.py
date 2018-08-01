#!/user/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 10:58:30 2018

@author: martin
"""

#%%
import pandas as pd
import sys
input_file = sys.argv[1]
output_file = sys.argv[2]
df = pd.read_excel(input_file, 'january_2013', index_col=None)
df_meets_condition = df[df['Sale Amount'].astype(float) > 1400.0]
writer = pd.ExcelWriter(output_file)
df_meets_condition.to_excel(writer, sheet_name='jan_2013_output', index=False)
writer.save()