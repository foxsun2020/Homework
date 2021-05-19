"""
-*- coding: utf-8 -*-
@Author  : M090120303 Sun Yuexin
@Time    : 2021/5/15 16:29
@Function: newton_method
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def fun(x):
    return 100 * (x[0] ** 2 - x[1]) ** 2 + (x[1] - 1) ** 2  # book
    # return 2 * x[0] ** 2 + x[1] ** 2 + 2 * x[0] * x[1] + x[0] - x[1]  # task-1
    # return (3 / 2) * x[0] ** 2 + (1 / 2) * x[1] * 2 - x[0] * x[1] - x[0]  # task-2


def gfun(x):
    # book
    gx_1 = 400 * x[0] * (x[0] ** 2 - x[1]) + 2 * (x[1] - 1)
    gx_2 = -200 * (x[0] ** 2 - x[1])

    # task-1
    # gx_1 = 4 * x[0] + 2 * x[1] + 1
    # gx_2 = 2 * x[1] + 2 * x[0] - 1

    # task - 2
    # gx_1 = 2 * x[0] - x[1] - 1
    # gx_2 = x[1] - x[0]
    return [gx_1, gx_2]


def hess(x):
    # book
    row_1 = [1200 * x[0] ** 2 - 400 * x[1] + 2, -400 * x[0]]
    row_2 = [-400 * x[0], 200]

    # task-1
    # row_1 = [4, 2]
    # row_2 = [2, 2]

    # task-2
    # row_1 = [2, -1]
    # row_2 = [-1, 1]

    return [row_1, row_2]


def show(objv, px, py, pz):
    fig = plt.figure()
    ax = Axes3D(fig)
    ax_x = np.arange(-15, 15, 1)
    ax_y = np.arange(-50, 50, 1)
    x, y = np.meshgrid(ax_x, ax_y)
    z = fun([x, y])
    ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap='rainbow')
    if objv is not None:
        z1 = fun(objv)
        ax.plot(objv[0], objv[1], z1, marker='o', color='#ff0000')
        ax.scatter3D(px, py, pz, c=pz, cmap='hsv')

    plt.show()

class Method:
    def __init__(self):
        self.maxk = 150
        self.rho = 0.55
        self.sigma = 0.4
        self.epsilon = 1e-5
        self.tau = 0.0

    def process(self, x, gk, dk, k):
        m, mk = 0, 0
        while m < 20:
            d1 = x + np.power(self.rho, m) * dk
            d2 = self.sigma * np.power(self.rho, m) * sum(gk * dk)
            if fun(d1) < fun(x) + d2:
                mk = m
                break
            m += 1
        x += np.power(self.rho, mk) * dk
        print(f"No.{k}:")
        print(f"---point: {x}")
        print(f"---learning rate: {np.power(self.rho, mk)}")
        print(f"---step: {np.power(self.rho, mk) * dk}")
        print(f"---val: {fun(x)}")
        global x_points, y_points, z_points
        x_points = np.append(x_points, x[0])
        y_points = np.append(y_points, x[1])
        z_points = np.append(z_points, fun(x))
        return x

    def revisenm(self, x0):
        k = 0
        while k < self.maxk:
            gk = gfun(x0)
            muk = np.power(np.linalg.norm(gk, ord=2), (1 + self.tau))
            hk = hess(x0)
            ak = hk + muk * np.ones([2, 2])
            dk = -1.0 * np.linalg.solve(ak, gk)
            if np.linalg.norm(dk, ord=2) < self.epsilon:
                break
            x0 = self.process(x0, gk, dk, k)
            k += 1
        return [x0, fun(x0)]

    def dampnm(self, x0):
        k = 0
        while k < self.maxk:
            gk = gfun(x0)
            hk = hess(x0)
            dk = -1.0 * np.linalg.solve(hk, gk)
            if np.linalg.norm(dk, ord=2) < self.epsilon:
                break
            x0 = self.process(x0, gk, dk, k)
            k += 1
        return [x0, fun(x0)]

    def grad(self, x0):
        k = 0
        while k < self.maxk:
            gk = gfun(x0)
            dk = -1 * gk
            if np.linalg.norm(dk, ord=2) < self.epsilon:
                break
            x0 = self.process(x0, gk, dk, k)
            k += 1
        return [x0, fun(x0)]


if __name__ == "__main__":
    x_points, y_points, z_points = np.array([]), np.array([]), np.array([])
    sues = Method()
    # min_val = sues.dampnm([10, -10])  # 阻尼牛顿法
    min_val = sues.revisenm([10, 10])  # 修正牛顿法
    # min_val = sues.grad([-1, 1])  # 最速下降法
    print("-" * 30)
    print("x_1: %.2f".center(30) % min_val[0][0])
    print("x_2: %.2f".center(30) % min_val[0][1])
    print("min_val: %.2f".center(30) % min_val[1])
    print("-" * 30)
    show(min_val[0], x_points, y_points, z_points)
