import cv2
import numpy as np

img= cv2.imread("Resources/cards.jpg")
print(img.shape)
resized= cv2.resize(img, (360, 500))
# stacking/Joining the image horizontally--> we will use numpy's hstack function
img_hor= np.hstack((resized, resized))

# stacking/joining the image vertically
img_vert= np.vstack((img, img))

#Note: 
#       Main Issue with using numpy stack to stack iamges is that it only stack images with same number of
#       channels that means we can not stack grayscale image with RGB image, because as we are using numpy
#       so dimensions will not match.
#showing
cv2.imshow("Normal Image", img)
cv2.imshow("Resized Iamge", resized)
cv2.imshow("Horizontally Stacked Resized Image", img_hor)
cv2.imshow("Vertical Stacked Image", img_vert)
cv2.waitKey(0)