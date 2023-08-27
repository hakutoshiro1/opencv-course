import cv2 as cv
import numpy as np

blank= np.zeros((500,500,3),dtype='uint8')
cv.imshow('blank',blank)

# paint certain region of images with certain color
# blank[125:375,125:375]= 255,255,255
# cv.imshow('blank-w',blank)

# blank[:]= 255,255,255
# cv.imshow('blank-white',blank)

# 2. Draw a Rectangle
# cv.rectangle(blank,(125,125),(375,375),(0,0,0),thickness=-1)
# cv.imshow('blank-rect',blank)

# cv.rectangle(blank,(0,125),(500,375),(255,255,255),thickness=-1)
# cv.imshow('blank-rect',blank)

# 3. Draw A circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255), thickness=-1)
cv.imshow('Circle', blank)

# 4. Draw a line
cv.line(blank, (100,250), (300,400), (255,255,255), thickness=3)
cv.imshow('Line', blank)



cv.waitKey(0)
if 0xFF== ord('d') :
    blank.release()
    cv.destroyAllWindows()