'''Load any one of the provided images and place a line, rectangle, circle and text using the inbuilt functions in OpenCV.
Each of the placed object must have a different color. The text must contain the name of at least one member of your group.
Provide the code and screenshot of the image.'''

import cv2

image = cv2.imread("lab3_robot_green_bg.bmp")


# line 
x1 = 10
x2 = 100
y1 = 20
y2 = 100
thickness = 5
cv2.line(image, (x1, y1), (x2, y2), (255, 0, 0), thickness)

# circle
center_coordinates = (200,200)
color = (255,255,255)
thickness = -1
radius = 50
cv2.circle(image, center_coordinates, radius, color, thickness) 

# rectangle
top_left_coordinate = (200,60)
top_right_coordinate = (300,100)
color = (0,255,255)
thickness = -1
cv2.rectangle(image,top_left_coordinate,top_right_coordinate,color, thickness)

# text 
text = "ALI"
org = (100,200)
font = cv2.FONT_HERSHEY_SIMPLEX
color = (0,0,255)

cv2.putText(image,text,org, font, 5, color, 5, cv2.LINE_AA)




cv2.imshow("image",image)
cv2.waitKey(0)