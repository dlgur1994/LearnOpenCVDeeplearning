import cv2
import sys
import numpy as np

src = cv2.imread('lenna.bmp', cv2.IMREAD_GRAYSCALE)
if src is None:
    print("File load failed")
    sys.exit()

# change the return type of dx and dy to float in order to put them in cv2.magnitude as float
dx = cv2.Sobel(src,cv2.CV_32F,1,0)
dy = cv2.Sobel(src,cv2.CV_32F,0,1)

mag = cv2.magnitude(dx, dy)
mag = np.clip(mag, 0, 255).astype(np.uint8) # change float type back to uint8
edge = np.zeros(src.shape[:2], dtype=np.uint8)
edge[mag>120] = 255

cv2.imshow('mag', mag)
cv2.imshow('edge', edge)
cv2.waitKey()
cv2.destroyAllWindows()