import cv2 as cv
import numpy as np

blank_img=np.zeros((400,400,3),dtype='uint8')
cv.imshow('Blank image',blank_img)

# Colored image
# blank_img[:]=128,128,110
# cv.imshow('Colored image',blank_img)

# Draw rectangle on a shape
cv.rectangle(blank_img,(0,0),(200,200),(0,255,0),thickness=1)    # pt1=origin/start & pt2=end
cv.imshow('Rectangle above shape',blank_img)

# Draw circle above shape
cv.circle(blank_img,(200,200),100,(255,255,0),thickness=1)
cv.imshow('Circled image',blank_img)

# Draw a line on shape
cv.line(blank_img,(100,50),(200,200),(255,255,255),thickness=2)
cv.imshow('Lined image',blank_img)

# Write text on image
cv.putText(blank_img,'65',(140,190),cv.FONT_HERSHEY_SIMPLEX,1.0,(255,255,255),thickness=1)
cv.putText(blank_img,'Geometric Concepts',(50,350),cv.FONT_HERSHEY_DUPLEX,1.0,(255,255,255),thickness=2)
cv.imshow('Texted image',blank_img)

cv.waitKey(0)