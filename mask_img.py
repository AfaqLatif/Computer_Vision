import cv2 as cv
import numpy as np

img=cv.imread('Pics/cats3.JPG')
cv.imshow('Image',img)
print(img.shape[:2])

res_img=cv.resize(img,(600,600),interpolation=cv.INTER_AREA)
cv.imshow('Resized image',res_img)

blank=np.zeros(res_img.shape[:2],'uint8')
cv.imshow('Blank image',blank)

cir_blank=cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),200,255,-1)
cv.imshow('Circle on image',cir_blank)

mask=cv.bitwise_and(res_img,res_img,mask=cir_blank)
cv.imshow('Masked image',mask)

cv.waitKey(0)