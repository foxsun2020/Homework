"""
Function: Find Mean, Variance, Standard Variance of X(discrete random variables)
Coding: utf-8
Author: Sun Yuexin
Date: 2020/11/10
"""

import numpy as np  # using version-1.19.3 if you are Windows PC


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


if __name__ == '__main__':
    arr = arr_input()
    arr_mean = np.mean(arr)
    arr_var = np.var(arr)
    arr_std = np.std(arr)
    print("Mean: %f" % arr_mean)
    print("Variance: %f" % arr_var)
    print("Std_Variance: %f" % arr_std)





