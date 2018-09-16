from cv2 import *
import numpy as np
import os

import get_photo
import facial_recog

# Takes a picture and then returns the facebook profile
def main():
	get_photo.get_photo_func()

	urls = get_picture_urls()
	results = facial_recog.face_recog(urls, 'filename.jpg')
	print(results)


def get_picture_urls():
	return ['facebook_pictures/'+filename for filename in os.listdir('facebook_pictures')]


def capture():
	# initialize the camera
	cam = VideoCapture(0)   # 0 -> index of camera
	s, img = cam.read()
	if s:
	    img = add(img,np.array([50.0]))
	    imwrite("filename.jpg",img) #save image



if __name__ == '__main__':
	main()