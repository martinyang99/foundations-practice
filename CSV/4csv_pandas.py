#!user/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 14:05:41 2018

@author: martin
"""

#%%
import pandas as pd
import sys
input_file = sys.argv[1]
output_file = sys.argv[2]
data_frame = pd.read_csv(input_file)
important_dates = ['1/20/14', '1/30/14']
data_frame_value = data_frame.loc[data_frame['Purchase Date'].isin(important_dates), :]
data_frame_value.to_csv(output_file, index=False)