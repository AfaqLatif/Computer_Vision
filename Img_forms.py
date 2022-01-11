import cv2 as cv

img=cv.imread('Pics/1.png')
cv.imshow('Image',img)

gray_img=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray image',gray_img)

blur_img=cv.blur(img,(3,3))
cv.imshow('Blur image',blur_img)

edge_det=cv.Canny(blur_img,0,175)
cv.imshow('Egde detected',edge_det)

edge_det1=cv.Canny(blur_img,125,175)
cv.imshow('Egde detected again',edge_det1)

dil_img=cv.dilate(edge_det1,(3,3),iterations=1)
cv.imshow('Dilated canny image',dil_img)

erod_img=cv.erode(dil_img,(3,3),iterations=1)
cv.imshow('Eroding dilated image',erod_img)

resi_img=cv.resize(erod_img,(800,200),interpolation=cv.INTER_CUBIC)
cv.imshow('Resized image',resi_img)



cv.waitKey(0)