# -*- coding: utf-8 -*-
"""
@author: Projet Multidisciplinaire Agregation algues - MAIN3 promo 2025
"""


# Module qui permet le lancement de la simulation



# Import des bibliothèque PyQt5

from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QButtonGroup, QGroupBox, QGridLayout, QPushButton, QRadioButton, QLabel

# Import du module data

import _settings as sett



# Définition des classes

class Simul_class(QGroupBox) :
    # Classe QGroupbox contenant les éléments permettant de choisir les paramètres du lancement de la simulation

    def __init__(self) : 
        super().__init__()

            # Choix et ajout du layout 
        layout = QGridLayout()
        self.setLayout(layout)

            # Choix du nom
        self.setTitle("Simulation")

            # Création des éléments 
        self.choixstress_label = ChoixStress_label_class()
        self.choixdiv_label = ChoixDiv_label_class()
        self.choixkill_label = ChoixKill_label_class()


            # Création d'un groupe de bouttons (ici pour le choix d'application ou non d'un stress lors de la simulation)
        self.grpbutton_stress = QButtonGroup()                
        self.grpbutton_stress.setExclusive(True)                               # Les bouttons ne peuvent etre selectionnés en même temps
        self.stress_oui_radiobutton = ChoixStressOui_radiobutton_class()            #  Création d'un boutton oui
        self.stress_non_radiobutton = ChoixStressNon_radiobutton_class()         # Création d'un boutton non
        self.grpbutton_stress.addButton(self.stress_oui_radiobutton)           # Ajout des bouttons au groupe de bouttons
        self.grpbutton_stress.addButton(self.stress_non_radiobutton)


        self.grpbutton_div = QButtonGroup()                
        self.grpbutton_div.setExclusive(True)                               # Les bouttons ne peuvent etre selectionnés en même temps
        self.div_oui_radiobutton = ChoixDivOui_radiobutton_class()            #  Création d'un boutton oui
        self.div_non_radiobutton = ChoixDivNon_radiobutton_class()         # Création d'un boutton non
        self.grpbutton_div.addButton(self.div_oui_radiobutton)           # Ajout des bouttons au groupe de bouttons
        self.grpbutton_div.addButton(self.div_non_radiobutton)


        self.grpbutton_kill = QButtonGroup()                
        self.grpbutton_kill.setExclusive(True)                               # Les bouttons ne peuvent etre selectionnés en même temps
        self.kill_oui_radiobutton = ChoixKillOui_radiobutton_class()            #  Création d'un boutton oui
        self.kill_non_radiobutton = ChoixKillNon_radiobutton_class()         # Création d'un boutton non
        self.grpbutton_kill.addButton(self.kill_oui_radiobutton)           # Ajout des bouttons au groupe de bouttons
        self.grpbutton_kill.addButton(self.kill_non_radiobutton)



            # Création d'un boutton permettant de lancer la simulation en format gif
        self.simul_button_gif = QPushButton("Lancer la simulation : gif", self)
        self.simul_button_gif.setStyleSheet("background-color: white")      # Choix de la couleur de fond

            # Création d'un boutton permettant de lancer la simulation en format mp4
        self.simul_button_mp4 = QPushButton("Lancer la simulation : mp4", self)
        self.simul_button_mp4.setStyleSheet("background-color: white")      # Choix de la couleur de fond

            # Ajout des éléments au layout
        layout.addWidget(self.choixstress_label,0,0)
        layout.addWidget(self.stress_oui_radiobutton,0,1)
        layout.addWidget(self.stress_non_radiobutton,0,2)

        layout.addWidget(self.choixdiv_label,1,0)
        layout.addWidget(self.div_oui_radiobutton,1,1)   
        layout.addWidget(self.div_non_radiobutton,1,2)    

        layout.addWidget(self.choixkill_label,2,0)
        layout.addWidget(self.kill_oui_radiobutton,2,1)   
        layout.addWidget(self.kill_non_radiobutton,2,2) 
           
        layout.addWidget(self.simul_button_gif,3,0)
        layout.addWidget(self.simul_button_mp4,4,0)

    
