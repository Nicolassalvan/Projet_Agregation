# -*- coding: utf-8 -*-
"""
@author: Projet Multidisciplinaire Agregation algues - MAIN3 promo 2025
"""


import cv2
import numpy as np
import math
from fonction import nombre_cell
import os
import matplotlib.pyplot as plt
from os import listdir
from os.path import isfile, join
import numpy

#on recupère le chemin courant
current = os.getcwd()

#chemin dans lequel on va chercher les différentes frames extraites de la video 
mypath= current + '/image_frame_video'

onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]


#on cree un tableau numpy qui stocke les images sous forme de matrice 
images = numpy.empty(len(onlyfiles), dtype=object)
for n in range(0, len(onlyfiles)):
    print("Calcul de l'image n°",n)
    
    images[n] = cv2.imread(mypath + "/" + str(n) + ".jpg")
    images[n] = images[n][0:1100, 0:2048]
    
    #print(mypath + "/" + str(n) + ".jpg")
    #fin boucle




#tableau que l'on remplira avec les aires maximales des agrégats de chaque image
tab_airesMax = np.empty(len(images))

#tableau des que l'on remplira avec le nombre de cellules pour chaque image
nb_cell_fonction = np.empty(len(images))

#tableau que l'on remplira avec le nombre de cellules pour chaque image (seconde méthode)
nb_cell_methode_min = np.empty(len(images))

#tableau que l'on remplira avec l'aire moyenne de tous les objets détectés
average_all = np.empty(len(images))

#tableau que l'on remplira avec l'aire moyenne des agrégats
average_agregat = np.empty(len(images))

for i in range (len(images)):
    original = images[i].copy()
    hsv = cv2.cvtColor(images[i], cv2.COLOR_BGR2HSV)

#plage de hue saturation value

    hsv_lower = np.array([0,0,0])
    #filtre changeant au fil du temps
    hsv_upper = np.array([0,0,145-(i//35)])
    

#creer un masque qui dépend de la plage de hsv
    mask = cv2.inRange(hsv, hsv_lower, hsv_upper,cv2.THRESH_BINARY)

#on utilise une matrice de convolution (principe de filtre de sobel)
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (1,1))
    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)


#retr external prend le contour element exterieur et pas intérieur
#cnts va etre un tableau de tout les contours trouvés
    cnts = cv2.findContours(opening, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

#prend l'élément correspondant a l'indice 0 si longueur tab = 2 et sinon prend elem a l'indice 1
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]
    cntsSorted = sorted(cnts, key=lambda x: cv2.contourArea(x))

    area_list_size_test=[]
    for c in cntsSorted:
        e = cv2.contourArea(c)
        if e>0:
            if e<2:
                area_list_size_test.append(2.0)
            area_list_size_test.append(e)
            
    
    aireMax = max(area_list_size_test)
    tab_airesMax[i] = aireMax
    
    
    minimum_area = area_list_size_test[0]
    average_cell_area = np.average(area_list_size_test)
    connected_cell_area= minimum_area*2



    cells = 0



    #stocke nb de pixel dans le contour
    area_list=[]
    
    for c in cntsSorted:
        area = cv2.contourArea(c)
        if area > minimum_area:
    
            area_list.append(area)
            
            #pour vérifier si cela est bien détouré on dessine les différents contours
            #-1 indique que je veux draw les contours dans c jusqu'au dernier element
            cv2.drawContours(original, [c], -1, (0,255,0), 1)
            
            if area > connected_cell_area:
                cells += math.ceil(area // average_cell_area)
                
            else:
                cells += 1

    nb_cell_fonction[i]=nombre_cell(area_list)
    nb_cell_methode_min[i]=cells
    average_all[i] = np.average(area_list)
    every_agregat = []
    for f in area_list:
        if f > 100:
            every_agregat.append(f)
        
    average_agregat[i] = np.average(every_agregat)
    # print('Cells: {}'.format(cells))
    #on affiche le tableau
    #print(area_list)

# print("nombre de cellule par la fonction crée: ",nombre_cell(area_list))
# print("nombre de cellule méthode 2: ",cells)
# print("evolution aire max",tab_airesMax)
    
NB_IMAGES = np.arange(0, len(images), 1)
plt.plot(NB_IMAGES*330, tab_airesMax, label = "aire max")
plt.title("Aire max en fonction de l'image")
plt.legend()
plt.show()

plt.plot(NB_IMAGES*330, nb_cell_fonction, label = "evolution nombre cellules déduit par la fonction")
plt.xlabel("seconde (s)")
plt.title("Cellules détectées en fonction du temps")
plt.legend()
plt.show()

plt.plot(NB_IMAGES*330, nb_cell_methode_min, label ="evolution nombre cellules")
plt.xlabel("seconde (s)")
plt.title("Cellules détectées par la deuxieme méthode")
plt.legend()
plt.show()

plt.plot(NB_IMAGES*330, average_all, label ="evolution surface cellules+agregats+palmeloides")
plt.xlabel("seconde (s)")
plt.title("Evolution surface cellules+agregats+palmelloides")
plt.xlabel("seconde")
plt.ylabel("taille_moyenne")
plt.legend()
plt.show()

plt.plot(NB_IMAGES*330, average_agregat, label ="evolution surface agregat")
plt.xlabel("seconde (s)")
plt.title("Evolution de la surface moyenne des agregats")
plt.xlabel("seconde")
plt.ylabel("taille_moyenne")
plt.legend()
plt.show()