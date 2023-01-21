# -*- coding: utf-8 -*-
"""
@author: Projet Multidisciplinaire Agregation algues - MAIN3 promo 2025
"""

import cv2
import os

current = os.getcwd()

#On ouvre la video (avec son chemin d'accès)
cap= cv2.VideoCapture(current + '/video/FOV_2_20fps.avi')

i=0
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == False:
        print("Fin de l'extraction des images")
        break
    if i%1 == 0:
        cv2.imwrite("image_frame_video/" + str(i)+'.jpg',frame)
    i+=1

cap.release()
cv2.destroyAllWindows()