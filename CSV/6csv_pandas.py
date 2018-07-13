#!user/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 17:42:18 2018

@author: martin
"""

#%%
import pandas as pd
import sys
input_file = sys.argv[1]
output_file = sys.argv[2]
data_frame = pd.read_csv(input_file)
data_frame_columns = data_frame.iloc[:, [0, 3]]
data_frame_columns.to_csv(output_file, index=False)