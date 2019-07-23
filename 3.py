# -*- coding: utf-8 -*-

import cv2
import numpy as np
img = cv2.imread("../imori.jpg").astype(np.float)

#二値化

r = img[:,:,0].copy()
g = img[:,:,1].copy()
b = img[:,:,2].copy()

imgQ3 = 0.2126*r+0.7152*g+0.0722*b
imgQ3 = imgQ3.astype(np.uint8)

print(imgQ3.shape)
th = 128
imgQ3[imgQ3 < th] = 0
imgQ3[imgQ3 >= th] = 255

cv2.imwrite("imgQ3.jpg", imgQ3)
cv2.imshow("result", imgQ3)
cv2.waitKey(0)
cv2.destroyAllWindows()