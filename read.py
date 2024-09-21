import cv2 as cv

img = cv.imread('photos/cat.jpeg')

cv.imshow('Cat', img)

cv.waitKey(1)