# -*- coding: utf-8 -*-


import cv2
import numpy as np
img = cv2.imread("../imori.jpg").astype(np.float)

#グレースケール化

r = img[:,:,0].copy()
g = img[:,:,1].copy()
b = img[:,:,2].copy()

imgQ2 = 0.2126*r+0.7152*g+0.0722*b
imgQ2 = imgQ2.astype(np.uint8)

cv2.imwrite("imgQ2.jpg", imgQ2)
cv2.imshow("result", imgQ2)
cv2.waitKey(0)
cv2.destroyAllWindows()