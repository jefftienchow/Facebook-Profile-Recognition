#Facebook-Profile-Recognition

if __name__ == "__main__":

        import facebook

        your_token = 'EAAaJZCDDvNSEBAFgZCV5HFSQNBRZALr3WVwHdPMIIET8jB082pdfOuZAoQdjcAhxgJxbxAqFRMyZC3OrV2pnoZAmFHZB94dQdCfyJvGVkJ9cIkvTWpcTxXUf8gLV87SrZCVnY4PLW7jRaVGKKIO8Butx4F6JycCjpPBjANxBpJz9nF8Ck7c5enNAko9alPASo9sZD'

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
