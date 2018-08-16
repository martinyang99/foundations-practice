#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 11:45:28 2018

@author: martin
"""

#%%
import pandas as pd
import glob
import sys
import os
input_path = sys.argv[1]
output_file = sys.argv[2]
all_workbooks = glob.glob(os.path.join(input_path, '*.xlsx'))
df = []
for workbook in all_workbooks:
    all_worksheets = pd.read_excel(workbook, sheet_name=None, index_col=None)
    workbook_total_sales = []
    workbook_number_of_sales = []
    worksheet_df = []
    worksheets_df = None
    workbook_df = None
    for worksheet_name, d in all_worksheets.items():
        total_sales = pd.DataFrame([float(str(value).strip('$').replace(',',''))\
                                    for value in d.loc[:, 'Sale Amount']]).sum()
        number_of_sales = len(d.loc[:, 'Sale Amount'])
        average_sales = pd.DataFrame(total_sales / number_of_sales)
        workbook_total_sales.append(total_sales)
        workbook_number_of_sales.append(number_of_sales)
        d = {"workbook": os.path.basename(workbook), "worksheet": worksheet_name, \
                "worksheet_total": total_sales, "worksheet_average": average_sales}
        d1 = pd.DataFrame(data=d)
        worksheet_df.append(d1)
    worksheets_df = pd.concat(worksheet_df, axis=0, ignore_index=True)
    workbook_total = pd.DataFrame(workbook_total_sales).sum()
    workbook_total_number_of_sales = pd.DataFrame(workbook_number_of_sales).sum()
    workbook_average = pd.DataFrame(workbook_total / workbook_total_number_of_sales)
    workbook_stats = {"workbook": os.path.basename(workbook), "workbook_total": \
                      workbook_total, "workbook_average": workbook_average}
    workbook_stats1 = pd.DataFrame(data=workbook_stats)
    workbook_df = pd.merge(worksheet_df, workbook_stats1, on='workbook', how='left')
    df.append(workbook_df)
all_data_concatenated = pd.concat(df, axis=0, ignore_index=True)
writer = pd.ExcelWriter(output_file)
all_data_concatenated.to_excel(writer, sheet_name='sums and averages', index=False)
writer.save()