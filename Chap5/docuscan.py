import cv2
import sys

# def drawROI(img, corners):

# def onMouse(event, x, y, flags, param):

# 입력 이미지 불러오기
src = cv2.imread('scanned.jpg')
if src is None:
    print("Image load failed")
    sys.exit()

# 입력 영상 크기 및 출력 영상 크기
h, w = src.shape[:2]
dw = 500
dh = round(dw*297/210)

# 모서리 점들의 좌표, 드래그 상태 여부

# 모서리점, 사각형 그리기

# 투시 변환

# 결과 영상 출력
cv2.imshow('src', src)
cv2.waitKey()
cv2.destroyAllWindows()
