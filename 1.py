# -*- coding: utf-8 -*-

import cv2
import numpy as np

#チャネル入れ替え

img = cv2.imread("../imori.jpg").astype(np.float)

imgQ1 = img.copy()
imgQ1 = imgQ1[:,:,(2,1,0)]
imgQ1 = imgQ1.astype(np.uint8)
cv2.imwrite("imgQ1.jpg", imgQ1)
cv2.imshow("result", imgQ1)
cv2.waitKey(0)
cv2.destroyAllWindows()