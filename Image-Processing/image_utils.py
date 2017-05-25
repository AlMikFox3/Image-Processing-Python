import numpy as np
import argparse
import cv2

def translate (image,x,y):
	mat = np.float32([[1,0,x],[0,1,y]])
	s = cv2.warpAffine(image, mat, (image.shape[1], image.shape[0]))
	return s

def rotate (image,angle,center=None,scale=1.0):
	(h,w)=(image.shape[0],image.shape[1])
	if center is None:
		center = (w//2, h//2)
	rot_matrix = cv2.getRotationMatrix2D(center, angle, scale)
	rot = cv2.warpAffine(image,rot_matrix,(w,h))
	return rot

def resize (image, width=None, height=None, interpolation = cv2.INTER_AREA):
	dim = None
	(h,w) = image.shape[:2]
	if width is None and height is None:
		return image

	if width is None:
		r = height/float(h)
		dim = (int(w*r), height)
	else:
		r = width/float(w)
		dim = (width, int(h*r))
	resized = cv2.resize(image,dim,interpolation= interpolation)
	return resized


