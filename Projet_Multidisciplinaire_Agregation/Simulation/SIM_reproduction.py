# -*- coding: utf-8 -*-
"""
@author: Projet Multidisciplinaire Agregation algues - MAIN3 promo 2025
"""

import numpy as np

import _settings as sett
import SIM_class_algue 
import SIM_deplacement as move

def update_age_et_reprod(population, box):
    """
    Update l'âge de chaque cellule de la population entre deux frames.Reproduit 
    les cellules si possible.
    Parameters
    ----------
    population : class Population
        Population d'algues. 
    box: class Box
        Zone de simulation. 

    Returns
    -------
    None.

    """
    for i in range(population.nombre_algues):
        age = population.age[i]
        taille = population.taille[i]

        # Pour chaque cellule, on la fait se reproduire si elle a atteint l'âge
        if (age >= sett.TEMPS_DIV):
            # Si la taille est égale à celle d'un palméloïde de 8 cellules, on reproduit 
            # la cellule c'est à dire qu'on la fait "s'éclater"
            if taille >= sett.TAILLE_8:
                # on reproduit la cellule i si possible
                reproduire(population, box, i)
            # Sinon on incrémente la taille et réinitialise l'âge
            else:
                # On incrémente la taille 
                population.taille[i] = augmenter_taille(taille)
                # On réinitialise l'âge, pour que la cellule refasse un cycle de reproduction
                population.age[i] = 0
        # Sinon la cellule est trop jeune, on incrémente son âge
        else:
            population.age[i] += 1
            
        
                    
def augmenter_taille(taille):
    """
    Renvoie la taille supérieure à celle rentrée en argument.

    Parameters
    ----------
    taille : int
        Taille de la cellule qui sera affichée.

    Returns
    -------
    - Si la taille est celle de 1 cellule, renvoie la taille de 2 cellules. 
    - Si la taille est celle de 2 cellule, renvoie la taille de 4 cellules. 
    - Si la taille est celle de 4 cellule, renvoie la taille de 8 cellules.     

    """
    if taille == sett.TAILLE_1:
        return sett.TAILLE_2
    elif taille == sett.TAILLE_2:
        return sett.TAILLE_4
    elif taille == sett.TAILLE_4:
        return sett.TAILLE_8
       
        
def reproduire(population, box, i):
    """
    Reproduit la cellule d'indice i, crée 7 nouvelles cellules autour d'elle. 
    Update l'age et la taille de la cellule mère. 
    
    Paramètres
    ----------
    population : class Population
        Population d'algues.
    box : class Box
        Zone de simulation.
    i : int
        Indice de l'algue à reproduire.

    Retours
    -------
    Aucun.

    """
    
    if is_room_for_reprod(population, box, i):
        # On update les infos de la cellule i
        population.taille[i] = sett.TAILLE_1
        population.age[i] = 0
        
        # Tableau représentant le voisinnage de la cellule i
        Tab = np.zeros((3,3,2))
        Tab[0, :, 1] = 1
        Tab[2, :, 1] = -1
        Tab[:, 0, 0] = -1
        Tab[:, 2, 0] = 1
        Tab = np.reshape(Tab, (1,9,2))
        Tab = Tab[0]
        
        # Coordonnée de l'algue qui se reproduit
        x_i = population.x[i]
        y_i = population.y[i]
        
        # Pour chaque case autour de la cellule à faire reproduire, 
        # On vérifie si il n'y a pas de cellule et si il n'y en a pas,
        # On ajoute une cellule à cette coordonnée. 
        nb_nouvelles_algues = 0
        for deplacement in Tab:
            if (deplacement[0] != 0 or deplacement[1] != 0) and nb_nouvelles_algues <8: 
                if move.check_deplacement(population, i, box, deplacement):
                    population.creer_algue(x_i+deplacement[0], y_i+deplacement[1])
                    nb_nouvelles_algues += 1
        
 


def is_room_for_reprod(population, box, i):
    
    """
    Vérifie si il la cellule i a la place pour se reproduire. 
    
    Paramètres
    ------
    population : class Population
        Population d'algues. Type décrit dans le fichier class_algues. 
    box : class Box
        Zone de simulation.
    i : int
        Indice de l'algue à reproduire.
    
    Retours
    ------
    - False si il y a plus d'une cellule dans le carré 3x3 autour de la cellule i ou si elle est
    sur le bord de la zone de simulation.
    - True si il y a moins d'une cellule dans le carré 3x3 autour de la cellule i et qu'elle
    n'est pas au bord.
    """
    # Coordonnées de l'algue 
    x_i = population.x[i]
    y_i = population.y[i]
    
    # On vérifie que la cellule n'est pas sur un bord
    if (x_i-1 < 0 or y_i-1 < 0):
        return False
    elif (x_i+1 >box.x_max or y_i+1 > box.y_max):
        return False
    
    # Nombre de voisins
    nb_voisins = 0
    # Je définis nb_max au cas où on veut changer de norme 
    nb_max = 1
    
    for j in range(population.nombre_algues):
        # Pour chaque cellule, on vérifie si elle est au voisinnage de la cellule i
        # Pour cela, on mesure la distance à l'aide de la norme infinie et si elle est 
        # Supérieure stricte à 1 alors il y a une cellule voisine
        deltax = abs(population.x[j] - x_i)
        deltay = abs(population.y[j] - y_i)
        distance_ij = max(deltay, deltax)
        if distance_ij <= 1:
            nb_voisins += 1
            # Si il y a plus d'un voisin il n'y aura pas la place pour que les cellules 
            # se reproduisent
            if nb_voisins > nb_max:
                return False
    # Si on sort de la boucle, la cellule a au plus un voisin donc elle a la place pour
    # se reproduire. 
    return True