import cv2 
import sys

src = cv2.imread('building.jpg')
if src is None:
    print("File load failed")
    sys.exit()

dst = cv2.Canny(src, 50, 150)

cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()