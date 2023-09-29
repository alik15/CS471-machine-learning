'''Write code to load the walle.jpg file and place alternating green and white horizontal lines in the image.
Do NOT use the line function (cv2.line). You need to this by changing the pixel colors. Each line must be 1-pixel thick. 
The lines are also spaced apart by 1-pixel wide gap. Thus, the image will have one green line, then one line of image pixels,
then one white line, then another line of image pixels and so on. Provide the code and screenshot for the submission.'''

import cv2
# the 1 indicates that the image should be loaded as a BGR image
img = cv2.imread("lab3_walle.jpg",1)
rows,columns = img.shape[:2]

green = (0,255,0)
white = (255,255,255)

i = 0
j = 0

while( i < rows ):
    while(j < columns):
       
        img[i , j] = green
        i = i + 1
    j = j + 1
            

            
        
cv2.imshow("image",img)
cv2.waitKey(0)
        

