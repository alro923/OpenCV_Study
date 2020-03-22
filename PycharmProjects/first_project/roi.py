import cv2
import numpy as np

# 마우스로 영역 지정해서 저장
isDragging = False
x0, y0, w, h = -1,-1,-1,-1
blue, rdd = (255,0,0) , (0,0,255)

def onMouse(event, x,y,flags,param):
    global isDragging, x0, y0, img
    if event == cv2.EVENT_LBUTTONDOWN:
        isDragging = True
        x0 = x
        y0 = y
    elif event == cv2.EVENT_MOUSEMOVE:
        if isDragging:
            img_draw = img.copy()
            cv2.rectangle(img_draw, (x0, y0), (x, y), blue, 2)
            cv2.imshow('img', img_draw)
    elif event == cv2.EVENT_LBUTTONUP:
        if isDragging:
            isDragging = False
            w = x - x0
            h = y - y0
            print("x:%d, y:%d, w:%d, h:%d" % (x0, y0, w, h))
            if w > 0 and h > 0:
                img_draw = img.copy()
                cv2.rectangle(img_draw, (x0, y0), (x, y), (255, 0, 0), 3)
                cv2.imshow('img', img_draw)
                roi = img[y0:y0+h, x0:x0+w]
                cv2.imshow('cropped', roi)
                cv2.moveWindow('cropped', 0, 0)
                cv2.imwrite('./cropped.jpg', roi)
                print("cropped.")
            else:
                cv2.imshow('img', img)
                print("Drag from left top to right bottom.")

img = cv2.imread('img/pizza01.jpg')
cv2.imshow('img', img)
cv2.setMouseCallback('img', onMouse)
cv2.waitKey(0)
cv2.destroyAllWindows()
