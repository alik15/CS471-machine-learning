'''For detection of faces, people, objects etc. in images, the result of the detection is depicted as a rectangular box around
the detection. Load the robots.jpg image and use the cv2.rectangle function to place bounding boxes around the robots.
Each bounding box must be of a different color. Provide the code and screenshot of the final result.

'''

import cv2

image = cv2.imread("lab3_robots.jpg")

cv2.rectangle(image,(370,60),(470,300),(0,0,190),3)
cv2.rectangle(image,(490,60),(570,300),(0,250,0),3)

cv2.rectangle(image, (90, 20),(170, 200),(250,0,0),3)
cv2.rectangle(image, (180, 60),(300, 300),(250,0,250),3)


cv2.imshow("bounded_box_image",image)
cv2.waitKey(0)