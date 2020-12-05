"""
Function: 
Coding: utf-8
Author: Sun Yuexin
Date:
"""

data = open("database.txt", mode="w+", encoding="utf-8")
i = 0
j = 1
while i < 700000000:
    data.write("github-zsqw1234")
    if i % 10000:
        print("writen %dW data" % j)
        j += 1
    i += 1
data.close()