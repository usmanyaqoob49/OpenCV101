import cv2
import numpy as np
#importing the image
img= cv2.imread('Resources/usman.jpeg')

###########################Gray Scale image###################
#We will use cvtColor() function
img_Gray= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


############################Blurring the image##################
#we will use GaussianBlur() function----> (7,7) is kernel size and it should be odd number, 0 is sigmax

#kernel size determine extent of Blurring-->more high odd number, more blur in the image
#sigmax is spread of gaussian kernel and 0 means calculate it accroding to kernel size
blur_image= cv2.GaussianBlur(img_Gray, (13,13), 0)

############################Edges Detection in the Image###################

# (100,100) figure out number of edges it will detect, lower the numbers, more edges will be detected
img_edges= cv2.Canny(img_Gray, 100, 100)

###########################Image Dilation/Edges Thickness#########################
#so now we will make the edges of the image thick
                                    #we made kernel of all ones --> means more white color for edges
                                    #iterations tell us how many times to iterate kernel -->means how much tickness
dilated_img= cv2.dilate(img_edges, np.ones((5,5), np.uint8), iterations= 1)


######################Image Erodtion/Edges Thinner################################
img_eroded= cv2.erode(dilated_img, np.ones((5,5), np.uint8), iterations= 1)


#showing the normal image
cv2.imshow("Normal Image", img)
#adding delay
cv2.waitKey(0)

#showing the gray scale image
cv2.imshow("Gray Scale Image", img_Gray)
cv2.waitKey(0)

#showing the blurred image
cv2.imshow("Blurred Image", blur_image)
cv2.waitKey(0)

#shwoing image edges
cv2.imshow("Image Edges", img_edges)
cv2.waitKey(0)


#shwoing image dilated edges
cv2.imshow("Image Dialted", dilated_img)
cv2.waitKey(0)

#shwoing image with eroded/thinner edges
cv2.imshow("Image Eroded", img_eroded)
cv2.waitKey(0)