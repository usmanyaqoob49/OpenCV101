import cv2

img= cv2.imread("Resources/usman.jpeg")
#printing the shape of our image--->shape of image is represented as (height, width, number of channels)
print("shape of the image: ", img.shape)

#current size--> (800, 800, 3)

#---------------------------Resizing Image-----------------------------------------
#Lets resize the image-->in resize we have to give convntionally (width, height)
img_resized= cv2.resize(img, (600,400))
print("shape of resized image: ", img_resized.shape)

#---------------------------Cropping Image-----------------------------------------
            #image axis are like:
                        #x-axis
#                        ----------->
#                        |
#                        |
#                        |
#                        
#we will just specify the number of pixels in x and y
#       height comes first and then width
img_cropped= img[100:600, 300:700]

#--------------------------------Showing images------------------------------

cv2.imshow("Normal Image", img)
cv2.imshow("Resized Image", img_resized)
cv2.imshow("Cropped Image", img_cropped)
cv2.waitKey(0)