# Fin de la classe



class ChoixStress_label_class(QLabel) : 
    # Classe QLabel introduisant le choix de l'application d'un stress lors de la simulation

    def __init__(self) :
        super().__init__()

            # Choix du texte
        self.setText("Voulez-vous appliquer un stress lors de la modélisation ?")

# Fin de la classe



class ChoixStressOui_radiobutton_class(QRadioButton) : 
    # Classe QRadioButton permettant le choix du stress lors de la simulation

    signal = pyqtSignal(bool) 

    def __init__(self) :
        super().__init__()

        self.setText("Oui")
        self.setChecked(True)

        self.clicked.connect(self.clicked_f)
    
    def clicked_f(self) : 
        sett.stress_niv = 0.05
        self.signal.emit(True) 



# Fin de classe



class ChoixStressNon_radiobutton_class(QRadioButton) : 
    # Classe QRadioButton permettant le choix du stress lors de la simulation

    signal = pyqtSignal(bool)       # Le signal permet d'envoyer une information vers les parents du widget 

    def __init__(self) :
        super().__init__()

        self.setText("Non")
    
        self.clicked.connect(self.clicked_f)
    
    def clicked_f(self) : 
        # Fonction d'actualisation des variables de _settings.py

        sett.stress_niv = 0
        self.signal.emit(True)      # Ici on emet un signal pour modifier l'affichage du niveau de stress si le choix change dans cette partie

# Fin de classe



class ChoixDiv_label_class(QLabel) : 
    # Classe QLabel introduisant le choix de la division des cellules lors de la simulation

    def __init__(self) :
        super().__init__()

            # Choix du texte
        self.setText("Division des cellules lors de la simulation : ")

# Fin de la classe



class ChoixDivOui_radiobutton_class(QRadioButton) : 
    # Classe QRadioButton permettant le choix de la division des cellules lors de la simulation

    signal = pyqtSignal(bool) 

    def __init__(self) :
        super().__init__()

        self.setText("Oui")
        self.setChecked(True)

        self.clicked.connect(self.clicked_f)

    def clicked_f(self) : 
        # Fonction d'actualisation des variables de _settings.py
        
        sett.bool_div = True

# Fin de classe



class ChoixDivNon_radiobutton_class(QRadioButton) : 
    # Classe QRadioButton permettant le choix de la division des cellules lors de la simulation

    signal = pyqtSignal(bool) 

    def __init__(self) :
        super().__init__()

        self.setText("Non")

        self.clicked.connect(self.clicked_f)

    def clicked_f(self) : 
        # Fonction d'actualisation des variables de _settings.py

        sett.bool_div = False

# Fin de classe



class ChoixKill_label_class(QLabel) : 
    # Classe QLabel introduisant le choix de la mort des cellules lors de la simulation

    def __init__(self) :
        super().__init__()

            # Choix du texte
        self.setText("Mort des cellules lors de la simulation : ")

# Fin de la classe



class ChoixKillOui_radiobutton_class(QRadioButton) : 
    # Classe QRadioButton permettant le choix de la mort des cellules lors de la simulation

    def __init__(self) :
        super().__init__()

        self.setText("Oui")
        self.setChecked(True)
    
        self.clicked.connect(self.clicked_f)

    def clicked_f(self) : 
        # Fonction d'actualisation des variables de _settings.py

        sett.bool_kill = True

# Fin de classe



class ChoixKillNon_radiobutton_class(QRadioButton) : 
    # Classe QRadioButton permettant le choix de la mort des cellules lors de la simulation

    def __init__(self) :
        super().__init__()

        self.setText("Non")

        self.clicked.connect(self.clicked_f)
        
    def clicked_f(self) : 
        # Fonction d'actualisation des variables de _settings.py
        
        sett.bool_kill = False


# Fin de classe



# Fin du module