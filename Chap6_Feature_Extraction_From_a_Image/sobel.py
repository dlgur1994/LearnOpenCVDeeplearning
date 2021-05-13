import cv2
import sys

src = cv2.imread('lenna.bmp', cv2.IMREAD_GRAYSCALE)
if src is None:
    print("File load failed")
    sys.exit()

dx = cv2.Sobel(src, -1, 1, 0)
dy = cv2.Sobel(src, -1, 0, 1)

cv2.imshow('dx', dx)
cv2.imshow('dy', dy)
cv2.waitKey()
cv2.destroyAllWindows()