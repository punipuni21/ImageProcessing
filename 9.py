# -*- coding: utf-8 -*-



import cv2
import numpy as np

img = cv2.imread("../imori_noise.jpg")
H, W, C = img.shape


#フィルタの大きさ
K_siz = 3
sigma = 1.3

#パディングを行う
pad = K_siz // 2
imgQ9 = np.zeros((H+pad*2,W+pad*2,C),dtype=np.float)
imgQ9[pad:pad+H, pad:pad+W] = img.copy().astype(np.float)


#カーネルを設定
K = np.zeros((K_siz,K_siz),dtype=np.float)
for x in range(-pad, -pad+K_siz):
    
    for y in range(-pad, -pad+K_siz):
        K[y+pad, x+pad] = np.exp( -(x**2 + y**2) / (2* (sigma**2)))
K /= (sigma * np.sqrt(2 * np.pi))
K /= K.sum()

tmp = imgQ9.copy()

for y in range(H):
    for x in range(W):
        for c in range(C):
            imgQ9[pad+y, pad+x, c] = np.sum(K * tmp[y:y+K_siz, x:x+K_siz, c])

imgQ9 = imgQ9[pad:pad+H, pad:pad+W].astype(np.uint8)

cv2.imwrite("imgQ9.jpg", imgQ9)