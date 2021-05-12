import cv2

src = cv2.imread('tekapo.bmp')
h, w = src.shape[:2]
aff = cv2.getRotationMatrix2D((w/2,h/2), 20, 1)
dst = cv2.warpAffine(src, aff, (0,0))

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()