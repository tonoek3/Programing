import cv2
import numpy as np
img1 = cv2.imread("images.jpeg",0)

cv2.imshow("images.jpeg",img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
