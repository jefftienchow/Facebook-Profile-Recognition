from cv2 import *
import numpy as np
import os
import facebook

import get_photo
import webcam
import facial_recog

ACCESS_TOKEN = 'EAAaJZCDDvNSEBAIF8u2AyRZCDYvenn8QYGmGLTLU0ujyq5NZBCJFXl7iEtmKDHM0An2XXRVXFGZAFUlHEpLfMkC78ONsNsTL5IVvldUx40nb12cC9CL9MGPRNRZCICEY9u8CGmgEmMN2ziGWoEtOw2MdyZAF0TQpwF7WuE2RXzDsqmID9kiaAhwrtxPtCZAougE2QpuPiNZBZBwZDZD'
	

# Takes a picture and then returns the facebook profile

def main():
	get_photo.get_photo_func()
	webcam.capture()
	paths = get_picture_paths()
	ordered_ids = [path.split('/')[1] for path in paths]
	results = facial_recog.face_recog(paths, 'filename.jpg')
	print(results)
	target = [ordered_ids[i].split('.')[0] for i in range(len(paths)) if results[i]][0]

	graph = facebook.GraphAPI(access_token= ACCESS_TOKEN, version="3.0")
	target_info = graph.get_object(id=target)
	print(target_info)

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
