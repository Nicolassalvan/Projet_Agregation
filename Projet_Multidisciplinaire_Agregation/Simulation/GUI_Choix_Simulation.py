# -*- coding: utf-8 -*-
"""
@author: Projet Multidisciplinaire Agregation algues - MAIN3 promo 2025
"""


# Module du choix des paramètres liés à la boite  



# Import des bibliothèques de PyQt5

from PyQt5.QtWidgets import QGroupBox, QGridLayout, QLabel, QSpinBox, QComboBox

# Import du module data 

import _settings as sett



# Définition des classes

class ChoixSimul_class(QGroupBox) : 
    # Classe GroupBox contenant les éléments permettant de choisir les paramètres de la simulation

    def __init__(self) : 
        super().__init__()

            # Définition et ajout du layout 
        layout = QGridLayout()
        self.setLayout(layout)

            # Choix du nom
        self.setTitle("Parametres de la simulation")

            # Création des différents éléments
        self.long_label = Long_label_class()
        self.long_spinbox = Long_spinbox_class()
        self.larg_label = H_label_class()
        self.larg_spinbox = H_spinbox_class()
        self.tsim_label = TSimul_label_class()
        self.tsim_spinbox = TSimul_spinbox_class()
        self.vitsim_label = VitSimul_label_class()
        self.vitsim_combobox = VitSimul_combobox_class()

            # Ajout des différents éléments au layout
        layout.addWidget(self.long_label,0,0)
        layout.addWidget(self.long_spinbox,0,1)
        layout.addWidget(self.larg_label,1,0)
        layout.addWidget(self.larg_spinbox,1,1)
        layout.addWidget(self.tsim_label,2,0)
        layout.addWidget(self.tsim_spinbox,2,1)
        layout.addWidget(self.vitsim_label,3,0)
        layout.addWidget(self.vitsim_combobox,3,1)
        
# Fin de la classe 



class Long_label_class(QLabel) : 
    # Classe QLabel introduisant le choix de la longueur de la boite

    def __init__(self) : 
        super().__init__()

            # Choix du texte
        self.setText("Longueur de la boite :")

# Fin de la classe



class Long_spinbox_class(QSpinBox) : 
    # Classe QSpinbox permettant le choix de la longeur de la boite

    def __init__(self) :
        super().__init__()

            # Choix du Suffix, de la valeur initiale, du min et du max
        self.setSuffix(" mm")
        self.setValue(sett.long_boite)
        self.setMinimum(sett.long_boite_min)
        self.setMaximum(sett.long_boite_max)

            # Connexion du changement de la valeur à la fonction changed
        self.valueChanged.connect(self.changed)

    def changed(self) : 
        # Fonction permettant d'actualiser la valeur du fichier data avec la valeur courante
        sett.long_boite = self.value()

# Fin de la classe



class H_label_class(QLabel) : 
    # Classe QLabel introduisant le choix de la largeur de la boite

    def __init__(self) : 
        super().__init__()

            # Choix du texte
        self.setText("Hauteur de la boite :")

# Fin de la classe 



class H_spinbox_class(QSpinBox) : 
    # Classe QSpinbox permettant le choix de la largeur de la boite

    def __init__(self) :
        super().__init__()

            # Choix du suffix, de la valeur initiale, du min et du max
        self.setSuffix(" mm")
        self.setValue(sett.h_boite)
        self.setMinimum(sett.h_boite_min)
        self.setMaximum(sett.h_boite_max)

            # Connexion du changement de la valeur à la fonction changed
        self.valueChanged.connect(self.changed)

    def changed(self) : 
        # Fonction permettant d'actualiser la valeur du fichier data avec la valeur courante
        sett.h_boite = self.value()

# Fin de la classe



class TSimul_label_class(QLabel) : 
    # Classe QLabel introduisant le choix du temps de modélisation 

    def __init__(self) :
        super().__init__()

            # Choix du texte
        self.setText("Temps de modélisation :")

# Fin de la classe 



class TSimul_spinbox_class(QSpinBox) : 
    # Clsse QSpinbox permettant le choix du temps de simulation

    def __init__(self) :
        super().__init__()

            # Choix du Suffix, de la valeur initiale, du min et du max
        self.setValue(sett.T_SIMUL)
        self.setSuffix(" j")
        self.setMinimum(sett.t_simul_min)
        self.setMaximum(sett.t_simul_max)

            # Connexion du changement de la valeur à la fonction changed
        self.valueChanged.connect(self.changed)

    def changed(self) : 
        # Fonction permettant d'actualiser la valeur du fichier data avec la valeur courante
        sett.T_SIMUL = self.value()

# Fin de la classe 



class VitSimul_label_class(QLabel) : 
    # Classe QLabel introduisant le choix de la vitesse de simulation

    def __init__(self) :
        super().__init__()

            # Choix du texte
        self.setText("Vitesse de la simulation : ")

# Fin de la classe 



class VitSimul_combobox_class(QComboBox) : 
    # Classe QSpinbox permettant le choix de la vitesse de simulation

    def __init__(self) :
        super().__init__()

            # Choix du Suffix, de la valeur initiale, du min et du max
        self.addItem("1s/3h")
        self.addItem("1s/1h")
        self.addItem("1s/20min")

            # Connexion du changement de la valeur à la fonction changed
        self.currentTextChanged.connect(self.changed)
        self.changed()

    def changed(self) : 
        # Fonction permettant d'actualiser la valeur du fichier data avec la valeur courante
        if (self.currentText() == "1s/20min") : 
            sett.V_SIMUL = 1 / (60*20)              # Comme une carte, on exprime le rapport en 1/1200ième 
        
        elif (self.currentText() == "1s/1h") :
            sett.V_SIMUL = 1 / (60*60)

        else : 
            sett.V_SIMUL = 1 / (60*60*3)


# Fin de la classe 



# Fin du module