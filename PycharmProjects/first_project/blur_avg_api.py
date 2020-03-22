import cv2
import numpy as np

file_name = 'img/pizza01.jpg'
img = cv2.imread(file_name)

blur1 = cv2.blur(img, (10,10))
blur2 = cv2.boxFilter(img, -1, (10, 10))

merged = np.hstack( (img, blur1, blur2))
cv2.imshow('blur', merged)
cv2.waitKey(0)
cv2.destroyAllWindows()