import cv2
import numpy as np

#Warp Perspective basically give us specific part of an image in a proper perspective(not rotated and stuff)
card_img= cv2.imread('Resources/cards.jpg')

#we have to specify width and height of a card (normally a card is 2.5 x 3.5 inches)
width, height= 250, 350
#so we got the points of a specific card on image
pts1= np.float32([[23, 60], [187, 57], [23, 300], [187,298]])
#now we have to specify which point represent each location (like starting left top point, or end bottom right corner)
    #0,0 starting position of card-->top left point
    #187,57 ---> top right point where height will be 0 and width will be max
    #23,300 ---> bottom left 
    #187, 298 --->bottom right
pts2= np.float32([[0,0], [width, 0], [0, height], [width, height]])

#making perspectiveTransform matrix using points of image we want
matrix= cv2.getPerspectiveTransform(pts1, pts2)

#using image, matrix to get the warpImage
img_out= cv2.warpPerspective(card_img, matrix, (width, height))
cv2.imshow("Cards Image", card_img)
cv2.imshow("Warp Prespective of Card", img_out)
cv2.waitKey(0)