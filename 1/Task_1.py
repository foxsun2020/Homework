import os
import xlrd
import re


def main():
    path = r'.\CollegeCode'  # open the folder that need to operate
    for each in os.listdir(path):
        if re.match(r'^[0-9]{1,2}\.xlsx$', each):  # check file name by re
            file_name = os.path.splitext(each)[0]  # split file name and extract base name
            xlsx = xlrd.open_workbook(r'.\CollegeCode\%s' % each)
            sheet1 = xlsx.sheets()[0]
            sheet1_nrow = sheet1.nrows  # the number of row
            t = open(r'.\Output\%s.txt' % file_name, 'a', encoding='gbk')
            t.write(str(sheet1.row_values(0)) + '\n')  # insert sheet header
            for i in range(sheet1_nrow - 1, 0, -1):  # insert data
                t.write(str(sheet1.row_values(i)) + '\n')
            t.close()


if __name__ == '__main__':
    main()