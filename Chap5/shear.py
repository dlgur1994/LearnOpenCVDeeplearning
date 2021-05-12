import cv2
import numpy as np

src = cv2.imread('tekapo.bmp')
aff = np.array([[1,0.5,0],[0,1,0]], dtype=np.float32)
h, w = src.shape[:2]
dst = cv2.warpAffine(src, aff, (int(w+0.5*h),h))

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()