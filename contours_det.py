import cv2 as cv
import numpy as np

img=cv.imread('Pics/cats2.png')
cv.imshow('Image',img)

gray_img=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray image',gray_img)

# blur_img=cv.blur(gray_img,(3,3),cv.BORDER_DEFAULT)
# cv.imshow('Blur image',blur_img)

# edge_det=cv.Canny(blur_img,5,175)
# cv.imshow('Egde detected again',edge_det)

ret,thresh=cv.threshold(gray_img,155,255,cv.THRESH_BINARY)
cv.imshow('Threshold',thresh)

contours,hierarchy=cv.findContours(thresh,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} : contours')
blank=np.zeros(img.shape,'uint8')
cv.drawContours(blank,contours,-1,(0,0,255),1)
cv.imshow('Contours',blank)

cv.waitKey(0)