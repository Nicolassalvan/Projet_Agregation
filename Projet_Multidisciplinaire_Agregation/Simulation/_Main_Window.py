# -*- coding: utf-8 -*-
"""
@author: Projet Multidisciplinaire Agregation algues - MAIN3 promo 2025
"""

#Programme principal, création de la fenetre principale et liens entre tous les parametres

#Développé sur Visual Studio et Spyder avec PyQt5, numpy, matplotlib, ffmpeg


# Import du système

import sys

# Import des bibliothèques PyQt5

from PyQt5.QtWidgets import QWidget, QMainWindow, QGridLayout, QApplication

# Import des modules

from GUI_Donnees import *
from GUI_Choix_Algues import *
from GUI_Choix_Stress import *
from GUI_Choix_Simulation import *
from GUI_Launch_Simulation import *

import _settings as sett

from SIM_class_algue import * 
from SIM_video_et_anim import *



# Définition de la classe de la fenètre principale



class MainWindow(QMainWindow) : 
    # Classe QMainwindow définissant la fenêtre principale de l'interface 

    print("Chargement de l'interface...")

    def __init__(self) :
        super().__init__()

            # Choix de la dimension et du nom
        self.setWindowTitle("Modélisation Chlamydomonas Reinhardtii")
        # self.setGeometry(0,0,1200,700)

            # Ajout du layout (support)
        self.layout = QGridLayout()

            # Créations des différents éléments 
        self.Intro = Intro_class()
        self.Alg = Alg_class()
        self.Stress = Stress_class()
        self.Simul= ChoixSimul_class()
        self.LaunchSimul = Simul_class()

            # Ajout des éléments au layout 
        self.layout.addWidget(self.Intro,0,0,1,2)           # le widget est en position 0,0 et occupe 1 ligne et 2 colonne
        self.layout.addWidget(self.LaunchSimul,0,2)
        self.layout.addWidget(self.Alg,1,0)
        self.layout.addWidget(self.Stress,1,1)
        self.layout.addWidget(self.Simul,1,2)

            # Création d'un central widget comprenant tous les éléments de la fenêtre principale (appel de fonction)
        self.centralWidget_f()

            # Application de la police sett.font
        self.setFont(sett.font)

            # Connection des éléments de le fenêtre et actualisation des affichages (appel de fonction)
        self.connect()
        self.actu()

        # self.show()

        self.showMaximized()            # Affichage de la fenêtre en plein écran

    def connect(self) : 
        # Fonction de connections des différents éléments de la fenètre
        self.Alg.nb_spinbox.valueChanged.connect(self.actu)

        self.Simul.larg_spinbox.valueChanged.connect(self.actu)         # Ici on connecte par exemple le changement de la valeur de la largeur de la boite à l'actualisatio des calculs affichés
        self.Simul.long_spinbox.valueChanged.connect(self.actu)
        self.Simul.tsim_spinbox.valueChanged.connect(self.actu)
        self.Simul.vitsim_combobox.currentTextChanged.connect(self.actu)
        

        self.LaunchSimul.stress_oui_radiobutton.signal.connect(self.Stress.niv_spinbox.stress_changed)
        self.LaunchSimul.stress_non_radiobutton.signal.connect(self.Stress.niv_spinbox.stress_changed)
        self.LaunchSimul.simul_button_gif.clicked.connect(self.launch_simul_gif)
        self.LaunchSimul.simul_button_mp4.clicked.connect(self.launch_simul_mp4)


    def actu(self) : 
        # Fonction d'actualisation globale de la fenètre
        self.Intro.ctes_groupbox.dens_label.actu()
        self.Intro.ctes_groupbox.surfboite_label.actu()
        self.Intro.ctes_groupbox.tvid_label.actu()

    

    def launch_simul_gif(self) : 
        # Fonction de lancement de la simulation en gif
        
        print("Chargement de la simulation en gif...")
        
        self.close()

        box = Box(sett.long_boite, sett.h_boite)
        pop = Population(sett.nb_alg, box)
        agregat = []

        gif_simulation(pop, box, agregat)

        print("Done")

    
    def launch_simul_mp4(self) : 
        # Fonction de lancement de la simulation en mp4

        print("Chargement de la simulation en mp4...")
        
        self.close()

        box = Box(sett.long_boite, sett.h_boite)
        pop = Population(sett.nb_alg, box)
        agregat = []

        video_simulation(pop, box, agregat)

        print("Done")


    def centralWidget_f(self) :             
        # definition du central Widget sur lequel poser les différents elements
 
            # Création du widget
        widget = QWidget()

            # Le Layout créé précédement est appliqué à ce widget (les éléments ajoutés au layout aussi)
        widget.setLayout(self.layout)
        
            # Le central widget est appliqué à la fenêtre
        self.setCentralWidget(widget)


    
# Fin de la classe 



# Module d'affichage de la fenêtre principale

if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = MainWindow()

    sys.exit(app.exec())