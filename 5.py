# -*- coding: utf-8 -*-

import cv2
import numpy as np

img = cv2.imread("../imori.jpg")

#HSV変換
#画像はBGRの順番

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)


hsv[:,:,0]+=180
hsv[:,:,0]%=360

cv2.imwrite("hsv.jpg", hsv)

rgb = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
cv2.imwrite("rgb.jpg", rgb)

