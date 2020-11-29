"""
Function: 
Coding: utf-8
Author: Sun Yuexin
Date:
"""
import cv2
import numpy as np


def hProject(binary):
    h, w = binary.shape
    hprojection = np.zeros(binary.shape, dtype=np.uint8)

    h_h = [0] * h
    for j in range(h):
        for i in range(w):
            if binary[j, i] == 0:
                h_h[j] += 1
    for j in range(h):
        for i in range(h_h[j]):
            hprojection[j, i] = 255
    cv2.imshow("hpro", hprojection)

    return h_h


def vProject(binary):
    h, w = binary.shape
    vprojection = np.zeros(binary.shape, dtype=np.uint8)

    w_w = [0] * w
    for i in range(w):
        for j in range(h):
            if binary[j, i] == 0:
                w_w[i] += 1
    for i in range(w):
        for j in range(w_w[i]):
            vprojection[j, i] = 255
    cv2.imshow("vpro", vprojection)

    return w_w


if __name__ == '__main__':
    img = cv2.imread("sheet_pic.png")
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    ret, th = cv2.threshold(gray, 180, 255, cv2.THRESH_BINARY)

    h, w = th.shape
    h_h = hProject(th)

    start = 0
    h_start, h_end, position = [], [], []

    for i in range(len(h_h)):
        if h_h[i] > 0 and start == 0:
            h_start.append(i)
            start = 1
        if h_h[i] ==0 and start == 1:
            h_end.append(i)
            start = 0
        h_end.append(len(h_h))

    for i in range(len(h_start)):
        cropImg = th[h_start[i]:h_end[i], 0:w]
        if i == 0:
            cv2.imshow('cropimg', cropImg)
            cv2.imwrite('words_cropimg.jpg', cropImg)
        w_w = vProject(cropImg)

        wstart, wend, w_start, w_end = 0, 0, 0, 0
        for j in range(len(w_w)):
            if w_w[j] > 0 and wstart == 0:
                w_start = j
                wstart = 1
                wend = 0
            if w_w[j] ==0 and wstart == 1:
                w_end = j
                wstart = 0
                wend = 1

            if wend == 1:
                position.append([w_start, h_start[i], w_end, h_end[i]])
                wend = 0

    for p in position:
        cv2.rectangle(img, (p[0], p[1]), (p[2], p[3]), (0, 0, 255), 2)

    cv2.imshow('image', img)
    cv2.imshow('th', th)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
