import cv2 as cv
import numpy as np

flag = 0
cap = cv.VideoCapture(0)
while(1):
    # Take each frame
    _, frame = cap.read()
    # Convert BGR to HSV
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    lower_red1 = np.array([140,71,107])
    upper_red1 = np.array([179,255,212])
    lower_red2 = np.array([0,71,107])
    upper_red2 = np.array([10,255,212])
    # Threshold the HSV image to get only red colors
    mask = cv.inRange(hsv, lower_red1, upper_red1)
    mask2 = cv.inRange(hsv, lower_red2, upper_red2)
    mask3 = cv.bitwise_or(mask, mask2)
    blur = cv.medianBlur(mask3,5)
    blur2 = cv.blur(blur,(5,5))
    edges = cv.Canny(blur2, 100, 200)
    contours, _ = cv.findContours(blur2, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    if flag == 1 and len(contours) > 0:
        cnt = contours[0]
        x,y,w,h = cv.boundingRect(cnt)
        cv.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
        print(x , y, w, h)
    #cv.rectangle(frame,(0,0),(50,50),(0,0,255),5)
    cv.imshow('frame',frame)
    cv.imshow('mask',mask)
    cv.imshow('mask2',mask2)
    cv.imshow('mask3',mask3)
    cv.imshow('blur',blur)
    cv.imshow('blur2', blur2)
    cv.imshow('edges', edges)
    #cv.imshow('res',res)
    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break
    if flag == 0:
        flag = 1
cv.destroyAllWindows()