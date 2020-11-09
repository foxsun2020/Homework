"""
Function: Compare students‘ major in CheckList.xlsx and Standard.xlsx with print result (pandas).
Author: Sun Yuexin
Date: 2020.10.27
"""

import pandas as pd
import time

time_start = time.time()
df1 = pd.read_excel('./CheckList.xlsx', sheet_name=0)  # open Checklist.xlsx
df2 = pd.read_excel('./Standard.xlsx', sheet_name=0)  # open Standard.xlsx
df3 = pd.merge(df1, df2, how='left', on=["考生编号"])  # merge two sheet
bool_list = df3['专业名称_x'] == df3['专业名称_y']  # compare and output bool list
for i, v in bool_list.items():  # output infos of difference.
    name = df1.values[i][1]
    id = df1.values[i][0]
    c_major = df3.values[i][6]
    s_major = df3.values[i][17]
    if v is False:
        print('%s(%s)----%s(×)---->%s(✓)' % (name, id, c_major, s_major))
time_end = time.time()
print('Time cost = %fs' % (time_end - time_start))
