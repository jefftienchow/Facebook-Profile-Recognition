# Webcam

from cv2 import *
import numpy as np
import os
import time

def capture():
	'''
	Take a photo from webcam and save as filename.jpg
	'''
	# initialize the camera
	cam = VideoCapture(0)   # 0 -> index of camera
	time.sleep(1.2)
	s, img = cam.read()
	if s:
	    #img = add(img,np.array([100.0]))
	    imwrite("filename.jpg",img) #save image
	    del(cam)



if __name__ == '__main__':
	capture()
