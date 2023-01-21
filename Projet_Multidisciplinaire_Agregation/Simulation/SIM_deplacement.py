# -*- coding: utf-8 -*-
"""
@author: Projet Multidisciplinaire Agregation algues - MAIN3 promo 2025
"""

import SIM_class_algue as cla 
import _settings as config
import random as rand
import numpy as np

def check_deplacement(population, i, box, deplacement):
    """

    Cette fonction vérifie si le déplacement est possible ou non.
    Si le déplacement est possible, elle renvoie True, -1
    Si le déplacement n'est pas possible car en dehors de la box, elle renvoie False, -1
    Si le déplacement n'est pas possible car une autre cellule est présente, elle renvoie False, j, avec j l'indice de la cellule présente


    Paramètre 
    =============

    population : tableau numpy de cellules
    i : indice de la cellule
    box : tableau numpy de l'environnement où se déplace les cellules
    deplacement : tableau numpy du déplacement possible (x,y)
    """
    # je vérifie que je ne sorte pas de la box
    if (population.x[i] + deplacement[0] > box.x_max or population.x[i] + deplacement[0] < 0):
        return False
    if (population.y[i] + deplacement[1] > box.y_max or population.y[i] + deplacement[1] < 0):
        return False

    # je vérifie que je ne me déplace pas sur une autre cellule
    for j in range(population.nombre_algues):
        if (i != j):
            if (population.x[i] + deplacement[0] == population.x[j] and population.y[i] + deplacement[1] == population.y[j]):
                return False
    return True

def deplacement_cellule(population,box):
    """
    La fonction modifie les coordonnées des cellules de la population sans prendre en compte le stress

    retourne la population modifiée

    Paramètre
    =============
    population : tableau numpy de cellules
    box : tableau numpy de l'environnement où se déplace les cellules
    """
    for i in range(population.nombre_algues):
        if (population.agregat[i] == False):
            x = rand.randint(-config.DEP_MAX, config.DEP_MAX)
            y = rand.randint(-config.DEP_MAX, config.DEP_MAX)
            deplacement = np.array([x,y])

            if (check_deplacement(population, i, box, deplacement)):
                population.x[i] += deplacement[0]
                population.y[i] += deplacement[1]



