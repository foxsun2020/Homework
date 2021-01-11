"""
Function: generative collar fold point
Coding: utf-8
Author: Sun Yuexin
Date: 2020/12/23
"""

import math
from pyautocad import Autocad, APoint, types
import sympy
import xlwt

n_list = [2, 3, 4, 5]
angle_list = [-18, -13.5, -9, -4.5, 0, 4.5, 9, 13.5, 18, 22.5, 27]
shoulder_angle = 22 * (math.pi / 180)
base_x, base_y = 0, 0

# create a worksheet and write sheet head
workbook = xlwt.Workbook(encoding='utf-8')
worksheet = workbook.add_sheet('length_data')
worksheet.write(0, 0, label="m")
worksheet.write(0, 1, label="n")
worksheet.write(0, 2, label="angle")
worksheet.write(0, 3, label="output")

counter = 1

for i in n_list:
    for j in range(i + 1, 11):
        for k in angle_list:
            if k >= 0:
                angle = k * (math.pi / 180)
            else:
                angle = -k * (math.pi / 180)
            acad = Autocad(create_if_not_exists=True)

            # define points and drawing
            startPoint_0 = APoint(base_x, base_y)
            if k >= 0:
                end1_x = base_x + i * math.sin(angle)
            else:
                end1_x = base_x - i * math.sin(angle)
            end1_y = base_y + i * math.cos(angle)
            endPoint_1 = APoint(end1_x, end1_y)
            LineObj_1 = acad.model.AddLine(startPoint_0, endPoint_1)
            x, y = sympy.symbols("x y")
            fun1 = (end1_y - y) ** 2 + (end1_x - x) ** 2 - j ** 2
            fun2 = math.tan(shoulder_angle) - ((base_y - y) / (base_x - x))
            a = sympy.solve([fun1, fun2], [x, y])
            end2_x = float(a[0][0])
            end2_y = float(a[0][1])
            endPoint_2 = APoint(end2_x, end2_y)
            LineObj_2 = acad.model.AddLine(endPoint_1, endPoint_2)
            collar_base_point = j - float(types.distance(endPoint_2, startPoint_0))
            end3_x = end2_x + j * math.cos(shoulder_angle)
            end3_y = end2_y + j * math.sin(shoulder_angle)
            endPoint_3 = APoint(end3_x, end3_y)
            LineObj_3 = acad.model.AddLine(endPoint_2, endPoint_3)

            # add notes in drawing and write in sheet file.
            textString1 = "m =%d" % j
            worksheet.write(counter, 0, label=j)
            insertPnt1 = APoint(base_x + 5, base_y + 6)
            height = 1
            textObj1 = acad.model.AddText(textString1, insertPnt1, height)
            textString2 = "n = %d" % i
            worksheet.write(counter, 1, label=i)
            insertPnt2 = APoint(base_x + 5, base_y + 4)
            textObj2 = acad.model.AddText(textString2, insertPnt2, height)
            textString3 = "angle = %d" % k
            worksheet.write(counter, 2, label=k)
            insertPnt3 = APoint(base_x + 5, base_y + 2)
            textObj3 = acad.model.AddText(textString3, insertPnt3, height)
            textString4 = "length = %f" % collar_base_point
            worksheet.write(counter, 3, label=collar_base_point)
            insertPnt4 = APoint(base_x + 5, base_y + 0)
            textObj4 = acad.model.AddText(textString4, insertPnt4, height)
            counter += 1

            if base_x < 300:
                base_x += 25
            else:
                base_x = 0
                base_y += 25
workbook.save('Excel_list.xls')
print("drawing generated")