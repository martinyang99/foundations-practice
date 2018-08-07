#!/user/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 17:02:28 2018

@author: martin
"""

#%%
import sys
from datetime import date
from xlrd import open_book, xldate_as_tuple
from xlwt import Workbook
input_file = sys.argv[1]
output_file = sys.argv[2]
