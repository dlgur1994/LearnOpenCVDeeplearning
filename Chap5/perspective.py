import cv2
import numpy as np

src = cv2.imread('namecard.jpg')
w, h = 720, 400
src_quad = np.array([[325, 307], [760,369], [718,611], [231,515]], dtype=np.float32)
dst_quad = np.array([[0,0], [w-1,0], [w-1,h-1], [0,h-1]], dtype=np.float32)
mat = cv2.getPerspectiveTransform(src_quad, dst_quad)
dst = cv2.warpPerspective(src, mat, (w,h))

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()