import cv2 as cv

img = cv.imread('photos/cat.jpg')

cv.imshow('Cat', img)


capture = cv.VideoCapture('videos\\cat.mp4')

while True:
    isTrue, frame = capture.read()
    if not isTrue:
        print("Error: Could not read frame")
        break
    elif cv.waitKey(20) & 0xFF == ord('d'):
        break
    cv.imshow('Video', frame)

capture.release()
cv.destroyAllWindows()
