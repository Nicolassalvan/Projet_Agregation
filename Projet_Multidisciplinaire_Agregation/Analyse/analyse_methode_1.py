# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 00:55:49 2022

@author: cleme
"""

"""
première méthode utilisé que nous avons abandonné car nous ne 
pouvions pas différencier cellule seule, palmélloïdes et agregats
----------------------------------------
Points forts:
-Flexibilité, juste à ajuster la valeur pour le mask
-Rapide de calcul
Points faible:
-Pas accès au surface
----------------------------------------
bibliothèque utile:
numpy
imageio.v3
matplotlib
PIL
skimage
----------------------------------------

"""




import numpy as np
import imageio.v3 as iio
import skimage.color
import skimage.filters
import matplotlib.pyplot as plt
from PIL import Image



#stock dans la var l'image
#convertie en jpg si c'est en png
#pour cela il faut enlever les val en alpha avec conversion rgb
#on creer nouv image.jpg


image = Image.open("all_test_images/image_01.png")
print(image.format)

#on convertie en format rgb au cas ou il est au format RGBD qui n'est pas pris en compte par iio
rgb_image = image.convert('RGB')
rgb_image.save("image_convert.jpg")
algue_image = iio.imread(uri="image_convert.jpg")


#display image
fig, ax = plt.subplots()
plt.imshow(algue_image)
gray_image = algue_image;
#create to shades of gray
gray_image = skimage.color.rgb2gray(algue_image)
# display the gray image
fig, ax = plt.subplots()
#plt.imshow(gray_image, cmap="gray")

blurred_image = skimage.filters.gaussian(gray_image, sigma=1.0)
plt.imshow(blurred_image, cmap="gray")
histogram, bin_edges = np.histogram(blurred_image, bins=256, range=(0.0, 1.0))
fig, ax = plt.subplots()
plt.plot(bin_edges[0:-1], histogram)
plt.title("Graylevel histogram")
plt.xlabel("gray value")
plt.ylabel("pixel count")
plt.xlim(0, 1.0)



#image01 0.6 image02 0.6 image03 0.75 image04 0.7
mask = blurred_image<0.6
print(blurred_image)
fig, ax = plt.subplots()
plt.imshow(mask, cmap="gray")

#compte le nombre de cellule présente sur l'image
labeled_image, count = skimage.measure.label(mask, return_num=True)
print(count)


# color each of the colonies a different color
colored_label_image = skimage.color.label2rgb(labeled_image, bg_label=0)
# give our grayscale image rgb channels, so we can add the colored colonies
summary_image = skimage.color.gray2rgb(gray_image)
summary_image[mask] = colored_label_image[mask]

# plot overlay
fig, ax = plt.subplots()
plt.imshow(summary_image)





