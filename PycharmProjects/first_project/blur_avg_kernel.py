import cv2
import numpy as np

img = cv2.imread('img/pizza01.jpg')
# 5x5 average filter kernel
kernel = np.array([[0.04, 0.04, 0.04, 0.04, 0.04],
                    [0.04, 0.04, 0.04, 0.04, 0.04],
                    [0.04, 0.04, 0.04, 0.04, 0.04],
                    [0.04, 0.04, 0.04, 0.04, 0.04],
                    [0.04, 0.04, 0.04, 0.04, 0.04]])

kernel = np.ones((5, 5))/5**2

blurred = cv2.filter2D(img, -1, kernel)

cv2.imshow('origin', img)
cv2.imshow('avg', blurred)
cv2.waitKey()
cv2.destroyAllWindows()
