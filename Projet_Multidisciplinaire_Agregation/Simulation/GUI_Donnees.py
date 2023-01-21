# -*- coding: utf-8 -*-
"""
@author: Projet Multidisciplinaire Agregation algues - MAIN3 promo 2025
"""


# Module qui permet l'affichage du message d'introduction



# Import des bibliothèques de PyQt5 

from PyQt5.QtWidgets import QGroupBox, QGridLayout, QLabel

# Import du module data

import _settings as sett



# Définition des classes

class Intro_class(QGroupBox) : 
    # Classe QGroupBox contenant les différents éléments d'introduction et de calcul des constantes

    def __init__(self) : 
        super().__init__()

            # Définition et ajout du layout
        self.layout = QGridLayout()
        self.setLayout(self.layout)

            # Choix du nom
        self.setTitle("Bienvenue")

            # Création des différents éléments
        self.intro_label = Intro_label_class()
        self.typestress_label = TypeStress_label_class()
        self.ctes_groupbox = Ctes_groupbox_class()
        self.fin_label = Fin_label_class()

            # Ajout des éléments au layout
        self.layout.addWidget(self.intro_label,0,0)
        self.layout.addWidget(self.typestress_label,1,0)
        self.layout.addWidget(self.ctes_groupbox,0,1,3,1)
        self.layout.addWidget(self.fin_label,2,0)

# Fin de la classe 



class Intro_label_class(QLabel) : 
    # Classe QLabel permettant d'afficher le message d'introduction de l'interface graphique

    def __init__(self) : 
        super().__init__()

            # Choix du texte
        self.setText(sett.message_intro) 

# Fin de la classe 


class Fin_label_class(QLabel) : 
    # Classe QLabel permettant d'afficher le message de fin d'introduction de l'interface graphique

    def __init__(self) : 
        super().__init__()

            # Choix du texte
        self.setText(sett.message_fin) 

# Fin de la classe 



class TypeStress_label_class(QLabel) : 
    # Classe QLabel permettant d'afficher le message explicatif sur le choix du stress

    def __init__(self) :
        super().__init__()
        
            # Choix du texte
        self.setText(sett.message_type_stress)

# Fin de la classe 



class Ctes_groupbox_class(QGroupBox) :
    # Classe QGroupBox permettant de calculer et d'afficher les différentes constantes

    def __init__(self) :
        super().__init__()

            # Choix du nom
        self.setTitle("Données de la modélisation : ")

            # Définition et ajout du layout
        self.layout = QGridLayout()
        self.setLayout(self.layout)

            # Création des éléments
        self.surfboite_label = SurfBoite_label_class()
        self.dens_label = DensAlg_label_class()
        self.diamalg_label = DiamAlg_label_class()
        self.tvid_label = TVid_label_class()

            # Ajout des éléments au layout
        self.layout.addWidget(self.surfboite_label,0,0)
        self.layout.addWidget(self.dens_label,1,0)
        self.layout.addWidget(self.diamalg_label,2,0)
        self.layout.addWidget(self.tvid_label,3,0)

# Fin de la classe 

class SurfBoite_label_class(QLabel) : 
    # Classe QLabel permettant l'affichage de la surface de la boite

    def __init__(self) :
        super().__init__()

        self.actu()

    def actu(self) : 
        # Fonction permettant d'actualiser l'affichage avec les bonnes valeurs
            # Choix du texte
        sett.surf_boite = sett.h_boite*sett.long_boite
        self.setText("Surface de la boite : " + str(sett.surf_boite) + " mm²")

# Fin de la classe 



class DensAlg_label_class(QLabel) : 
    # Classe QLabel permettant d'afficher la densité d'algues initiale

    def __init__(self) :
        super().__init__()

            # Choix du texte 
        self.actu()

    def actu(self) : 
        # Fonction permettant d'actualiser l'affichage avec les bonnes valeurs
        sett.dens_alg = sett.nb_alg / (sett.h_boite*sett.long_boite)
            #Choix du texte
        self.setText("Densité d'algues initiale : "+ str(sett.dens_alg)+" /mm²")

# Fin de la classe



class DiamAlg_label_class(QLabel) : 
    # Classe QLabel permettant d'afficher le diamètre d'une algue

    def __init__(self) :
        super().__init__()
    
            # Choix du texte
        self.setText("Diamètre d'une algue : " + str(sett.diam_alg) + " µm")

# Fin de la classe



class TVid_label_class(QLabel) : 
    # Classe QLabel permettant d'afficher la durée de la vidéo

    def __init__(self) :
        super().__init__()
    

    def actu(self) : 
        # Fonction permettant d'actualiser l'affichage avec les bonnes valeurs

            # Actualisation de la durée de la vidéo, ici on multiplie par la vitesse car elle est < 1
        sett.T_VID = sett.T_SIMUL*24*60*60 * sett.V_SIMUL

            # Choix du texte
        self.setText("Durée de la vidéo : " + str(sett.T_VID) + " s")

            # Calcul Nb frames de la vidéo
        sett.NB_FRAMES_TOT = sett.FPS * sett.T_VID
        sett.NB_FRAMES_STRESS = sett.FPS * sett.TRIGGER * sett.V_SIMUL

# Fin de la classe


# Fin du module