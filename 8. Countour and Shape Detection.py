import cv2
import numpy as np

#we will Detect the Shapes in the Image.
#firstly defining function for getting contours
def get_contours(img):
    #what we want is to extract the extreme outer contours-->that is why we will use cv2.RETR_EXTERNAL
    #and as we want all the Contours so we will do cv2.CHAIN_APPROX_NONE
    contours, hierarchy= cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        #we will find the area of contour 
        area= cv2.contourArea(cnt)
        print(area)
        cv2.drawContours(img_copy, cnt, -1, (255, 0, 0), 5)

img= cv2.imread('Resources/shapes.jpg')

#making copy
img_copy= img.copy()

resized= cv2.resize(img, (900,600))
#preprocessing the image
gray_scale_img= cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
#blurring
blurred_img= cv2.GaussianBlur(gray_scale_img, (7,7), 1)
#now finding edges in our image
canny_img=  cv2.Canny(blurred_img, 50, 50)


#calling function
get_contours(canny_img)
cv2.imshow('Resized Photo', resized)
cv2.imshow('Gray Scale', gray_scale_img)
cv2.imshow('Blurred Image', blurred_img)
cv2.imshow('Edges', canny_img)
cv2.imshow('Contour Draws', img_copy)
cv2.waitKey(0)