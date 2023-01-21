# -*- coding: utf-8 -*-
"""
@author: Projet Multidisciplinaire Agregation algues - MAIN3 promo 2025
"""



# Interface graphique
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, writers, PillowWriter

import numpy as np

import _settings as config
import SIM_class_algue as algue
import SIM_deplacement as move
import SIM_agregat as aggr
import SIM_reproduction as reprod
import SIM_mort as mort

# ===== CREATION D'UN FICHIER .mp4 ===== #

def video_simulation(population, rectangle, agregat):
    """
    Lance la simulation de la population dans la zone délimitée par un rectangle. 
    Créé un fichier .mp4 à partir du déroulement de la simulation.
    Utilise la fonction update_frame pour update l'état de la population.
    Paramètres
    ----------
    population : class Population
        Population d'algues.
    rectangle : Box
        Zone de simulation.
    Retours
    -------
    None.
    """
    # initialisation du plot
    plt.close('all')

    fig, ax = plt.subplots()

    ax.set_xlim(-5, rectangle.x_max + 5)
    ax.set_ylim(-5, rectangle.x_max + 5)

    scat = ax.scatter([], [], s=5)



    # Enesemble de frames
    _frames=np.arange(0, config.NB_FRAMES_TOT)
    
    # initialisation de l'animation
    animation = FuncAnimation(
        fig, func=animation_frame, frames=_frames,
        fargs=(population, rectangle, agregat, scat), interval=50)

    # Initialisations du writer
    writer = writers['ffmpeg']
    writer = writer(fps=config.FPS, metadata={'artist': 'me'}, bitrate=1800)

    animation.save("Modélisation_Algues_{}.mp4".format(config.STRESS), writer)

    # Pour créer un graphique du nombre d'algues en fonction du temps, enlever le commentaire suivant
    # Et celui dans animation_frame
    """
    #Graph Stats
    figure=plt.figure(figsize=(100,100))
    plt.plot(_frames,config.tabNbAlgues[:-1],label="Nombre d'algues")
    plt.xlabel("frames")
    plt.ylabel("Nombre d'algues")
    plt.legend()
    plt.show()
    plt.savefig("Stats.png")
    """


# ===== CREATION D'UN GIF ===== #    

def gif_simulation(population, rectangle, agregat):
    """
    Lance la simulation de la population dans la zone délimitée par un rectangle. 
    Créé un fichier .gif à partir du déroulement de la simulation.
    Utilise la fonction update_frame pour update l'état de la population.
    Paramètres
    ----------
    population : class Population
        population d'algues.
    rectangle : Box
        zone de simulation.
    aggregat : Liste des aggrégats
    Retours
    -------
    Aucun.    
    """
    # initialisation du plot
    plt.close('all')

    fig, ax = plt.subplots()

    ax.set_xlim(-5, rectangle.x_max + 5)
    ax.set_ylim(-5, rectangle.x_max + 5)

    scat = ax.scatter([], [], s=5)

    
    # Ensemble de frames
    _frames = np.arange(0, int(config.NB_FRAMES_TOT))

    # initialisation de l'animation
    animation = FuncAnimation(
        fig, func=animation_frame, frames=_frames,
        fargs=(population, rectangle,agregat,scat), interval=50)

    # Initialisations du writer
    writer = PillowWriter(fps=15, metadata={'artist': 'me'}, bitrate=1800)

    animation.save("Modélisation_Algues_stress_{}.gif".format(config.STRESS), writer)

    # Pour créer un graphique du nombre d'algues en fonction du temps, enlever le commentaire suivant
    # Et celui dans animation_frame
    """
    #Graph Stats
    figure=plt.figure(figsize=(100,100))
    plt.plot(_frames,config.tabNbAlgues[:-1],label="Nombre d'algues")
    plt.xlabel("frames")
    plt.ylabel("Nombre d'algues")
    plt.legend()
    plt.show()
    plt.savefig("Stats.png")
    """
    




# ===== FONCTION QUI MET A JOUR LA POPULATION ===== #

def animation_frame(i, population, rect, agregat, scat):
    """
    Update chaque frame de l'animation en mettant à jour les morts, les reproductions, 
    l'aggrégation, les déplacements et l'âge des algues de la population. 
    
    Paramètres
    ------
    i: int
        numero de la frame
    population: class population 
        population d'algues
    rect: class Box
        rectangle dans lequel sont simulées les algues
    aggregat : Liste des aggrégats
        
    Retour
    ------
    Aucun
    """
    
    # On active le stress si la durée est dépassée
    if i >= config.NB_FRAMES_STRESS:
        config.STRESS = config.STRESS_USER
        
    # On met à jour la population avec les cellules qui meurent

    if (config.bool_kill and config.STRESS > 0):
        mort.update_mort(population)
    
    # On met à jour les aggrégats 
    if (config.STRESS > 0):
        # Mise a jour des cellules qui s'agregent entre elles
        aggr.update_agregat(population,agregat)
        # Mise a jour des agregats qui fusionnent
        aggr.update_agregat2(population, agregat)

    # On met à jour l'âge et la reproduction des cellules
    if  config.bool_div and population.nombre_algues < config.nb_alg_max:
        reprod.update_age_et_reprod(population, rect)
        
    # On met à jour les déplacements des algues et des agrégats
    move.deplacement_cellule(population, rect)
    if len(agregat) > 0 :
        aggr.deplacement_agregat(population, rect, agregat)

    # Pour créer un graphique du nombre d'algues en fonction du temps, enlever le commentaire suivant
    """
    # Update le array du nombre d'algues par frame 
    config.tabNbAlgues=np.append(config.tabNbAlgues,population.nombre_algues)
    """
    
        
    # Update de l'animation avec un scatter
    data = np.c_[population.x, population.y]
    scat.set_offsets(data)
    scat.set_sizes(population.taille)