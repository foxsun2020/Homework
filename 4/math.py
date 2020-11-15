"""
Function: Find Mean, Variance, Standard Variance of X(discrete random variables)
Coding: utf-8
Author: Sun Yuexin
Date: 2020/11/10
"""

import numpy as np  # using version-1.19.3 if you are Windows PC
import math


def arr_input():
    array = []
    while True:
        num = input("Input variable or end:")
        if num == "end":
            break
        else:
            array.append(float(num))
            print(array, "-" * 10,len(array))
    return array


def sum_ln(ar):
    sum = 0
    for num in ar:
        ln = math.log(num, math.e)
        sum += ln
    return sum


def var(ar):
    sum = 0
    for num in ar:
        dis = num - np.mean(ar)
        sum += dis * dis
    return sum/(len(ar) - 1)


if __name__ == '__main__':
    # arr = arr_input()
    arr = [2.14, 2.1, 2.13, 2.15, 2.13, 2.12, 2.13, 2.1, 2.15, 2.12, 2.14, 2.1, 2.13, 2.11, 2.14, 2.11]
    arr_mean = np.mean(arr)
    arr_var = var(arr)
    arr_std = var(arr) ** 0.5
    print("Mean: %f" % arr_mean)
    print("Variance (unbiased): %f" % arr_var)
    print("Std_Variance (unbiased): %f" % arr_std)
    # print(-(1+len(arr)/sum_ln(arr)))





