import os
import requests
import urllib
import sys

def get_photo_func():
	'''
	Save images (profile pics of your friends) to the facebook_pictures folder
	'''
	ACCESS_TOKEN = "EAAaJZCDDvNSEBAG4ABvmQFxZARKzel1ZBsRX1KLesHNPFGSC75LiDZCR4dwlWmawWcCAHeO2SoVpH9oCr0tiLnspQ5EUkxeAWzrbN81eQusjqcIw0yWnzO2lx4IQ2JhJP93jZCFH5dZB6GI86rD8chjkOL51cOZBrDLxVuxTHytgKTWdGg8NTmjqxfMZA4ilJAQkFoPfIhde9QZDZD"   
	photo_type = 'tagged'
	r_url = 'https://graph.facebook.com/v3.1/me/friends?access_token=' + ACCESS_TOKEN
	r = requests.get(r_url)
	#print(r.json())
	friend_data = r.json()['data']
	friend_ids = []
	propics = []

	directory = 'facebook_pictures'
	if not os.path.exists(directory):
		os.makedirs(directory)

	print('locating tagged photos on facebook...')

        
	for friend in friend_data:
		friend_ids.append(friend['id'])

	for id in friend_ids:
		f_url = 'https://graph.facebook.com/v3.1/' + id + '/picture?height=500&width=500' + '&access_token=' + ACCESS_TOKEN
		print(f_url)
		propics.append(f_url)
		id_photo = f_url.split('/')[4]


	print('downloading photos...')

	for i,propic in enumerate(propics):
		print(propic)
		urllib.request.urlretrieve(propic, os.path.join(directory, friend_ids[i] + '.jpg'))


##	def get_fb_token(app_id, app_secret):
##		url = 'https://graph.facebook.com/oauth/access_token'
##		payload = {
##	        'grant_type': 'client_credentials',
##	        'client_id': app_id,
##	        'client_secret': app_secret
##	    }
##		response = requests.post(url, params=payload)
##		return response.json()['access_token']
