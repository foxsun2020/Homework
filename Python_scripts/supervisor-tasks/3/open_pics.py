"""
Function: Convert RGB pictures in folder into grayscale and open them.
Author: Sun Yuexin
Date: 2020.11.9
"""

import os
from PIL import Image

path = r".\pic_source"
for each in os.listdir(path):
    im = Image.open(r".\pic_source\%s" % each).convert("L")
    im.show()