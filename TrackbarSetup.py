def trackbar(pos):
  global threshold1
  global threshold2
  threshold1 = cv.getTrackbarPos('threshold1', 'edges')
  threshold2 = cv.getTrackbarPos('threshold2', 'edges')
threshold1 = 255/3
threshold2 = 255
cap = cv.VideoCapture(0)
cv.namedWindow('edges')
cv.createTrackbar('threshold1', 'edges', 0, 999, trackbar)
cv.createTrackbar('threshold2', 'edges', 0, 999, trackbar)