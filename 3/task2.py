'''Write code to load the walle.jpg file. Using the slice operation, crop out the four quadrants of the image and display them
in separate windows. The code must be generic enough to take the image size into account. For submission, provide the code and 
a single screenshot showing all 4 windows.'''

import cv2
img = cv2.imread("lab3_walle.jpg")
y = 0
x = 0
height, width = img.shape[:2]
h = int(height/2)
w = int(width/2)

top_left_quadrant =  img[y:y+h, x:x+w]
top_right_quadrant = img[y:y+h, w:width]
bottom_left_quadrant = img[h:height, x:x+w]
bottom_right_quadrant = img[h:height, w:width]


cv2.imshow("top right quadrant", top_right_quadrant)
cv2.imshow("top left quadrant", top_left_quadrant)
cv2.imshow("bottom right quadrant", bottom_right_quadrant)
cv2.imshow("bottom left quadrant", bottom_left_quadrant)

cv2.waitKey(0)