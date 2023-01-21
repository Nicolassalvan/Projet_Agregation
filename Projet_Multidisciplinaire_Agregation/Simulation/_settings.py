    # -*- coding: utf-8 -*-
"""
@author: Projet Multidisciplinaire Agregation algues - MAIN3 promo 2025
"""
# Module contenant toutes les variables et constantes nécessaires dans différents fichiers 

from PyQt5.QtGui import QFont
import numpy as np


# Les paramètres min et max permettent de limiter les entrées possibles lors de la mise en place 
# et ainsi éviter des cas d'erreurs ou des paramètres aberants. 



#///////////////////////////////////////////////////////////////////////////#
#                  Paramètres par défaut de la simulation                   #
#///////////////////////////////////////////////////////////////////////////#

    # Diamètre d'une algue par défaut
diam_alg = 10/1000            # en mm   (10micrometres) 

    # Densité des algues dans la boite (calculée automatiquement)
dens_alg = 0

    # Taille des algues / palmelloïdes en diamètres d'une algue    
# Taille d'une cellule
TAILLE_1 = 1
# Taille d'un palméloïde de 2 cellules
TAILLE_2 = 2
# Taille d'un palméloïde de 4 cellules
TAILLE_4 = 3
# Taille d'un palméloïde de 8 cellules
TAILLE_8 = 4

    # Déplacement maximal entre chaque frame, en diamètres d'algues (calculée automatiquement)
DEP_MAX = 1         # valeur par défaut

    # Surface de la boite en mm² (calculée automatiquement)
surf_boite = 0      


    # Nombre de frames avant activation du stress (calculé automatiquement)
NB_FRAMES_STRESS = 0

#///////////////////////////////////////////////////////////////////////////#
#                Paramètres modifiables par l'utilisateur                   #
#///////////////////////////////////////////////////////////////////////////#

    # Vitesse des algues en micrometres/s
vit_alg = 10            # valeur par défaut
vit_alg_min = 0
vit_alg_max = 100

    # Nombre d'algues initial
nb_alg = 10             # valeur par défaut
nb_alg_min = 1
nb_alg_max = 2000

    # Temps de division des algues en heures !!!!!!!!!!!!CONVERSION!!!!!!!!!
TEMPS_DIV = 10          # valeur par défaut
t_div_alg_min = 5
t_div_alg_max = 50

   # Niveau de stress appliqué en % 
STRESS_USER = 0          # valeur par défaut, 0 quand l'option de stress n'est pas activé
stress_min = 0
stress_max = 100

    # Largeur de la boite en mm
long_boite = 100        # en unit (1unit = 1 diamètre d'algue en micromètres)
long_boite_min = 5
long_boite_max = 500        

    # Longueur de la boite en mm
h_boite = 100           # en unit
h_boite_min = 5         
h_boite_max = 500

    # Niveau de stress appliqué une fois le trigger atteind 
STRESS = 0.2            # entre 0 et 1


    # Trigger d'activation du stress en fonction du temps écoulé 
TRIGGER = 10            # en h
trigger_min = 1
trigger_max = 100

    # Probabilité d'agrégation entre un agrégat et une cellule
PROBA_AGREGAT = 0.2

    # Probabilité d'agrégation entre deux agrégats
PROBA_AGREGAT_NORMAL = 0.1

    # Niveau de stress minimal avant la formation d'agrégats
SEUIL_AGREGAT = 0.4     

    # Temps simulé
T_SIMUL = 2         # en jours
t_simul_min = 1
t_simul_max = 10

#Ce coefficient multiplié par STRESS, correspond à la taille minimale d'un agregat 
# pour quelle puisse se coller avec une autre
COEF = 10




#///////////////////////////////////////////////////////////////////////////#
#                           Options de la simulation                        #
#///////////////////////////////////////////////////////////////////////////#


bool_div = True     # booléen représentant la possibilité de division des algues
bool_kill = True    # booléen représentant la possibilité de mort des algues



#///////////////////////////////////////////////////////////////////////////#
#                           Produits de la simulation                       #
#///////////////////////////////////////////////////////////////////////////#


    # Taille de la population en fonction de la frame

tabNbAlgues=np.array([])



#///////////////////////////////////////////////////////////////////////////#
#                             Paramètres Interface                          #
#///////////////////////////////////////////////////////////////////////////#

    # fps de la vidéo ou du gif
FPS = 15

    # Vitesse de simulation
V_SIMUL= 1      # Rapport entre le temps réel et le temps de modélisation

    # Durée réelle de la vidéo en secondes
T_VID = 10

    # Nombre de frames de la vidéo
NB_FRAMES_TOT = 50


    # Police et taille de caractères
font = QFont('Arial', 10)

    # Messages 
message_intro = "Bienvenue, \nDans cette interface, vous avez à déterminer les différents paramètres qui seront \npris en compte pour la modéilisation\n"
message_type_stress = "Ici, le stress sera abiotique (thermqiue, hydrique, oxydatif, lumineux...).\nDans ce modèle, on associe le stress à une probabilité de survie de la cellule \net à une architecture en agregats des cellules"
message_type_stress += "\nAfin de faciliter les choix possibles, le stress sera designé en tant que pourcentage. \nDépassé 100, les cellules sont détruites par l'environnement."
message_fin = "\nBien à vous."