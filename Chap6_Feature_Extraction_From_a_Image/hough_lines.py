import cv2
import sys
import numpy as np

src = cv2.imread('building.jpg', cv2.IMREAD_GRAYSCALE)
if src is None:
    print('File load failed')
    sys.exit()

edge = cv2.Canny(src, 50, 150)
lines = cv2.HoughLinesP(edge, 1.0, float(np.pi/180), 160, minLineLength=50, maxLineGap=5)
dst = cv2.cvtColor(edge, cv2.COLOR_GRAY2BGR)

if len(lines) != 0:
    for i in range(len(lines)):
        x1, y1, x2, y2 = lines[i][0]
        cv2.line(dst, (x1,y1), (x2,y2), (0,0,255), 2, cv2.LINE_AA)

cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()
        