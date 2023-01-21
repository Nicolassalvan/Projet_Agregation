# -*- coding: utf-8 -*-
"""
@author: Projet Multidisciplinaire Agregation algues - MAIN3 promo 2025
"""


# Module permettant le choix des paramètres liés au stress  



# Import des bibliothèques de PyQt5

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGroupBox, QGridLayout, QLabel, QComboBox, QSpinBox

# Import du module data

import _settings as sett



# Définition des classes

class Stress_class(QGroupBox) : 
    # Classe QGroupBox contenant les éléments permettant de choisir les paramètres du stress

    def __init__(self) : 
        super().__init__()

            # Choix du nom        
        self.setTitle("Parametres du stress")

            # Définition et ajout du layout
        layout = QGridLayout()
        self.setLayout(layout)

            # Création des différents éléments 
        niv_label = NivStress_label_class()
        self.niv_spinbox = NivStress_spin_class()
        seuil_label = Seuil_label_class()
        self.seuil_spinbox = Seuil_spinbox_class()
        probaagregcell_label = ProbaAgrCell_label_class()
        self.probaagregcell_spinbox = ProbaAgrCell_spin_class()
        probacellcell_label = ProbaCellCell_label_class()
        self.probacellcell_spinbox = ProbaCellCell_spin_class()
        stressagr_label = StressAgr_label_class()
        self.stressagr_spinbox = StressAgr_spin_class()
        
            # Ajouts des éléments au layout
        layout.addWidget(niv_label,0,0)
        layout.addWidget(self.niv_spinbox,0,1)
        layout.addWidget(stressagr_label,1,0)
        layout.addWidget(self.stressagr_spinbox,1,1)
        layout.addWidget(seuil_label,2,0)
        layout.addWidget(self.seuil_spinbox,2,1)
        layout.addWidget(probaagregcell_label,3,0)
        layout.addWidget(self.probaagregcell_spinbox,3,1)
        layout.addWidget(probacellcell_label,4,0)
        layout.addWidget(self.probacellcell_spinbox,4,1)


# Fin de la classe 



class NivStress_label_class(QLabel) : 
    # Classe QLabel introduisant le choix du niveau de stress
    def __init__(self) :
        super().__init__()

            # Définition du Texte
        self.setText("Niveau de stress : ")



class NivStress_spin_class(QSpinBox) :
    # Classe QSpinbox permettant le choix du niveau du stress

    def __init__(self) :
        super().__init__()

            # Choix de la valeur initiale, du suffix, du min et du max
        self.setValue(sett.STRESS_USER*100)
        self.setSuffix(" %")
        self.setMinimum(sett.stress_min)
        self.setMaximum(sett.stress_max)

            # Connexion du changement de la valeur à la fonction changed
        self.valueChanged.connect(self.changed)

    def stress_changed(self) : 
        self.setValue(sett.STRESS_USER*100)

    def changed(self) : 
        # Fonction permettant d'actualiser la valeur du fichier data avec la valeur courante
        sett.STRESS_USER = self.value() / 100

# Fin de la classe



class Seuil_label_class(QLabel) : 
    # Classe Qlabel permettant l'introduction du choix du niveau du trigger

    def __init__(self) :
        super().__init__()

            # Choix du texte
        self.setText("Seuil de déclenchement du stress : ")



class Seuil_spinbox_class(QSpinBox) : 
    # Classe QSpinBox permettant le choix de la valeur du seuil du trigger

    def __init__(self) :
        super().__init__()

        self.setSuffix(" h")
        self.setValue(sett.TRIGGER)
        self.setMinimum(sett.trigger_min)
        self.setMaximum(sett.trigger_max)
        

            # Connexion du changement de la valeur et de la fonction changed 
        self.valueChanged.connect(self.changed)


    def changed(self) :
        # Fonction permettant d'actualiser la valeur du fichier data avec la valeur courante 
        sett.TRIGGER = self.value()*60*60        # On choisit la valeur en secondes

# Fin de la classe



class ProbaAgrCell_label_class(QLabel) : 
    # Classe QLabel introduisant le choix de la probabilité d'agrégation entre un agrégat et une cellule
    def __init__(self) :
        super().__init__()

            # Définition du Texte
        self.setText("Chance d'agrégation lors de la colission Algue - Agrégat : ")

# Fin de la classe



class ProbaAgrCell_spin_class(QSpinBox) :
    # Classe QSpinbox permettant le choix de la probabilité d'agrégation entre un agrégat et une cellule

    def __init__(self) :
        super().__init__()

            # Choix de la valeur initiale, du suffix, du min et du max
        self.setValue(sett.PROBA_AGREGAT*100)
        self.setSuffix(" %")
        self.setMinimum(100)
        self.setMaximum(0)

            # Connexion du changement de la valeur à la fonction changed
        self.valueChanged.connect(self.changed)

    def changed(self) : 
        # Fonction permettant d'actualiser la valeur du fichier data avec la valeur courante
        sett.PROBA_AGREGAT= self.value() / 100

# Fin de la classe



class ProbaCellCell_label_class(QLabel) : 
    # Classe QLabel introduisant le choix de la probabilité d'agrégation entre deux cellules seules

    def __init__(self) :
        super().__init__()

            # Définition du Texte
        self.setText("Chance d'agrégation lors de la colission ALgue - Algue : ")

# Fin de la classe



class ProbaCellCell_spin_class(QSpinBox) :
    # Classe QSpinbox permettant le choix de la probabilité d'agrégation entre deux cellules seules

    def __init__(self) :
        super().__init__()

            # Choix de la valeur initiale, du suffix, du min et du max
        self.setValue(sett.PROBA_AGREGAT_NORMAL*1000)
        self.setSuffix(" /1000")
        self.setMinimum(0)
        self.setMaximum(100)
        self.setSingleStep(10)

            # Connexion du changement de la valeur à la fonction changed
        self.valueChanged.connect(self.changed)

    def changed(self) : 
        # Fonction permettant d'actualiser la valeur du fichier data avec la valeur courante
        sett.PROBA_AGREGAT_NORMAL= self.value() / 1000

# Fin de la classe



class StressAgr_label_class(QLabel) : 
    # Classe QLabel introduisant le choix de la probabilité d'agrégation entre deux cellules seules

    def __init__(self) :
        super().__init__()

            # Définition du Texte
        self.setText("Niveau de stress minimal pour l'apparition d'agrégats : ")

# Fin de la classe



class StressAgr_spin_class(QSpinBox) :
    # Classe QSpinbox permettant le choix de la probabilité d'agrégation entre deux cellules seules

    def __init__(self) :
        super().__init__()

            # Choix de la valeur initiale, du suffix, du min et du max
        self.setValue(sett.SEUIL_AGREGAT*100)
        self.setSuffix(" %")
        self.setMinimum(0)
        self.setMaximum(100)
        self.setSingleStep(10)

            # Connexion du changement de la valeur à la fonction changed
        self.valueChanged.connect(self.changed)

    def changed(self) : 
        # Fonction permettant d'actualiser la valeur du fichier data avec la valeur courante
        sett.SEUIL_AGREGAT = self.value() / 100

# Fin de la classe



# Fin du module