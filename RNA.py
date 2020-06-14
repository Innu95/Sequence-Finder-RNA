# -*- coding: utf-8 -*-
"""
Name: Florin Alexandru
Version: 1.0

"""





import math as m
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib import colors

#Open the file text and get the RNA seq

print("Enter path of txt file:")
ruta = input()

fichero = open(ruta)
secuencia = fichero.read()

#Creating the square matrix for representation
long = len(secuencia)
matriz_tamano = m.sqrt(long)
matriz_tamano = m.ceil(matriz_tamano)
recorrido = matriz_tamano*matriz_tamano


#Giving a new asignation for adenine, cytosine, guanine, and thiamine
img = []
for x in range(recorrido):
    img.append(0)
    
    
img = np.array(img)    
for y in range(len(secuencia)):
    if(secuencia[y]=='A'):  
        img[y] = 1
    if(secuencia[y]=='C'):  
        img[y] = 2
    if(secuencia[y]=='G'):  
        img[y] = 3
    if(secuencia[y]=='T'):  
        img[y] = 4
    
seccion = len(img)


#Creating the colors asignation for the elements
cmap = colors.ListedColormap(['#FFFFFF','red' ,'yellow', 'green', 'blue'])
norm = plt.Normalize(0,4)

img_aux = img

print("Enter sequence you want to find:")
busqueda = input()

lon_gen = len(busqueda)
cont = 0 #variable used to find the positions of sequences
veces = 0 #times that appear the sequence

seq = []

#Search and find
for j in range(lon_gen):
    seq.append(0)
    
seq = np.array(seq)    

for k in range(lon_gen):
    comparador = busqueda[k]
    if(comparador=='A'):  
        seq[k] = 1
    if(comparador=='C'):  
        seq[k] = 2
    if(comparador=='G'):  
        seq[k] = 3
    if(comparador=='T'):  
        seq[k] = 4


seq = str(seq)
lista_pos = [] 

while(cont!=long):
    if(cont<long-lon_gen):
            gen = img_aux[cont:cont+lon_gen]    
    gen = str(gen)       
    if(seq==gen):
        veces+=1
        lista_pos.append(cont)
        cont = cont+lon_gen
    else:
        cont+=1


#Conclusions:
if(veces>0):
    print("The sequence you are looking for has appeared ", veces, "times in positions->", lista_pos)
else:
    print("Sequence not detected!")
   


with plt.style.context('dark_background'):        
    img = np.split(img,seccion/matriz_tamano)
    plt.imshow(img, cmap=cmap, norm=norm)
    patch_r = mpatches.Patch(color='red', label='Adenine')
    patch_y = mpatches.Patch(color='yellow', label='Cytosine')
    patch_g = mpatches.Patch(color='green', label='Guanine')
    patch_b = mpatches.Patch(color='blue', label='Thiamine')
    plt.legend(handles=[patch_r,patch_y,patch_g,patch_b], loc='center', bbox_to_anchor=(0.5, -0.05),
              fancybox=True, shadow=True, ncol=4)
    plt.show()

            
fichero.close()









