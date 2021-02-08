"""
***Take a long time to run!!!***
Function: Compare students‘ major in CheckList.xlsx and Standard.xlsx with print result(Class).
Author: Sun Yuexin
Date: 2020.10.23
"""

import xlrd


class Sheet:
    def __init__(self, path):
        self.path = path
        excel = xlrd.open_workbook(path)
        self.sheet = excel.sheets()[0]
        self.nrows = self.sheet.nrows


class Row(Sheet):
    def __init__(self, path, row):
        super().__init__(path)
        self.nrows = self.sheet.nrows
        self.id = self.sheet.row_values(row)[0]
        self.name = self.sheet.row_values(row)[1]
        self.major = self.sheet.row_values(row)[6]


def check_major(c_path, s_path):
    c_sheet = Sheet(c_path)
    s_sheet = Sheet(s_path)
    counter = 0
    for a in range(1, c_sheet.nrows):
        c_row = Row(c_path, a)
        print('%s checking' % a)
        for b in range(1, s_sheet.nrows):
            s_row = Row(s_path, b)
            if c_row.id == s_row.id:
                counter += 1
                if c_row.major == s_row.major:
                    pass
                else:
                    print('%s(%s)----%s(×)---->%s(✓)' % (c_row.name, str(c_row.id)[0:15], c_row.major, s_row.major))
    print('%s students checked' % counter)


if __name__ == '__main__':
    check_major(r'.\CheckList.xlsx', r'.\Standard.xlsx')
