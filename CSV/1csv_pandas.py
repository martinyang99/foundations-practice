#!user/bin/env pethon3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 09:43:57 2018

@author: martin
"""

import sys
import pandas as pd
input_file = sys.argv[1]
output_file = sys.argv[2]
data_frame = pd.read_csv(input_file)
print(data_frame)
data_frame.to_csv(output_file, index=False)