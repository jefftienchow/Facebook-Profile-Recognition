from cv2 import *
import numpy as np
import os
import facebook

import get_photo
import webcam
import facial_recog

ACCESS_TOKEN = 'EAAaJZCDDvNSEBABZBBUOq6p1mOun1dm64MiUBWrQ5o24keV4HxmPZBOyjxq4JJYQt8bZAUisuK1D1QuTuqPz0iLR3iWGU8OU2J7ur7Ybs57cwwtFkrhIN4gamBcN6OfyoNHkXoZB76UI6ByXBD2ugm4ikh4Oi9Piu79ZAkidsKYuI69hJRIeA3s2xw4lauSKrnoORAYhKZB1sonIVyWoZBRji4NIC7PA2KuHmdrWgtaBqgZDZD'
	

# Takes a picture and then returns the facebook profile

def main(photo):
	get_photo.get_photo_func()
	if not photo:
                webcam.capture()
	paths = get_picture_paths()
	ordered_ids = [path.split('/')[1] for path in paths]
	results = facial_recog.face_recog(paths, 'filename.jpg')
	print(results)
	try:
		target = [ordered_ids[i].split('.')[0] for i in range(len(paths)) if results[i]][0]
	except:
		print('No one recgnized')
		return {'name':"No one recognized" , 'id': "0"}
	graph = facebook.GraphAPI(access_token= ACCESS_TOKEN, version="3.0")
	target_info = graph.get_object(id=target)
	print(target_info)
	return target_info

def get_picture_paths():
	return ['facebook_pictures/'+filename for filename in os.listdir('facebook_pictures')]



##def link_to_profile_url(file):
##        url_dic = {}
##        f = open(file,'r')
##        for i in f.readlines():
##                id, id_photo = i.split('\t')
##                url_dic[id_photo] = id 
        


if __name__ == '__main__':
	main()
