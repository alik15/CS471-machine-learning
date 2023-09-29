'''Load any one of the provided images and use the rotate function to rotate the image at angles of 30, 60 and 90 degrees. 
For each rotated image, you need to manually adjust the scale factor (in get2DRotationMatrix function) so that the entire image 
is shown in the window. The rotated image’s border/corner must touch the window’s border. Show all 3 windows in the screenshot. 
Provide the code and screenshot for the submission.'''

import cv2

def rotate_image(angle, scale_factor, image):



    # Define a center point for the rotation
    h, w = image.shape[:2]
    center = (w // 2, h // 2)

    # Create the affine transformation matrix for image rotation
    M = cv2.getRotationMatrix2D(center, angle, scale_factor)
    rotated_image = cv2.warpAffine(image, M, (w, h))
    return rotated_image

image1 = cv2.imread("lab3_walle.jpg")
image2 = cv2.imread("lab3_robots.jpg")
image3 = cv2.imread("lab3_robot_green_bg.bmp")

rotated_image = rotate_image(30, 0.71,image1)
rotated_image2 = rotate_image(60, 0.7, image1)
rotated_image3 = rotate_image(90, 1, image1)

cv2.imshow("rotated_image 1", rotated_image)
cv2.imshow("rotated_image 2", rotated_image2)
cv2.imshow("rotated_image 3", rotated_image3)
cv2.waitKey(0)