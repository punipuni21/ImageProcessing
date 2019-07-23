# -*- coding: utf-8 -*-
import cv2
import numpy as np

img = cv2.imread("../imori_noise.jpg")
H, W, C = img.shape

      
imgQ10_2 = img.copy()

imgQ10_2 = cv2.medianBlur(imgQ10_2, ksize=3)

cv2.imwrite("imgQ10_2.jpg", imgQ10_2)