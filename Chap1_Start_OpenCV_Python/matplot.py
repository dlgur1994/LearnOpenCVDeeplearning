import cv2
import matplotlib.pyplot as plt

# Color image
src = cv2.imread('cat.bmp')
dst = cv2.cvtColor(src, cv2.COLOR_BGR2RGB)

plt.axis('off')
plt.imshow(dst)
plt.show()

# Grey image
src = cv2.imread('cat.bmp', cv2.IMREAD_GRAYSCALE)

plt.axis('off')
plt.imshow(src, cmap='gray')
plt.show()