import numpy as np
import argparse
import cv2
import image_utils
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
	help = "Path to the image")
args = vars(ap.parse_args())
image = cv2.imread(args["image"])
cv2.imshow("Original Image",image)
cv2.waitKey(0)
#shift 25 pix to right and 40 pix right
mat = np.float32([[1,0,25],[0,1,40]])
shifted = cv2.warpAffine(image,mat,(image.shape[1],image.shape[0]))
cv2.imshow("25r 40d", shifted)
cv2.waitKey(0)

s2 = image_utils.translate(image,-20,-20)
cv2.imshow("20l 20u",s2)
cv2.waitKey(0)