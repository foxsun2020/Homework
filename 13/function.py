"""
Function: 
Coding: utf-8
Author: Sun Yuexin
Date:
"""

import math
from pyautocad import Autocad, APoint
import sympy

n = 3
m = 6
angle = 9 * (math.pi / 180)

acad = Autocad(create_if_not_exists=True)
startPoint_0 = APoint(0, 0)
endPoint_1 = APoint(1, 1)
LineObj_1 = acad.model.AddLine(startPoint_0, endPoint_1)

endPoint_2 = APoint(-2, -3)
LineObj_2 = acad.model.AddLine(endPoint_1, endPoint_2)