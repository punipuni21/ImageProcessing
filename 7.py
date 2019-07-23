# -*- coding: utf-8 -*-

import cv2
import numpy as np

img = cv2.imread("../imori.jpg")

imgQ7 = img.copy()

H,W,C = img.shape
grid = 8

Nh = int(H/grid)
Nw = int(W/grid)

for y in range(Nh):
    for x in range(Nw):
        for c in range(C):
            imgQ7[grid*y:grid*(y+1),grid*x:grid*(x+1),c]=np.mean(imgQ7[grid*y:grid*(y+1), grid*x:grid*(x+1), c]).astype(np.int)

cv2.imwrite("imgQ7.jpg", imgQ7)

