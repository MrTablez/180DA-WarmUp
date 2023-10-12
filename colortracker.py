import cv2 as cv
import numpy as np
cap = cv.VideoCapture(0)
while(1):
 # Take each frame
 _, frame = cap.read()
 # Convert BGR to HSV
 hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
 # define range of blue color in HSV
 #pink = np.uint8([[[33,27,128]]])
 #hsv_pink = cv.cvtColor(pink,cv.COLOR_BGR2HSV)
 #print( hsv_pink )
 lower_blue = np.array([168,100,100])
 upper_blue = np.array([188,255,255])
 # Threshold the HSV image to get only blue colors
 mask = cv.inRange(hsv, lower_blue, upper_blue)
 # Bitwise-AND mask and original image
 res = cv.bitwise_and(frame,frame, mask= mask)
 cv.imshow('frame',frame)
 cv.imshow('mask',mask)
 cv.imshow('res',res)
 k = cv.waitKey(5) & 0xFF
 if k == 27:
    break
cv.destroyAllWindows()