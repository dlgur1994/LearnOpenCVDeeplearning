import cv2
import sys

src = cv2.imread('cat.bmp')
if src is None:
    print('Image load failed')
    sys.exit()

cv2.imshow('src', src)
cv2.waitKey()
cv2.destroyAllWindows()