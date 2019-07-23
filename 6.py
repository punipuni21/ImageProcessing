# -*- coding: utf-8 -*-

import cv2
import numpy as np

img = cv2.imread("../imori.jpg")

imgQ6 = img.copy()

imgQ6 = imgQ6 // 64 * 64 + 32

cv2.imwrite("imgQ6.jpg", imgQ6)
