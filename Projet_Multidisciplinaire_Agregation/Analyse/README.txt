---- * Analyse successive d'images d'algues unicelullaires Chlamydomonas Reinhardtii * ----


---- * Bibliothèques nécessaires pour faire fonctionner le code correctement * ----
cv2
numpy 
math
os
matplotlib.pyplot

---- * * ----


Voici les parties de code les plus utiles (et fonctionnelles) pour l'analyse d'un grand nombre d'images tirées 
de la vidéo présente ici https://dropsu.sorbonne-universite.fr/s/8TbeAXKwMAPMs9w/download (voir FOV_2_20fps)
Le grand nombre d'autres données présentes ont étés utiles pour affiner les algorithmes de détection. 
Les nombreux codes provisoires et "essais" ne figurent pas dans ce projet.

---- * Pour utiliser le code * ----

--- * Etape 0 * ---
Si dossier "image_frame_video" et "video" non vide, supprimer tout les fichiers dedans

--- * Etape 1 * ---
Télecharger la video FOV_2_20fps (lien plus haut)

--- * Etape 2 * ---
Glisser la vidéo dans le dossier "video" du projet 

--- * Etape 3 * ---
Utiliser le code "extraction_video" pour extraire chaque frame de la vidéo FOV_2_20fps dans le dossier "image_frame_video".

--- * Etape 4 * ---
Utiliser le code "analyse_images" pour lancer l'analyse, ceci peut prendre un quelques minutes en fonction de la machine

--- * FIN * ---




N.B : certains paramètres du code analyse_image peuvent être modifiés tels que le filtre hsv (ligne 57)
La méthode de comptage utilisée aura également un effet drastique sur les résultats de l'analyse