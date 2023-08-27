import cv2 as cv
def rescaleFrame(frame,scale=0.75):
    width,height=int(frame.shape[1]*scale),int(frame.shape[0]*scale)
    dimensions=(width,height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)


# capture= cv.VideoCapture('Videos/dog.mp4')
capture= cv.VideoCapture(0)
while True:
    isTrue,frame=capture.read()
    cv.imshow('dog',frame)
    cv.imshow('rescaled',rescaleFrame(frame,0.5))
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()