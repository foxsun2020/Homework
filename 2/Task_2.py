import xlrd


def check_major(c_path, s_path):
    c_excel = xlrd.open_workbook(c_path)  # open Checklist.xlsx
    s_excel = xlrd.open_workbook(s_path)  # open Standard.xlsx
    c_sheet = c_excel.sheets()[0]
    s_sheet = s_excel.sheets()[0]
    c_nrow = c_sheet.nrows  # the number of row - Checklist.xlsx
    s_nrow = s_sheet.nrows  # the number of row - Standard.xlsx
    for a in range(1, c_nrow):  # info from Checklist.xlsx
        c_stu_id = c_sheet.row_values(a)[0]
        name = c_sheet.row_values(a)[1]
        c_major = c_sheet.row_values(a)[6]
        for b in range(1, s_nrow):  # info from Standard.xlsx
            s_stu_id = s_sheet.row_values(b)[0]
            s_major = s_sheet.row_values(b)[6]
            if c_stu_id == s_stu_id:  # compare and judge
                if c_major == s_major:
                    continue
                else:
                    print('考生编号 %s 的 %s 应为 %s，误选为 %s' % (str(c_stu_id)[0:15], name, s_major, c_major))


if __name__ == '__main__':
    check_major(r'.\CheckList.xlsx', r'.\Standard.xlsx')