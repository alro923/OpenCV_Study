import cv2
import numpy as np

img = cv2.imread('img/pizza01.jpg')

# gaussian kernel 직접생성해서 blurring
k1 = np.array([[1, 2, 1],
               [2, 4, 2],
               [1, 2, 1]]) * (1/16)

blur1 = cv2.filter2D(img, -1, k1)

# gaussian kernerl을 api로 얻고 blurring

k2 = cv2.getGaussianKernel(3, 0)
blur2 = cv2.filter2D(img, -1, k2*k2.T)

# gaussian blur api로 blurring
blur3 = cv2.GaussianBlur(img, (3, 3), 0)

print('k1:', k1)
print('k2:', k2*k2.T)

gaussian_merged = np.hstack((img, blur1, blur2, blur3))

cv2.imshow('gaussian blur', gaussian_merged)
cv2.waitKey(0)
cv2.destroyAllWindows()