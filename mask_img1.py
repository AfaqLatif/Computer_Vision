import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img=cv.imread('Pics/cats3_1.JPG')
cv.imshow('Image',img)
print(img.shape[:2])

res_img=cv.resize(img,(650,600),interpolation=cv.INTER_AREA)
cv.imshow('Resized image',res_img)

blank=np.zeros(res_img.shape[:2],'uint8')
cv.imshow('Blank image',blank)

cir_blank=cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),200,255,-1)
cv.imshow('Circle on image',cir_blank)

mask_img=cv.bitwise_and(res_img,res_img,mask=cir_blank)
cv.imshow('Masked image',mask_img)

plt.figure()
plt.title("Histogram of masked image")
plt.xlabel("Pixel bins")
plt.ylabel("No. of pixels")
col=['b','g','r']
for i,c in enumerate(col):
    hist=cv.calcHist([res_img],[i],cir_blank,[256],[0,256])
    plt.plot(hist,color=c)
    plt.xlim([0,256])

plt.show()

cv.waitKey(0)