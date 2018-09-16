# Facial Recognition

import face_recognition

def face_recog(imgs,test_img):
    '''
    img: a list of image paths, one for each person
    test_img: path of the img to the tested
    return a Boolean list of whether test_img correspond to the individual img in imgs
    '''
    faces = [face_recognition.load_image_file(img) for img in imgs]
    face_encodings = [face_recognition.face_encodings(face)[0] for face in faces]

    test_face = face_recognition.load_image_file(test_img)
    test_face_encoding = face_recognition.face_encodings(test_face)[0]

    results = []
    for i in face_encodings:
        to_append = face_recognition.compare_faces([i], test_face_encoding)[0]
        results.append(to_append)

    return results



#results = face_recog(['Daniel_Wang.jpg','Dave_Lin.jpg','Jeff_Chow.jpg'],'test.jpg')
#print(results)
results = face_recog(['Tom_Cruise.jpg','Will_Smith.jpg','Aaron_Kwok.jpg'],'test-2.jpg')
print(results)
