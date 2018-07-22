#!/user/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 22 23:18:18 2018

@author: marti
"""

#%%
import pandas as pd
import sys
input_file = sys.argv[1]
output_file = sys.argv[2]
header_list = ['Spplier Name', 'Invoice Number', 'Part Number', 'Cost', 'Purchase Date']
data_frame = pd.read_csv(input_file, header=None, names=header_list)
data_frame.to_csv(output_file, index=False)