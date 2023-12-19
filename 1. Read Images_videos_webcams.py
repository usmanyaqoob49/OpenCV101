import cv2

##################################reading image###############################

img= cv2.imread('Resources/usman.jpeg')
#displaying the image
cv2.imshow('Output Image', img)
#we have to add delay to see image otherwise it will get disappear
        #0 means infinite delay, user has to cancel by himself
cv2.waitKey(0)

################################Reading Video################################
#we will create video capture object
cap= cv2.VideoCapture('Resources/vid.mkv')
#as video is sequences of frames so we will apply while loop on videos to display them
while True:
    #reading the object--> success will tell when all frames are read
    success, img= cap.read()
    cv2.imshow("Video", img)
    #adding delay and when user press q it get out of loop
    if cv2.waitKey(1) &  0xFF== ord('q'):
        break

#############################Reading Video from Webcam##########################

#creating video capturing object that will capture our webcam (given by id=0)
cap= cv2.VideoCapture(0)
#setting width of the result and width has setting id=3
cap.set(3, 640)
#setting height of the result and height has setting id=4
cap.set(4, 480)

#rest we will do same for shownig frames
while True:
    #reading the object--> success will tell when all frames are read
    success, img= cap.read()
    cv2.imshow("Video", img)
    #adding delay and when user press q it get out of loop
    if cv2.waitKey(1) &  0xFF== ord('q'):
        break