import pytesseract
import cv2 as cv

pytesseract.pytesseract.tesseract_cmd=(r"C:\Program Files\Tesseract-OCR\tesseract.exe")

img=cv.imread('Pics/a1.png')
cv.imshow('Image',img)
#print(img.shape)

gray_img=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray image',gray_img)

thresh,binr_img=cv.threshold(gray_img,205,245,cv.THRESH_BINARY)
cv.imshow('Binarize image',binr_img)

# dil_img=cv.dilate(binr_img,(3,3),iterations=1)
# cv.imshow('Dilated image',dil_img)

# erod_img=cv.erode(binr_img,(1,1),iterations=1)
# cv.imshow('Eroded image',erod_img)

def noise_rem(image):
    image=cv.dilate(image,(1,1),iterations=1)
    image=cv.erode(image,(1,1),iterations=1)
    image=cv.morphologyEx(image,cv.MORPH_CLOSE,(1,1))
    image=cv.medianBlur(image,3)
    return (image)

noise_rem_img=noise_rem(binr_img)
cv.imshow('Noised removed image',noise_rem_img)

text=pytesseract.image_to_string(noise_rem_img,lang='ara')
print(text)

cv.waitKey(0)