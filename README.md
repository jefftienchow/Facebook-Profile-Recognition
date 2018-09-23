# Facebook-Profile-Recognition
-An application written during HackMIT

# Goal
Facebook Profile Rocognition is an online application that allows you to find the Facebook profile of the person of interest by providing a input photo.

# Implementation
The Facebook graphics API (https://facebook-sdk.readthedocs.io/en/latest/api.html) is utilized to get the publicly available photos and the link to each profile; the face recognition module (https://github.com/ageitgey/face_recognition) is used to compare the photos in your friend database and the input photo.

# Steps
1. Grab your friends list
2. Grab the available photos for each person on the list
3. Upload a photo/photos as input
4. Face recognition on both sides
5. Mathcing the faces
6. Provide recommendations (links to profile)

# Demonstration
Database
<img src="https://github.com/jefftienchow/Facebook-Profile-Recognition/blob/master/Aaron_Kwok.jpg" height="150">
<img src="https://github.com/jefftienchow/Facebook-Profile-Recognition/blob/master/Leonardo_DiCaprio.jpg" height="150">
<img src="https://github.com/jefftienchow/Facebook-Profile-Recognition/blob/master/The_Rock.jpg" height="150">
<img src="https://github.com/jefftienchow/Facebook-Profile-Recognition/blob/master/Tom_Cruise.jpg" height="150">
<img src="https://github.com/jefftienchow/Facebook-Profile-Recognition/blob/master/Will_Smith.jpg" height="150">

Test Files
<img src="https://github.com/jefftienchow/Facebook-Profile-Recognition/blob/master/test.jpg" height="150">
<img src="https://github.com/jefftienchow/Facebook-Profile-Recognition/blob/master/test-2.jpg" height="150">
<img src="https://github.com/jefftienchow/Facebook-Profile-Recognition/blob/master/test-3.jpg" height="150">
