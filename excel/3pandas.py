#!/user/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 14:59:46 2018

@author: martin
"""

#%%
import pandas as pd
import sys
input_file = sys.argv[1]
output_file = sys.argv[2]
df = pd.read_excel(input_file, sheet_name='january_2013')
writer = pd.ExcelWriter(output_file)
df.to_excel(writer, sheet_name='jan_2013_output', index=False)
writer.save()