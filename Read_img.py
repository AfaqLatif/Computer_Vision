import cv2 as cv

img=cv.imread('Pics/1.png')
cv.imshow('Image',img)

def rescale(frame,scale=0.75):
    w=int(frame.shape[1]*scale)
    h=int(frame.shape[0]*scale)
    dim=(w,h)
    return cv.resize(frame,dim,interpolation=cv.INTER_AREA)

# iterpolation=cv.INTER_AREA ( for reduction in size )
# iterpolation=cv.INTER_LINEAR ( for enlargement in size )
# iterpolation=cv.INTER_CUBIC ( for enlargement in size )
# It is applicable for images and videos but not for live videos
img_resized=rescale(img)
cv.imshow('Resized Image',img_resized)

cv.waitKey(0)


# vid_cap=cv.VideoCapture('cute rabbit.mp4')

# while True:
#     istrue, frame=vid_cap.read()
#     cv.imshow('Video',frame)
#     #if cv.waitKey(20) & 0×FF==ord('d'):
#     #    break
    
# cv.waitKey(0)
# vid_cap.release()
# cv.destroyAllWindows()