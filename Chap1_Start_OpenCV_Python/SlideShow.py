import glob
import sys
import cv2

imgs = glob.glob('./images/*.jpg')
if len(imgs) == 0:
    print("File load failed")
    sys.exit()

i = 0
while True:
    src = cv2.imread(imgs[i])
    cv2.imshow('src', src)
    if cv2.waitKey(1000) == 27:
        break
    
    i += 1
    if i == len(imgs):
        i = 0
        
cv2.destroyAllWindows()