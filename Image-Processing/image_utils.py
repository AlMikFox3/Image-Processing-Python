import numpy as np
import argparse
import cv2

def translate (image,x,y):
	mat = np.float32([[1,0,x],[0,1,y]])
	s = cv2.warpAffine(image, mat, (image.shape[1], image.shape[0]))
	return s

def rotate (image,angle):
	(h,w)=(image.shape[0],image.shape[1])
	center = (w//2, h//2)
	rot_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
	rot = cv2.warpAffine(image,rot_matrix,(w,h))
	return rot