# -*- coding: utf-8 -*-

import cv2
import numpy as np

img = cv2.imread("../imori_noise.jpg")
H, W, C = img.shape


#フィルタの大きさ
K_siz = 3

#パディングを行う
pad = K_siz // 2
imgQ10 = np.zeros((H+pad*2,W+pad*2,C),dtype=np.float)
imgQ10[pad:pad+H, pad:pad+W] = img.copy().astype(np.float)


tmp = imgQ10.copy()

for y in range(H):
    for x in range(W):
        for c in range(C):
            imgQ10[pad+y, pad+x, c] = np.median(tmp[y:y+K_siz, x:x+K_siz, c])

imgQ10 = imgQ10[pad:pad+H, pad:pad+W].astype(np.uint8)

cv2.imwrite("imgQ10.jpg", imgQ10)