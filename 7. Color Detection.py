import cv2
import numpy as np
#We will do Color Detection from the Image 

def empty(a):
    pass

img= cv2.imread("Resources/cards.jpg")
#now we will convert this image to HSV image, which is Hue, Satuatration, Value Image that are necessary for 
#color detection
img_HSV= cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

#we have to specify ranges for hue, saturation and value and if it fall in those ranges we will grab that colot
#we want to get red color area but we do not know min and max values for HSV for red color
#so we will use Trackbars that will help us play arround with values to figure it out

#making new window
cv2.namedWindow("TrackBars")
cv2.resizeWindow('TrackBars', 640, 240)   #resizing the trackbar
#creating trackbar
#showing
cv2.imshow("Normal Image", img)
cv2.imshow("HSV Image", img_HSV)

cv2.waitKey(0)