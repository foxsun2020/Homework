"""
Function: The Method of Least Squares
Coding: utf-8
Author: Sun Yuexin
Date:
"""

if __name__ == '__main__':
    # x = [49508,55152,60894,64181,41248,69609,81745,141165,135596,138593,142892,161761,259414,163738,184936,266081,313254,461484]
    # y = [527,860,1063,1281,1027,1823,2354,3997,4819,5432,6333,7090,10548,8837,9726,13837,16341,21802]
    x = [0.5,1.0,1.6,1.8,2.6,3.2,3.8,4.7]  # 3
    y = [0.28,0.29,0.29,0.18,0.17,0.18,0.10,0.12]
    n = len(x)
    alpha = 0.05
    x_square_sum, y_square_sum, x_sum, y_sum, xy_sum = 0, 0, 0, 0, 0
    for i, j in zip(x, y):
        x_square_sum += i ** 2
        y_square_sum += j ** 2
        x_sum += i
        y_sum += j
        xy_sum += i * j
    x_mean = x_sum / n
    y_mean = y_sum / n
    Lxx = x_square_sum - (1 / n) * (x_sum ** 2)
    Lyy = y_square_sum - (1 / n) * (y_sum ** 2)
    Lxy = xy_sum - (1 / n) * x_sum * y_sum

    b = Lxy / Lxx
    a = y_mean - b * x_mean
    Q = Lyy - b * Lxy
    sigma_square = Q / (n - 2)
    print("x_square_sum, x_sum, y_sum, xy_sum", "\n", x_square_sum, x_sum, y_sum, xy_sum)
    print("x_mean, y_mean = ", x_mean, y_mean)
    print("Lxx = ", Lxx, "Lxy = ", Lxy, "Lyy = ", Lyy)
    if b > 0:
        print("y^ = a^ - b^x = ", a, "+", b, "x")
    else:
        print("y^ = a^ - b^x = ", a, b, "x")
    print("T-test", "-" * 30)
    print("Q = ", Q, "δ^2 = ", sigma_square)
    T = b * (Lxx ** 0.5) / sigma_square ** 0.5
    F = ((b ** 2) * Lxx) / sigma_square
    print("Statistic value(T): ", T)
    print("refuse area: t[0.975](%d)" % (n-2))
    print("F-test", "-" * 30)
    print("Statistic value(F): ", F)
    print("refuse area: f[%f](1, %d)" % (1 - alpha, n - 2))
    print("b^ = ", 5.99 * sigma_square / Lxx, "b^2 = ", b ** 2)


