"""
Function: Save data in sheet files to text files with inverted order.
Author: Sun Yuexin
Date: 2020.10.21
"""

import os
import xlrd
import re
import time


def main():
    path = r'.\CollegeCode'  # open the folder that need to operate
    counter = 0
    time_stamp = time.strftime("%Y%m%d_%H%M%S", time.localtime())
    for each in os.listdir(path):
        if re.match(r"^[0-9]{1,2}\.xlsx$", each):  # check file name by re
            file_name = str(time_stamp + '_' + os.path.splitext(each)[0])
            # add time-stamp in file name to prevent overwriting
            xlsx = xlrd.open_workbook(r'.\CollegeCode\%s' % each)
            sheet1 = xlsx.sheets()[0]
            sheet1_nrows = sheet1.nrows  # the number of row
            t = open(r'.\Output\%s.txt' % file_name, 'a', encoding='gbk')
            t.write(str(sheet1.row_values(0)) + '\n')  # insert sheet header
            for i in range(sheet1_nrows - 1, 0, -1):  # insert data
                t.write(str(sheet1.row_values(i)) + '\n')
            t.close()
            counter += 1
    print('%s files finished with name started with *%s*' % (counter, time_stamp))


if __name__ == '__main__':
    main()
