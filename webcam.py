# import pygame
# import pygame.camera
# from pygame.locals import *
#
# pygame.init()
#
# pygame.camera.init()
#
# camlist = pygame.camera.list_cameras()
# if camlist:
#     cam = pygame.camera.Camera(camlist[0],(640,480))

from cv2 import *
# initialize the camera
cam = VideoCapture(0)   # 0 -> index of camera
s, img = cam.read()
if s:    # frame captured without any errors
    namedWindow("cam-test",CV_WINDOW_AUTOSIZE)
    imshow("cam-test",img)
    waitKey(0)
    destroyWindow("cam-test")
    imwrite("filename.jpg",img) #save image


