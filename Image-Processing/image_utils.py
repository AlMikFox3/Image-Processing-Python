import numpy as np
import argparse
import cv2

def translate (image,x,y):
	mat = np.float32([[1,0,x],[0,1,y]])
	s = cv2.warpAffine(image, mat, (image.shape[1], image.shape[0]))
	return s