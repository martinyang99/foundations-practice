#!user/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 17:04:55 2018

@author: martin
"""

import csv
import sys
input_file = sys.argv[1]
output_file = sys.argv[2]
with open(input_file, 'r', newline='') as csv_in_file:
    with open(output_file, 'w', newline='') as csv_out_file:
        filereader = csv.reader(csv_in_file)
        filewriter = csv.writer(csv_out_file)
        