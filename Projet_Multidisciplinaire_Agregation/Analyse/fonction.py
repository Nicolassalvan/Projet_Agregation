# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 23:50:42 2023

@author: cleme
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Dec 30 15:01:21 2022

@author: cleme
"""

import numpy as np

"""
pseudo code pour plus grande des agregats
pour chaque cellule/agregat ont fait le contour
on stock la valeur (perimetre ou air du contour)
on trie le tableau de maniere croissante ou decroissante de sorte que récuperer les val min max soit simple
on prend la taille du plus petit et on le set en taille minim de cellule
on calcule dans un nv tableau de taille meme que celui contenant perimetre/air
on calcule le nombre de cellule correspondant pour chaque en divisant l'air par l'air du plus petit élément
"""

#on prend l'hypothese ou au moins une cellule isolé
def nombre_cell(tab_taille_cell):
    """
    On prend l'hypothese que le plus petit élément dans le tableau est une cellule seule. 
    
    Parameters
    ----------
    tab_taille_cell : TYPE TABLEAU
        Tableau contenant les différentes surfaces des contours trouvées.

    Returns
    -------
    TYPE INT
    On va faire la somme des surfaces et la divisé par la taille pour obtenir le nombre
    de céllules présentes sur l'image.
    """
    
    taille_min_cell = np.min(tab_taille_cell)
    return np.sum(tab_taille_cell//taille_min_cell)


    
    