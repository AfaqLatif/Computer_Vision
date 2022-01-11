import pytesseract
import cv2 as cv

pytesseract.pytesseract.tesseract_cmd=(r"C:\Program Files\Tesseract-OCR\tesseract.exe")

img=cv.imread('Pics/a1.png')
cv.imshow('Image',img)
#print(img.shape)

gray_img=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray image',gray_img)

# resi_img=cv.resize(img,(600,150),interpolation=cv.INTER_CUBIC)
# cv.imshow('Resized image',resi_img)
# print(resi_img.shape)

text=pytesseract.image_to_string(gray_img,lang='ara')
print(text)

cv.waitKey(0)