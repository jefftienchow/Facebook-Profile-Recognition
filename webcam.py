from cv2 import *
import numpy as np
# initialize the camera
cam = VideoCapture(0)   # 0 -> index of camera
s, img = cam.read()
if s:    # frame captured without any errors
    #namedWindow("cam-test",WINDOW_NORMAL)#CV_WINDOW_AUTOSIZE)
    #imshow("cam-test",img)
    #waitKey(0)
    #destroyWindow("cam-test")

    img = add(img,np.array([50.0]))

    imwrite("filename.jpg",img) #save image