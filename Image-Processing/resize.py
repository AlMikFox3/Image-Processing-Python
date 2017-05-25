import numpy as np 
import argparse
import cv2
import image_utils

ap = argparse.ArgumentParser()
ap.add_argument("-i","--image", required = True, help = "image path" )
args = vars(ap.parse_args())
image = cv2.imread(args["image"])
cv2.imshow("Original",image)
cv2.waitKey(0)

#Resizing to width 150px
ratio = 150/image.shape[1]
dim = (150,int(image.shape[0]*ratio))
resized = cv2.resize(image,dim,cv2.INTER_AREA)
cv2.imshow("Resized",resized)
cv2.imwrite("Resized.jpg",resized)
cv2.waitKey(0)

x = image_utils.rotate(image,45)
cv2.imshow("rot",x)
cv2.waitKey(0)

p = image_utils.resize(image,750)
cv2.imshow("resz",p)
cv2.waitKey(0)