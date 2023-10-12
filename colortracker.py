import cv2 as cv
import numpy as np
import random as rng

cap = cv.VideoCapture(0)
while(1):
 # Take each frame
 _, frame = cap.read()
 # Convert BGR to HSV
 hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
 lower_blue = np.array([158,100,100])
 upper_blue = np.array([198,255,255])
 # Threshold the HSV image to get only blue colors
 mask = cv.inRange(hsv, lower_blue, upper_blue)
 edges = cv.Canny(mask, 0, 999)
 #cnt = cv.findContours(edges, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
 contours,hierarchy = cv.findContours(edges, 1, 2)
 cnt = contours[0]
 x,y,w,h = cv.boundingRect(cnt)
 cv.rectangle(edges,(x,y),(x+w,y+h),(0,255,0),2)
 # Bitwise-AND mask and original image
 #res = cv.bitwise_and(frame,frame, mask= mask)
 cv.imshow('frame',frame)
 cv.imshow('mask',mask)
 cv.imshow('edges',edges)
 cv.imshow('contours',contours)
 #cv.imshow('res',res)
 k = cv.waitKey(5) & 0xFF
 if k == 27:
    break
cv.destroyAllWindows()