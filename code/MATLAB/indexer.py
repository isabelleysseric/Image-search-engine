# Version Matlab : R2019a
# Systeme d'exploitation : Windows

import numpy as np
    
def indexer(nomRepertoire = None): 
    # Indexer une base de données d'images
# function indexer(nomRepertoire)
# ****************************************************************
# Auteur: Isabelle EYSSERIC
# Paramètre:
#   nomRepertoire: Chemin absolu du répertoire contenant la base
#                  de données d'images
# ****************************************************************
    
    # Création du dossier d'indexation
    index = strcat(nomRepertoire,'\index')
    mkdir(index)
    # Informations sur la base d'images
    liste = strcat(nomRepertoire,'\*.jpg')
    listeRep = ls(liste)
    tailleListe = len(listeRep)
    # Histogramme des images
    for a in np.arange(1,tailleListe+1).reshape(-1):
        # Préparation du format texte
        im1 = strcat(nomRepertoire,'\',listeRep(np.arange(a,a+1),:))
        im2 = listeRep(np.arange(a,a+1),:)
        im3 = im2(np.arange(1,3+1))
        im4 = strcat(im3,'.txt')
        im5 = strcat(nomRepertoire,'\index\',im4)
        open(im5,'w')
        # Histogramme de couleurs
        imageCible = imread(im1)
        h256 = np.zeros((256,256,256))
        taille256 = h256.shape
        # Histogramme de couleurs
        for x in np.arange(1,taille256(1)+1).reshape(-1):
            for y in np.arange(1,taille256(2)+1).reshape(-1):
                r = imageCible(x,y,1) + 1
                g = imageCible(x,y,2) + 1
                b = imageCible(x,y,3) + 1
                h256[r,g,b] = (h256(r,g,b) + 1) / np.asarray(imageCible).size
        # Quantification
        N = 4
        h64 = np.zeros((N,N,N))
        for i in np.arange(1,N+1).reshape(-1):
            for j in np.arange(1,N+1).reshape(-1):
                for k in np.arange(1,N+1).reshape(-1):
                    somme = sum(sum(sum(h256(np.arange(4 * i - 3,4 * i+1),np.arange(4 * j - 3,4 * j+1),np.arange(4 * k - 3,4 * k+1)))))
                    h64[i,j,k] = somme
        # Filtrage
        Mrgb = medfilt3(h64)
        # Signature de de l'image
        writematrix(Mrgb,im5,'Delimiter','tab')
        'all'.close()
    
    return
    
