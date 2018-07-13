#!user/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 16:55:16 2018

@author: martin
"""

#%%
import pandas as pd
import sys
input_file = sys.argv[1]
output_file = sys.argv[2]
data_frame = pd.read_csv(input_file)
data_frame_pattern = data_frame.loc[data_frame['Invoice Number'].str.startswith("001-"), :]
data_frame_pattern.to_csv(output_file)
print(data_frame)