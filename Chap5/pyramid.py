import cv2

src = cv2.imread('cat.bmp')
cpy = src.copy()
cv2.rectangle(cpy, (250,120,200,200), (0,0,255),2)
cv2.imshow('src', cpy)
cv2.waitKey()

for i in range(1,4):
    cpy = cv2.pyrDown(cpy)
    cv2.rectangle(cpy, (250,120,200,200), (0,0,255), 2, shift=i)
    cv2.imshow('cpy', cpy)
    cv2.waitKey()

cv2.destroyAllWindows()