import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img=cv.imread('Pics/girls1.JPG')
cv.imshow('Image',img)
#print(img.shape[:2])

gray_img=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray Image', gray_img)

haar_cascade=cv.CascadeClassifier('Haar_cascade_face_dect.xml')
detc_face=haar_cascade.detectMultiScale(gray_img,scaleFactor=1.1,minNeighbors=5)
print(f'Faces found : {len(detc_face)}')
for (x,y,w,h) in detc_face:
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=2)

cv.imshow('Deteced faces',img)

cv.waitKey(0)

# ScaleFactor must greater then 1.