from cv2 import *
import numpy as np
import os

import get_photo
import webcam
import facial_recog

# Takes a picture and then returns the facebook profile

def main():
	get_photo.get_photo_func()
	webcam.capture()
	paths = get_picture_paths()
	results = facial_recog.face_recog(paths, 'filename.jpg')
	print(results)


def get_picture_paths():
	return ['facebook_pictures/'+filename for filename in os.listdir('facebook_pictures')]



def link_to_profile_url(file):
        url_dic = {}
        f = open(file,'r')
        for i in f.readlines():
                id, id_photo = i.split('\t')
                url_dic[id_photo] = id 
        


if __name__ == '__main__':
	main()
