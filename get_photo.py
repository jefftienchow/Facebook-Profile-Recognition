import os
import requests
import urllib
import sys

ACCESS_TOKEN = "EAAaJZCDDvNSEBAAVkugeZARYfmEwyGFOgUOJwzjd5j6bnFTPszK86BubtpUMC1gZBjK8Xr3h4LC62JSL3kB8lrNBBeZALQ0J5REN7p6zlzZAgLJx9ZA9FM6Sz4QBauevMUjtxY5NnGbdf9pq6yGZCLPZCkEkT14qw0fZCRZCZBEvhWzhMQruh2aj1WaaHVb5h0cDo0ZD"
photo_type = 'tagged'
r_url = 'https://graph.facebook.com/v3.1/me/friends?access_token=' + ACCESS_TOKEN
r = requests.get(r_url)
print(r.json())
friend_data = r.json()['data']
friend_ids = []
propics = []


directory = 'facebook_pictures'
if not os.path.exists(directory):
	os.makedirs(directory)

print('locating tagged photos on facebook...')

for friend in friend_data:
	friend_ids.append(friend['id'] + '/picture?height=500&width=500')

for id in friend_ids:
	f_url = 'https://graph.facebook.com/v3.1/' + id + '&access_token=' + ACCESS_TOKEN
	print(f_url)
	#f = requests.get(f_url)
	#print (f.json())
	propics.append(f_url)#f.json()['data'])

# while r_url:
# 	for d in photo_data:
# 		photo_ids.append(d['id'])
# 	if 'paging' in r.json() and 'next' in r.json()['paging']:
# 		r_url = r.json()['paging']['next']
# 		r = requests.get(r_url)
# 		photo_data = r.json()['data']
# 	else:
# 		if photo_type == 'tagged':
# 			print('locating uploaded pictures on facebook...')
# 			photo_type = 'uploaded'
# 			r_url = 'https://graph.facebook.com/v2.12/me/photos?type=' + photo_type + '&access_token=' + ACCESS_TOKEN
# 			r = requests.get(r_url)
# 			photo_data = r.json()['data']
# 		else:
# 			r_url = ""

print('downloading photos...')

for i,propic in enumerate(propics):
	print(propic)
	urllib.request.urlretrieve(propic, os.path.join(directory, friend_ids[i]))

# for photo_id in photo_ids:
# 	photo_url = "https://graph.facebook.com/" + str(photo_id) + "/picture?access_token=" + ACCESS_TOKEN + "&type=normal"
# 	photo_name = photo_id + '.jpg'
# 	urllib.request.urlretrieve(photo_url, os.path.join(directory, photo_name))

print('successfully downloaded ' + str(len(photo_ids)) + ' photos')


def get_fb_token(app_id, app_secret):
	url = 'https://graph.facebook.com/oauth/access_token'
	payload = {
        'grant_type': 'client_credentials',
        'client_id': app_id,
        'client_secret': app_secret
    }
	response = requests.post(url, params=payload)
	return response.json()['access_token']