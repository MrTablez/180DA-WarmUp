import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)
while(1):
 # Take each frame
 _, frame = cap.read()
 # Convert BGR to HSV
 hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
 lower_green = np.array([40,51,51])
 upper_green = np.array([85,230,153])
 # Threshold the HSV image to get only green colors
 mask = cv.inRange(hsv, lower_green, upper_green)
 blur = cv.medianBlur(mask,5)
 blur2 = cv.blur(blur,(5,5))
 cv.imshow('frame',frame)
 cv.imshow('mask',mask)
 cv.imshow('blur',blur)
 cv.imshow('blur2', blur2)
 #cv.imshow('res',res)
 k = cv.waitKey(5) & 0xFF
 if k == 27:
    break
cv.destroyAllWindows()