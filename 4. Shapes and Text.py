import cv2
import numpy as np

#we want to generate a black image, so simply make 0's Matrix and It will be black image
black_img= np.zeros((512, 512))

#---------------------------Coloring the Image---------------------------------
colored_img= np.zeros((512, 512,3), np.uint8)   #right now its still black
#now if we want to color it
blue_img= np.zeros((512, 512,3), np.uint8)   
#coloring complete image that's why [:]
blue_img[:]= 255, 0, 0       #now it will become blue

#for Green Color
green_img= np.zeros((512, 512,3), np.uint8) 
green_img[:]= 0, 255, 0

#for Red Image
red_img= np.zeros((512, 512,3), np.uint8) 
red_img[:]= 0, 0, 255
#Coloring Scheme basically follows BGR--> In OpenCV RGB is called as BGR

#--------------------------Creating Shapes on Image-------------------------------
#--------Creating Lines on Image
#we can draw the line using cv2.line()
#line will start from (0,0) and will go until (200,200), the color will be red and thickness will be 3
cv2.line(colored_img, (0,0), (200,200), (0, 0, 255), 3)

#--------Creating Rectangle
#similar to line, starts from (200,200) and ends at (400,400), color is Green and and rectangle will be filled with color
cv2.rectangle(colored_img, (200,200), (300,300),(0, 255, 0), cv2.FILLED)

#-------Creating Circle
#Circle will have Center at (400,400), Radius of Circle will be 20, (255,255,0) is color and 6 is thickness
cv2.circle(colored_img, (400, 400), 20, (255, 255, 0), 6)

#--------------------------Writing on Images-------------------------------------------
#image, text you want to write, (300, 256) is the point where you want to write, font,
# 1 is the Scale (means how big text should be), (0,255,0) is color, 3 is the thickness of text
cv2.putText(colored_img, "OpenCV", (300, 256), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 3)


#showing images
cv2.imshow("Black Image", black_img)
cv2.imshow("Blue Colored Image", blue_img)
cv2.imshow("Green Colored Image", green_img)
cv2.imshow("Red Colored Image", red_img)
cv2.imshow("Image with Line", colored_img)
cv2.waitKey(0)