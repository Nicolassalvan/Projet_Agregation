# -*- coding: utf-8 -*-
"""
@author: Projet Multidisciplinaire Agregation algues - MAIN3 promo 2025
"""


# Module du choix des paramètres liés aux algues  



# Import des bibliothèques de PyQt5

from PyQt5.QtWidgets import QGroupBox, QGridLayout, QLabel, QSpinBox

# Import du module data 

import _settings as sett



# Définition des classes

class Alg_class(QGroupBox) :
    # Classe QGroupBox contenant les éléments permettant de choisir les paramètres des algues
     
    def __init__(self) :
        super().__init__()

            # Définition et ajout du layout
        layout = QGridLayout()
        self.setLayout(layout)

            # Choix du nom 
        self.setTitle("Parametres de l'algue")


            # Créations des différents éléments
        self.vit_label = Vit_label_class()
        self.vit_spinbox = Vit_spinbox_class()
        self.nb_label = Nb_label_class()
        self.nb_spinbox = Nb_spinbox_class()
        self.tdiv_label = Tdiv_label_class()
        self.tdiv_spinbox = Tdiv_spinbox_class()

            # Ajout des éléments au layout
        layout.addWidget(self.vit_label, 1,0)
        layout.addWidget(self.vit_spinbox,1,1)
        layout.addWidget(self.nb_label,2,0)
        layout.addWidget(self.nb_spinbox,2,1)
        layout.addWidget(self.tdiv_label,3,0)
        layout.addWidget(self.tdiv_spinbox,3,1)

#  Fin de la classe 



class Vit_label_class(QLabel) : 
    # Classe QLabel introduisant le choix de la vitesse des algues

    def __init__(self) :
        super().__init__()

            #Choix du texte
        self.setText("Vitesse moyenne : ")

# Fin de la classe



class Vit_spinbox_class(QSpinBox) : 
    # Classe QSpinbox permettant le choix de la vitesse des cellules

    def __init__(self) :
        super().__init__()

            # Choix du Suffix, de la valeur initiale, du min et du max
        self.setSuffix(" m/s")
        self.setValue(sett.vit_alg)
        self.setMinimum(sett.vit_alg_min)
        self.setMaximum(sett.vit_alg_max)

            # Connexion entre le changement de valeur et la fonction changed
        self.valueChanged.connect(self.changed)

    def changed(self) :
        # Fonction permettant d'actualiser la valeur du fichier data avec la valeur courante
        sett.vit_alg = self.value()
        
# Fin de la classe



class Nb_label_class(QLabel) : 
    # Classe QLabel introduisant le choix du nombre initial d'algues

    def __init__(self) :
        super().__init__()

            # Choix du texte
        self.setText("Nombre d'algues initial : ")

# Fin de la classe



class Nb_spinbox_class(QSpinBox) :
    # Classe QSpinbox permettant le choix du nombre initial de  cellules

    def __init__(self) :
        super().__init__()

            # Choix du Suffix, de la valeur initiale, du min et du max
        self.setSingleStep(10)
        self.setValue(sett.nb_alg)
        self.setMinimum(sett.nb_alg_min)
        self.setMaximum(sett.nb_alg_max)

            # Connexion du changement de la valeur à la fonction changed
        self.valueChanged.connect(self.changed)

    def changed(self) : 
        # Fonction permettant d'actualiser la valeur du fichier data avec la valeur courante
        sett.nb_alg = self.value()

# Fin de la classe



class Tdiv_label_class(QLabel) : 
    # Classe QLabel introduisant le choix du temps de division des algues

    def __init__(self) :
        super().__init__()

            # Choix du texte
        self.setText("Temps de division : ")

# Fin de la classe



class Tdiv_spinbox_class(QSpinBox) : 
    # Classe QSpinbox permettant le choix du temps de division des cellules

    def __init__(self) :
        super().__init__()

            # Choix du Suffix, de la valeur initiale, du min et du max
        self.setSuffix(" h")
        self.setValue(sett.TEMPS_DIV)
        self.setMinimum(sett.t_div_alg_min)
        self.setMaximum(sett.t_div_alg_max)

            # Connexion du changement de la valeur à la fonction changed
        self.valueChanged.connect(self.changed)

    def changed(self) : 
        # Fonction permettant d'actualiser la valeur du fichier data avec la valeur courante
        sett.TEMPS_DIV = self.value()

# Fin de classe 



# Fin du module 