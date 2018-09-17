#Facebook-Profile-Recognition

if __name__ == "__main__":

        import facebook

        your_token = 'EAAaJZCDDvNSEBABZBBUOq6p1mOun1dm64MiUBWrQ5o24keV4HxmPZBOyjxq4JJYQt8bZAUisuK1D1QuTuqPz0iLR3iWGU8OU2J7ur7Ybs57cwwtFkrhIN4gamBcN6OfyoNHkXoZB76UI6ByXBD2ugm4ikh4Oi9Piu79ZAkidsKYuI69hJRIeA3s2xw4lauSKrnoORAYhKZB1sonIVyWoZBRji4NIC7PA2KuHmdrWgtaBqgZDZD'

        graph = facebook.GraphAPI(access_token= your_token, version="3.0")

        friends_dic = graph.get_object(id='1750688195044088', fields='friends')
        #print(friends_dic)

        ids = []

        friends_list = friends_dic['friends']['data']
        for f in friends_list:
                ids.append(f['id'])

        all_photos = []
        for id in ids:
                photos = graph.get_object(id=id, fields='photos')
                all_photos.append(photos)
        #print(all_photos)

photos_dic = {}
for friend in all_photos:
        id = friend['id']
        photos_info = friend['photos']['data']
        temp = []
        for photo in photos_info:
                temp.append(photo['id'])
        photos_dic[id] = temp


for keys, values in photos_dic.items():
    print(keys)
    print(values)


url = 'https://graph.facebook.com/' + id + '?fields=images&access_token=' + your_token
