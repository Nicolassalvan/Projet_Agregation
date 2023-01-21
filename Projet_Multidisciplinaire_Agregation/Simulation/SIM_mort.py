# -*- coding: utf-8 -*-
"""
@author: Projet Multidisciplinaire Agregation algues - MAIN3 promo 2025
"""

import numpy as np
import SIM_class_algue as algue
import _settings as sett


def update_mort(population):
    """
    Met à jour la suppression d'algue en fonction du stress.

    Parametres:
    ------
    population: class population
        représente une population d'algues
    settings.STRESS est constant
    """
    tab_mort=np.array([])
    for i in range(population.nombre_algues):
        if(population.agregat[i]==False and np.random.binomial(1,sett.STRESS,1)==1):
            tab_mort=np.append(tab_mort,i)
    population.supprimer_algue(tab_mort.astype(int))
