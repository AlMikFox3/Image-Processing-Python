import numpy as np
import argparse
import cv2
import image_utils

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
	help = "Path to the image")
args = vars(ap.parse_args())
image = cv2.imread(args["image"])

(h,w)=(image.shape[0],image.shape[1])
center = (w//2, h//2)
rot_matrix = cv2.getRotationMatrix2D(center, -45, 1.0)

rot = cv2.warpAffine(image,rot_matrix,(w,h))
cv2.imshow("45 anticlock", rot)
cv2.waitKey(0)

rot1 = image_utils.rotate(image,-90)
cv2.imshow("90 clock", rot1)
cv2.waitKey(0)