"""
Function: The Method of Least Squares
Coding: utf-8
Author: Sun Yuexin
Date:
"""

if __name__ == '__main__':
    x = [0.5,1.0,1.6,1.8,2.6,3.2,3.8,4.7]
    y = [0.28,0.29,0.29,0.18,0.17,0.18,0.10,0.12]
    n = len(x)
    x_square_sum, x_sum, y_sum, xy_sum = 0, 0, 0, 0
    for i, j in zip(x, y):
        x_square_sum += i ** 2
        x_sum += i
        y_sum += j
        xy_sum += i * j
    x_mean = x_sum / n
    y_mean = y_sum / n
    Lxx = x_square_sum - (1 / n) * (x_sum ** 2)
    Lxy = xy_sum - (1 / n) * x_sum * y_sum

    b = Lxy / Lxx
    a = y_mean - b * x_mean
    print("x_square_sum, x_sum, y_sum, xy_sum", "\n", x_square_sum, x_sum, y_sum, xy_sum)
    print("x_mean, y_mean = ", x_mean, y_mean)
    print("Lxx = ", Lxx, "Lxy = ", Lxy)
    if b > 0:
        print("y^ = a^ - b^x = ", a, "+", b, "x")
    else:
        print("y^ = a^ - b^x = ", a, b, "x")

