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
 contours, _ = cv.findContours(edges, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
 contours_poly = [None]*len(contours)
 boundRect = [None]*len(contours)
 for i, c in enumerate(contours):
  contours_poly[i] = cv.approxPolyDP(c, 3, True)
  boundRect[i] = cv.boundingRect(contours_poly[i])
 drawing = np.zeros((edges.shape[0], edges.shape[1], 3), dtype=np.uint8)
 for i in range(len(contours)):
  color = (rng.randint(0,256), rng.randint(0,256), rng.randint(0,256))
  cv.drawContours(drawing, contours_poly, i, color)
  cv.rectangle(drawing, (int(boundRect[i][0]), int(boundRect[i][1])), (int(boundRect[i][0]+boundRect[i][2]), int(boundRect[i][1]+boundRect[i][3])), color, 2)
  cv.imshow('Contours', drawing)
 # Bitwise-AND mask and original image
 #res = cv.bitwise_and(frame,frame, mask= mask)
 cv.imshow('frame',frame)
 cv.imshow('mask',mask)
 cv.imshow('edges',edges)
 #cv.imshow('res',res)
 k = cv.waitKey(5) & 0xFF
 if k == 27:
    break
cv.destroyAllWindows()