"""
Function: Compare students‘ major in CheckList.xlsx and Standard.xlsx with print result.
Author: Sun Yuexin
Date: 2020.10.21
"""

import xlrd


# class Sheet:
#     def __init__(self, path):
#         self.path = path
#         excel = xlrd.open_workbook(path)
#         self.sheet = excel.sheets()[0]
#         self.nrows = self.sheet.nrows
#
#
# class Row(Sheet):
#     def __init__(self, path, row):
#         super().__init__(path)
#         self.nrows = self.sheet.nrows
#         self.id = self.sheet.row_values(row)[0]
#         self.name = self.sheet.row_values(row)[1]
#         self.major = self.sheet.row_values(row)[6]
#
#
# def check_major(c_path, s_path):
#     c_sheet = Sheet(c_path)
#     s_sheet = Sheet(s_path)
#     counter = 0
#     for a in range(1, c_sheet.nrows):
#         c_row = Row(c_path, a)
#         for b in range(1, s_sheet.nrows):
#             s_row = Row(s_path, b)
#             if c_row.id == s_row.id:
#                 counter += 1
#                 if c_row.major == s_row.major:
#                     pass
#                 else:
#                     print('%s(%s)----%s(×)---->%s(✓)' % (c_row.name, str(c_row.id)[0:15], c_row.major, s_row.major))
#     print('%s students checked' % counter)


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
    check_major(r'.\CheckList.xlsx', r'.\Standard.xlsx')
