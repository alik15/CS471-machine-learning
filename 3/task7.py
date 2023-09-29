'''Load any one of the provided images and use the resize function to make copies of the image at different sizes.
Display at least 3 different sizes in separate windows and take the screenshot. Provide the code and screenshot for the submission.

'''

import cv2

image = cv2.imread("lab3_walle.jpg")

#resized image 1 
ratio = 600.0 / image.shape[1]
dimension = (600, int(image.shape[0] * ratio))
resizedImage = cv2.resize(image, dimension, interpolation=cv2.INTER_AREA)

#resized image 2
ratio = 200.0 / image.shape[1]
dimension = (200, int(image.shape[0] * ratio))
resizedImage2 = cv2.resize(image, dimension, interpolation=cv2.INTER_AREA)

#resized image 3
ratio = 400.0 / image.shape[1]
dimension = (400, int(image.shape[0] * ratio))
resizedImage3 = cv2.resize(image, dimension, interpolation=cv2.INTER_AREA)


cv2.imshow("Resized Image 1", resizedImage)
cv2.imshow("Resized Image 2", resizedImage2)
cv2.imshow("Resized Image 3", resizedImage3)
cv2.imshow("original Image", image)
cv2.waitKey(0)