"""
Function: Compare students‘ major in CheckList.xlsx and Standard.xlsx with print result(xlrd).
Author: Sun Yuexin
Date: 2020.10.21
"""

import xlrd
import time


def check_major(c_path, s_path):
    c_excel = xlrd.open_workbook(c_path)  # open Checklist.xlsx
    s_excel = xlrd.open_workbook(s_path)  # open Standard.xlsx
    c_sheet = c_excel.sheets()[0]
    s_sheet = s_excel.sheets()[0]
    c_nrows = c_sheet.nrows  # the number of row - Checklist.xlsx
    s_nrows = s_sheet.nrows  # the number of row - Standard.xlsx
    counter = 0
    for a in range(1, c_nrows):  # info from Checklist.xlsx
        c_stu_id = c_sheet.row_values(a)[0]
        name = c_sheet.row_values(a)[1]
        c_major = c_sheet.row_values(a)[6]
        for b in range(1, s_nrows):  # info from Standard.xlsx
            s_stu_id = s_sheet.row_values(b)[0]
            s_major = s_sheet.row_values(b)[6]
            if c_stu_id == s_stu_id:  # compare and judge
                counter += 1
                if c_major == s_major:
                    pass
                else:
                    print('%s(%s)----%s(×)---->%s(✓)' % (name, str(c_stu_id)[0:15], c_major, s_major))
    print('%s students checked' % counter)


if __name__ == '__main__':
    time_start = time.time()
    check_major(r'.\CheckList.xlsx', r'.\Standard.xlsx')
    time_end = time.time()
    print('Time cost = %fs' % (time_end - time_start))
