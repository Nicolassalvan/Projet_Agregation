# -*- coding: utf-8 -*-
"""
@author: Projet Multidisciplinaire Agregation algues - MAIN3 promo 2025
"""

import matplotlib.pyplot as plt
import _settings as config
import random as rand
import numpy as np

import SIM_deplacement as dep
import SIM_class_algue as cla 

def recherche_agregat(agregat,indice):
    """
    Paramètre
    ==========
    agregat : liste python des algues aggrégées
    indice : indice de l'algue à tester

    Cette fonction permet de déterminer dans quelle agrégats se trouve la cellule d'indice indice

    retourne l'indice de l'aggrégat dans lequel se trouve la cellule d'indice indice
    """

    for i in range(len(agregat)):
        for j in range(len(agregat[i])):
            if agregat[i][j] == indice:
                return i


def update_agregat2(population,agregat):
    """
    

    Parameters
    ----------
    population : tableau numpy des cellules

    agregat : Liste python des aggrégats

    La fonction permet d'aggréger les différents aggrégats à côté en fonction du stress

    Returns
    -------
    None.

    """
    if (config.STRESS >= config.SEUIL_AGREGAT):
        i = 0
        verif = 0
        while (i != len(agregat)):
            j = 0
            if (len(agregat[i]) < config.COEF*config.STRESS):
                while (j != len(agregat[i]) and verif == 0):
                    k = 0
                    while (k!=len(agregat) and verif == 0):
                        l = 0
                        if (k != i):
                            nombre_cellule = len(agregat[k])
                            while (l != nombre_cellule and verif == 0):
                                if (np.abs(population.x[agregat[i][j]] - population.x[agregat[k][l]]) <= 1 and np.abs(population.y[agregat[i][j]] - population.y[agregat[k][l]]) <= 1):
                                    agregat[i] = agregat[i] + agregat[k]
                                    agregat.remove(agregat[k])
                                    nombre_cellule-=1
                                    verif = 1
                                l += 1
                        k += 1
                    j += 1
            i += 1

def update_agregat(population,agregat):
    """
    Cette fonction permet de créer des agrégats à partir de cellules individuelles

    Paramètre 
    ==========
    population : tableau numpy de cellule
    agregat : liste python des agrégats

    Retour
    ======
    None
    """
    #cette boucle permet de tester s'il y a des cellules autour d'une cellule d'indice i
    for i in range(population.nombre_algues):
        if population.agregat[i] == False:
            j = 0
            verif = 0

            #Cette boucle a pour but de vérifier si la cellule s'aggrège ou non avec une autre cellule autour d'elle
            while (j!= population.nombre_algues and verif == 0):

                #cette condition permet de savoir si il y a une cellule autour de la cellule d'indice i
                if (np.abs(population.x[i] - population.x[j]) <= 1 and np.abs(population.y[i] - population.y[j]) <= 1 and i != j):

                    #si la cellule à côté est aggrégée alors la cellule d'indice i a plus de chance de s'aggréger
                    if (population.agregat[j] == True):

                        #Si la cellule à côté est aggrégée, alors la cellule d'indice i a une probabilité de s'aggréger plus élevée
                        if (rand.uniform(0,1)< config.PROBA_AGREGAT):

                            #si la proba est réussi, alors ajouter cette cellule dans l'aggrégat
                            population.agregat[i] = True
                            population.x[i] = (population.x[j]+population.x[i])/2
                            population.y[i] = (population.y[j]+population.y[i])/2
                            indice = recherche_agregat(agregat,j)
                            agregat[indice].append(i)

                            #je fais vérif = 1 pour arrêter la boucle car la cellule s'est aggrégée
                            verif = 1
                    else :
                        #si la cellule à côté n'est pas aggrégée alors la cellule d'indice i a une probabilité de s'aggréger normal
                        if (rand.uniform(0,1) < config.PROBA_AGREGAT_NORMAL):

                            #si la proba est réussi, alors ajouter les deux cellules comme étant un nouvelle aggrégat
                            population.agregat[i] = True
                            population.agregat[j] = True
                            population.x[i] = (population.x[j]+population.x[i])/2
                            population.y[i] = (population.y[j]+population.y[i])/2
                            agregat.append([i,j])

                            #je fais vérif = 1 pour arrêter la boucle car la cellule s'est aggrégée
                            verif = 1
                j+=1
                            

def check_deplacement_agregat(population, i, box, agregat,deplacement):
    """
    Vérifie si le déplacement d'un agrégat à l'indice i est possible

    Paramètre 
    =========
    population : tableau numpy de cellule
    i : indice de l'agrégat dans le tableau agrégat
    box : limite de l'environnement 
    agregat : liste python contenant les différents agrégats de l'environnement 


    retour 
    =========
    Retourne True si le déplacement est possible
    False sinon
    """
    
    #On vérifie d'abord sur la bordure
    nombre_cellule = len(agregat[i])
    for j in range(nombre_cellule):

        #Ces deux conditions servent à vérifier si l'aggrégat ne veut pas sortir de la box
        if (population.x[agregat[i][j]] + deplacement[0] < 0 or population.x[agregat[i][j]] + deplacement[0] > box.x_max):
            return False
        if (population.y[agregat[i][j]] + deplacement[1] < 0 or population.y[agregat[i][j]] + deplacement[1] > box.y_max):
            return False

        #cette boucle vérifie si l'aggrégat ne veut pas se déplacer vers une cellule
        for k in range(population.nombre_algues):

            #je vérifie que la cellule n'est pas dans l'aggrégat
            if(k != agregat[i][j]):
                if (np.abs(population.x[agregat[i][j]] + deplacement[0] - population.x[k]) <= 1 and np.abs(population.y[agregat[i][j]] + deplacement[1] - population.y[k]) <= 1):
                    if (population.agregat[k] == False):
                        if (dep.check_deplacement(population,k,box,deplacement) == False):
                            return False
                        else :
                            population.x[k] += deplacement[0]
                            population.y[k] += deplacement[1]
                    else :
                        if (k not in agregat[i]):
                            return False
    return True

def deplacement_agregat(population,box, agregat):
    """

    La fonction déplace toutes les cellules qui sont agrégé
    
    Paramètre 
    ===========
    population : tableau numpy de cellule
    box : tableau numpy avec les limite de notre environnement 
    agregat : liste python des différents aggrégats de notre environnement 


    Retour 
    ===========
    Ne retourne rien
    """
    
    #On parcourt tous les aggrégats
    for i in range(len(agregat)):
        deplacement = [rand.uniform(-config.DEP_MAX,config.DEP_MAX),rand.uniform(-config.DEP_MAX,config.DEP_MAX)]

        #On vérifie si le déplacement est possible
        #Si oui, alors on déplace l'aggrégat
        #Sinon, on ne fait rien
        if (check_deplacement_agregat(population,i,box,agregat,deplacement)):
            nombre_cellule = len(agregat[i])
            for j in range(nombre_cellule):
                population.x[agregat[i][j]] += deplacement[0]
                population.y[agregat[i][j]] += deplacement[1]

        
    



        