import cv2 as cv

# img=cv.imread('Photos/cat_large.jpg')

# cv.imshow('cat',img)

# cv.waitKey(0)
capture= cv.VideoCapture('Videos/dog.mp4')
# capture= cv.VideoCapture(0)
while True:
    isTrue,frame=capture.read()
    cv.imshow('dog',frame)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()