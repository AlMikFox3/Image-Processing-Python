# USAGE
# python getting_and_setting.py --image ../images/trex.png

# Import the necessary packages
from __future__ import print_function
import argparse
import cv2

# Construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
	help = "Path to the image")
args = vars(ap.parse_args())

# Load the image and show it
image = cv2.imread(args["image"])
cv2.imshow("Original", image)

(b, g, r) = image[0, 0]
print("Pixel at (0, 0) - Red: {}, Green: {}, Blue: {}".format(r, g, b))

image[0, 0] = (0, 0, 255)
(b, g, r) = image[0, 0]
print("Pixel at (0, 0) - Red: {}, Green: {}, Blue: {}".format(r, g, b))

corner = image[0:100, 0:100]
cv2.imshow("Corner", corner)

width = image.shape[1]
height = image.shape[0]

image[0:10, 0:width] = (0, 80, 255)
image[height-10:height, 0:width] = (0, 80, 255)
image[0:height, 0:10 ] = (0, 80, 255)
image[0:height, width-10:width] = (0, 80, 255)

# Show the updated image
cv2.imshow("Updated", image)
#newname = args[image]
cv2.imwrite(args["image"].replace(".","")+"-border.jpg",image)
cv2.waitKey(0)