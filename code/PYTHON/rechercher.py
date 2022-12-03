# Version Matlab : R2019a
# Systeme d'exploitation : Windows

import numpy as np
    
def rechercher(nomImage = None,nomRepertoire = None): 
    # Rechercher les images similaires à l'image requête
# function listedist = rechercher(nomImage,nomRepertoire)
# ****************************************************************
# Auteur: Isabelle EYSSERIC
# Paramètres entrée :
#   nomImage: Chemin absolu de l'image requête
#   nomRepertoire: Chemin absolu du répertoire contenant la base
#                  de données d'images indexées
# Paramètre sortie :
#   listedist: tableau de structures trié. Une structure comprend
#              2 champs: le nom de l'image et la distance calculée.
# ****************************************************************
    
    # Image requete
    imageRequete = imread(nomImage)
    # Repertoire cible
    repIndex = strcat(nomRepertoire,'\index')
    liste = strcat(repIndex,'\*.txt')
    listeRep = ls(liste)
    tailleListe = len(listeRep)
    # Histogramme de couleurs de h1
    h1_256 = np.zeros((256,256,256))
    taille1_256 = h1_256.shape
    for x in np.arange(1,taille1_256(1)+1).reshape(-1):
        for y in np.arange(1,taille1_256(2)+1).reshape(-1):
            r = imageRequete(x,y,1) + 1
            g = imageRequete(x,y,2) + 1
            b = imageRequete(x,y,3) + 1
            h1_256[r,g,b] = (h1_256(r,g,b) + 1) / np.asarray(imageRequete).size
    
    # Quantification de h1
    N = 4
    h1 = np.zeros((N,N,N))
    for i in np.arange(1,N+1).reshape(-1):
        for j in np.arange(1,N+1).reshape(-1):
            for k in np.arange(1,N+1).reshape(-1):
                somme = sum(sum(sum(h1_256(np.arange(N * i - 3,N * i+1),np.arange(N * j - 3,N * j+1),np.arange(N * k - 3,N * k+1)))))
                h1[i,j,k] = somme
    
    # Filtrage
    Mrgb = medfilt3(h1)
    # Distance euclidienne entre les images
    listeDistance = struct([])
    for i in np.arange(1,tailleListe+1).reshape(-1):
        # Lecture des images indexées
        img1 = listeRep(np.arange(i,i+1),:)
        img2 = strcat(repIndex,'\',img1)
        open(img2,'r')
        file = scipy.io.loadmat(img2)
        h2 = np.reshape(file, tuple(np.array([4,4,4])), order="F")
        img3 = img1(np.arange(1,3+1))
        img4 = strcat(img3,'.jpg')
        # Calcul de la distance pour chaque canal
        FRed = sum((Mrgb(:,:,1) - h2(:,:,1)) ** 2)
        FGreen = sum((Mrgb(:,:,1) - h2(:,:,1)) ** 2)
        FBlue = sum((Mrgb(:,:,1) - h2(:,:,1)) ** 2)
        F = sum(np.sqrt(FBlue + FRed + FGreen)) / 4
        # Mise à jour de la structure de sortie
        listeDistance(i).nom = img4
        listeDistance(i).distanceTotale = F
        'all'.close()
    
    # Tri croissant
    T = struct2table(listeDistance)
    
    T = sortrows(T,'distanceTotale','ascend')
    
    listedist = table2struct(T)
    
    listedist = listedist(np.arange(1,5+1))
    
    return listedist
    
    return listedist