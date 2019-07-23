


import cv2
import numpy as np
img = cv2.imread("../imori.jpg").astype(np.float)

#大津の二値化

r = img[:,:,0].copy()
g = img[:,:,1].copy()
b = img[:,:,2].copy()

H, W, C = img.shape

imgQ4 = 0.2126*r+0.7152*g+0.0722*b
imgQ4 = imgQ2.astype(np.uint8)

max_sigma = 0
max_t = 0

for _t in range(1, 255):
    v0 = imgQ4[np.where(imgQ4 < _t)]
    m0 = np.mean(v0) if len(v0) > 0 else 0.
    w0 = len(v0) / (H * W)
    v1 = imgQ4[np.where(imgQ4 >= _t)]
    m1 = np.mean(v1) if len(v1) > 0 else 0.
    w1 = len(v1) / (H * W)
    sigma = w0 * w1 * ((m0 - m1) ** 2)
    if sigma > max_sigma:
        max_sigma = sigma
        max_t = _t

print("threshold >>", max_t)
th = max_t
imgQ4[imgQ4 < th] = 0
imgQ4[imgQ4 >= th] = 255



cv2.imwrite("imgQ4.jpg", imgQ4)
cv2.imshow("result", imgQ4)
cv2.waitKey(0)
cv2.destroyAllWindows()