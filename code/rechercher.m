% Version Matlab : R2019a
% Systeme d'exploitation : Windows

function listedist = rechercher(nomImage,nomRepertoire)
% Rechercher les images similaires à l'image requête
% function listedist = rechercher(nomImage,nomRepertoire)
% ****************************************************************            
% Auteur: Isabelle EYSSERIC
% Paramètres entrée : 
%   nomImage: Chemin absolu de l'image requête
%   nomRepertoire: Chemin absolu du répertoire contenant la base
%                  de données d'images indexées
% Paramètre sortie : 
%   listedist: tableau de structures trié. Une structure comprend
%              2 champs: le nom de l'image et la distance calculée.
% ****************************************************************
    
    % Image requete
    imageRequete = imread(nomImage); 

    % Repertoire cible
    repIndex = strcat(nomRepertoire,'\index');
    liste = strcat(repIndex,'\*.txt');
    listeRep = ls(liste);   
    tailleListe = length(listeRep);

    % Histogramme de couleurs de h1
    h1_256 = zeros(256,256,256); 
    taille1_256 = size(h1_256);
    for x=1:taille1_256(1)
        for y=1:taille1_256(2)
            r = imageRequete(x,y,1)+1; 
            g = imageRequete(x,y,2)+1; 
            b = imageRequete(x,y,3)+1;
            h1_256(r,g,b) = (h1_256(r,g,b)+1)/numel(imageRequete);
        end
    end

    % Quantification de h1
    N = 4; 
    h1 = zeros(N,N,N);
    for i=1:N
        for j=1:N
            for k=1:N
                somme=sum(sum(sum(h1_256(N*i-3:N*i,N*j-3:N*j,N*k-3:N*k))));
                h1(i,j,k) = somme;
            end
        end
    end

    % Filtrage 
    Mrgb = medfilt3(h1);
    
    % Distance euclidienne entre les images
    listeDistance = struct([]);
    for i = 1:tailleListe
        
        % Lecture des images indexées
        img1 = listeRep(i:i,:); img2 = strcat(repIndex,'\',img1);        
        fopen(img2,'r'); file = load(img2); h2 = reshape(file,[4,4,4]);
        img3 = img1(1:3); img4 = strcat(img3,'.jpg'); % Noms dans listedist
        
        % Calcul de la distance pour chaque canal
        FRed   = sum((Mrgb(:,:,1)-h2(:,:,1)).^2);
        FGreen = sum((Mrgb(:,:,1)-h2(:,:,1)).^2);
        FBlue  = sum((Mrgb(:,:,1)-h2(:,:,1)).^2);
        F = sum( sqrt( FBlue + FRed + FGreen ) )/4;
        
        % Mise à jour de la structure de sortie
        listeDistance(i).nom = img4;
        listeDistance(i).distanceTotale = F;
        fclose('all');
        
    end

    % Tri croissant
    T = struct2table(listeDistance); 		    % Convertion pour le tri
    T = sortrows(T,'distanceTotale','ascend');  % Tri croissant
    listedist = table2struct(T);     		    % Convertion pour sortie
    listedist = listedist(1:5);      		    % Les 5 plus similaires
    
end
