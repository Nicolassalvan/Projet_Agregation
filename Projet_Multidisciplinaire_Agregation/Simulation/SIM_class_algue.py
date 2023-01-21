# -*- coding: utf-8 -*-
"""
@author: Projet Multidisciplinaire Agregation algues - MAIN3 promo 2025
"""

# Librairies pour le calcul
import random as rd
import numpy as np

import _settings as config


#///////////////////////////////////////////////////////////////////////////#
#                          Population d'algues                              #
#///////////////////////////////////////////////////////////////////////////#
        
class Population:
    """
    Représente une population d'algues. Chaque algue est représenté par son indice i, et 
    les informations de chaque algue sont stocké dans des tableaux numpy. Ainsi, une algue
    est définie par sa position x, y, son age (temps entre les reproductions), sa taille 
    (selon le stade de reproduction, servira pour l'affichage), son statut (aggloméré ou non).
    Aussi, la population est définie par son effectif (nombre_algues).
    
    Paramètres pour l'initialisation
    ------
    nombre_algues: unsigned int
        nombre d'algues de la populatio; Supérieur à 0
    Box: class Box
        zone de simulation, définie par x_max et y_max
    
    Attributs 
    ------
    x: array of float
        coordonnées x, entre 0 et la coordonnée maximale x_max de la Box
    y: array of float
        coordonnées y, entre 0 et la coordonnée maximale y_max de la Box
    age: array of int
        age de la cellule, entre 0 et le temps de reproduction
    taille: array of int
        taille de la cellule, parmi TAILLE_1, TAILLE_2, TAILLE_4, TAILLE_8
    agregat: array of boolean
        état d'agrégation des cellules. True si agrégé; False si non agrégée
        
    """
    
    def __init__(self, nombre_algues, Box):
        # Nombre d'algues de la population
        self.nombre_algues = nombre_algues
        # Coordonnées de chaque algue
        self.x = np.array([])
        self.y = np.array([])
        # Age de chaque algue pour calculer les divisions
        self.age = np.random.randint(0, config.TEMPS_DIV, nombre_algues)
        # Stade de croissance / Taille affichée de la cellule
        self.taille = np.ones(nombre_algues) * config.TAILLE_1
        # Etat: True si agregee, False si non agrégée
        self.agregat = np.random.choice([True, False], nombre_algues, True, np.array([0,1]))        
        # Generation de chaque algue, en vérifiant qu'aucune ne soit à la même coordonnée
        for i in range(nombre_algues):
            x1 = rd.randint(0, Box.x_max)
            y1 = rd.randint(0, Box.y_max)
            # Verification de la présence des coordonnées dans la liste, si oui on les modifie
            not_in_list = False
            while not_in_list == False:
                not_in_list = True
                for j in range(i):
                    if x1 == self.x[j] and y1 == self.y[j]:
                        x1 = rd.randint(0, Box.x_max)
                        y1 = rd.randint(0, Box.y_max)
                        not_in_list = False
                        j = i
            self.x = np.append(self.x, x1)
            self.y = np.append(self.y, y1)

            
    def afficher_coord_algues(self):
        """
        Affiche les coordonnées de chaque algue dans la console. 
        """
        print("x ; y \n")
        for i in range (self.nombre_algues):
            print("{} ; {}\n".format(self.x[i], self.y[i]))
            
    
    def supprimer_algue(self, tab):
        """
        Supprime de la population l'ensemble des élements dont l'indice est dans le tableau. 
        tab est soit un tableau d'entier soit un entier (quand on veut supprimer une cellule)
        
        Paramètres
        ------
        tab: tableau d'entiers, ou nombre entier
            Indices à supprimer. Doivent être plus petit que le nombre d'algues.
        """
        self.x = np.delete(self.x, tab, 0)
        self.y = np.delete(self.y, tab, 0)
        self.age = np.delete(self.age, tab, 0)
        self.agregat = np.delete(self.agregat, tab, 0)
        self.taille = np.delete(self.taille, tab, 0)
        self.nombre_algues = self.x.size
    
    def creer_algue(self, x, y, age=0, taille=config.TAILLE_1, agregat=False):
        """
        Ajoute une algue dans la population dont les propriétés sont precisées
        dans les paramètres de la fonction.

        Parameters
        ----------
        x : int
            Coordonnée x de la nouvelle algue.
        y : int
            Coordonnée y de la nouvelle algue.
        age : int, optionnel
            Age de la nouvelle algue.La valeur par défaut est 0. 
        taille : TYPE, optional
            DESCRIPTION. La valeur par défaut est config.TAILLE_1.
        agregat : booléén, optional
            DESCRIPTION. La valeur par défaut est False.
        """
        self.x = np.append(self.x, x)
        self.y = np.append(self.y, y)   
        self.age = np.append(self.age, age)
        self.taille = np.append(self.taille, taille)
        self.agregat = np.append(self.agregat, agregat)
        self.nombre_algues += 1

        
#///////////////////////////////////////////////////////////////////////////#
#                        Zone de simulation (box)                           #
#///////////////////////////////////////////////////////////////////////////#

class Box:
    """
    Représente la zone de simulation où se déplaceront et évolueront les algues. 
    Est défini par un couple x_max et y_max entiers, qui représentent les limites de
    l'affichage et donc de la simulation.
    
    Parametres (et attribiuts) pour l'initialisation
    ------
    x_max: unsigned int
        coordonée x maximale de la zone de simulation
    y_max: unsigned int
        coordonée y maximale de la zone de simulation
    
        
    """
    
    def __init__(self, x_max, y_max):
        self.x_max = x_max
        self.y_max = y_max
    
    def modifier(self, x, y):
        """
        Modifie le couple x_max y_max de la Box par un nouveau couple x,y. 
        
        Paramètres        
        ------
        x: entier strictement positif
            nouvelle coordonnée x_max
        y: entier strictement positif
            nouvelle coordonnée y_max
        """
        self.x_max = x
        self.y_max = y
    
    def afficher_dimensions(self):
        """
        Affiche les dimensions de la zone de simulation. 
        """
        print("Dimensions: {} x {}".format(self.x_max, self.y_max))
        
