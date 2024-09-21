import cv2 as cv

img = cv.imread("photos/cat.jpg")

cv.imshow('cat', img)

def rescale(img, scale = 0.75):
    height, width = img.shape[0], img.shape[1]
    new_height = int(height * scale)
    new_width = int(width * scale)
    dimensions = (new_height, new_width)

    return cv.resize(img, dimensions, interpolation=cv.INTER_AREA)

new_img = rescale(img)

cv.imshow('Scaled img', new_img)

cv.waitKey(0)

capture = cv.VideoCapture("videos/cat.mp4")

#For live videos only
def changeRes(height, width):
    capture.set(3, width)
    capture.set(4, height)

while True:
    isTrue, frame = capture.read()
    new_frame = rescale(frame)
    cv.imshow('Cat', new_frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break;