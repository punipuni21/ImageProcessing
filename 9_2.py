# -*- coding: utf-8 -*-

import cv2
import numpy as np

img = cv2.imread("../imori_noise.jpg")
H, W, C = img.shape

imgQ9_2 = img.copy()
    
imgQ9_2 = cv2.GaussianBlur(imgQ9_2, ksize=(3,3), sigmaX=1.3)
    
cv2.imwrite("imgQ9_2.jpg", imgQ9_2)

