#!user/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 23:10:19 2018

@author: marti
"""

#%%
import pandas as pd
import sys
inputfile = sys.argv[1]
outputfile = sys.argv[2]
data_frame = pd.read_csv(inputfile)
data_frame['Cost'] = data_frame['Cost'].str.strip('$').astype(float)
data_frame_value_meets_condition = data_frame.loc[(data_frame['Supplier Name']\
.str.contains('Z')) | (data_frame['Cost'] > 600.0), :]
data_frame_value_meets_condition.to_csv(outputfile, index=False)