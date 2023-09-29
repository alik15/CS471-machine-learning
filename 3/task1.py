'''Write a python script in which you will load 3 different images from disk. Then, display the images in different windows
at the same time. You will need to provide the code and a single screenshot which shows all 3 windows at the same time.'''

import cv2 
image1 = cv2.imread("lab3_robot_green_bg.bmp")
image2 = cv2.imread("lab3_robots.jpg")
image3 = cv2.imread("lab3_walle.jpg")



    
cv2.imshow('Image 1', image1)
cv2.imshow('Image 2', image2)
cv2.imshow('Image 3', image3)

cv2.waitKey(0)
