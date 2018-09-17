import os
import requests
import urllib
import sys

def get_photo_func():
	'''
	Save images (profile pics of your friends) to the facebook_pictures folder
	'''
	ACCESS_TOKEN = "EAAaJZCDDvNSEBAG4ABvmQFxZARKzel1ZBsRX1KLesHNPFGSC75LiDZCR4dwlWmawWcCAHeO2SoVpH9oCr0tiLnspQ5EUkxeAWzrbN81eQusjqcIw0yWnzO2lx4IQ2JhJP93jZCFH5dZB6GI86rD8chjkOL51cOZBrDLxVuxTHytgKTWdGg8NTmjqxfMZA4ilJAQkFoPfIhde9QZDZD"   
	ACCESS_TOKEN = 'EAAaJZCDDvNSEBABZBBUOq6p1mOun1dm64MiUBWrQ5o24keV4HxmPZBOyjxq4JJYQt8bZAUisuK1D1QuTuqPz0iLR3iWGU8OU2J7ur7Ybs57cwwtFkrhIN4gamBcN6OfyoNHkXoZB76UI6ByXBD2ugm4ikh4Oi9Piu79ZAkidsKYuI69hJRIeA3s2xw4lauSKrnoORAYhKZB1sonIVyWoZBRji4NIC7PA2KuHmdrWgtaBqgZDZD'
	photo_type = 'tagged'
	r_url = 'https://graph.facebook.com/v3.1/me/friends?access_token=' + ACCESS_TOKEN
	r = requests.get(r_url)
	print(r.json())
	friend_data = r.json()['data']
	friend_ids = [] # a list of ids
	friend_names = []
	propics = [] # a list of f_urls

	directory = 'facebook_pictures'
	if not os.path.exists(directory):
		os.makedirs(directory)
	
	directory2 = 'static'
	if not os.path.exists(directory2):
		os.makedirs(directory2)
		
	print('locating tagged photos on facebook...')

	friend_ids = [friend['id'] for friend in friend_data]
	friend_names = [friend['name'] for friend in friend_data]

	for id in friend_ids:
		f_url = 'https://graph.facebook.com/v3.1/' + id + '/picture?height=500&width=500' + '&access_token=' + ACCESS_TOKEN
		print(f_url)
		propics.append(f_url)

	print('downloading photos...')

	for i,propic in enumerate(propics):
		#print(propic)
		urllib.request.urlretrieve(propic, os.path.join(directory, friend_ids[i] + '.jpg'))
		urllib.request.urlretrieve(propic, os.path.join(directory2, friend_ids[i] + '.jpg'))

##	def get_fb_token(app_id, app_secret):
##		url = 'https://graph.facebook.com/oauth/access_token'
##		payload = {
##	        'grant_type': 'client_credentials',
##	        'client_id': app_id,
##	        'client_secret': app_secret
##	    }
##		response = requests.post(url, params=payload)
##		return response.json()['access_token']
