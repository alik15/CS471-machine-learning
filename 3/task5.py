import cv2


image = cv2.imread("lab3_walle.jpg")
x = 42
y = 42

center_coordinates = (x, y)
radius = 42
red = (0,0,190)
black = (0,0,0)
thickness = -1

count = 4
color = red

while(count>0):
    row_count = 5
    count = count - 1 
   
    
    while(row_count>0):
        
        cv2.circle(image, center_coordinates, radius, color, thickness)
        x = x + radius*2 + 10
        center_coordinates = (x, y)
        
        row_count = row_count - 1
        
        if(color == red):
            color = black
            
        elif(color == black):
            color = red

    y = y + radius*2 + 10
    x = 42
    center_coordinates = (x, y)

cv2.imshow("radius",image)
cv2.waitKey(0)