import cv2 as cv
import numpy as np

img = cv.imread('photos/cat.jpg')

blank = np.zeros((img.shape[0], img.shape[1], 3))
# For all pixels
blank[:] = 255,0,0
# For certain pixels
blank[200:300, 200:300] = 0,0,255

# For Rectangles
cv.rectangle(blank, (0,0), (250,250), (255, 255, 255), thickness=-1) # or thickness = cv.FILLED

# For circles
cv.circle(blank, (250, 250), 100, (0, 255, 255), thickness=2)

# For Lines
cv.line(blank, (0,0), (250,250), (100, 200, 0), thickness=2)

# For text
cv.putText(blank, "Hello, World", (100, 100), fontFace=cv.FONT_HERSHEY_COMPLEX_SMALL, fontScale=1.0, color=(0, 100, 0))
cv.imshow("Blank", blank)


cv.waitKey(0)