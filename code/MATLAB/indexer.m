% Version Matlab : R2019a
% Systeme d'exploitation : Windows

function indexer(nomRepertoire)
% Indexer une base de données d'images
% function indexer(nomRepertoire)
% ****************************************************************            
% Auteur: Isabelle EYSSERIC        
% Paramètre: 
%   nomRepertoire: Chemin absolu du répertoire contenant la base 
%                  de données d'images 
% ****************************************************************

    % Création du dossier d'indexation
    index = strcat(nomRepertoire,'\index');
    mkdir (index);

    % Informations sur la base d'images
    liste = strcat(nomRepertoire,'\*.jpg');
    listeRep = ls(liste);   
    tailleListe = length(listeRep);

    % Histogramme des images
    for a = 1:tailleListe

        % Préparation du format texte
        im1 = strcat(nomRepertoire,'\',listeRep(a:a,:)); 
        im2 = listeRep(a:a,:); im3 = im2(1:3); im4 = strcat(im3,'.txt');
        im5 = strcat(nomRepertoire,'\index\',im4); 
        fopen(im5,'w');

        % Histogramme de couleurs
        imageCible = imread(im1);
        h256 = zeros(256,256,256); 
        taille256 = size(h256);

        % Histogramme de couleurs
        for x=1:taille256(1)       
            for y=1:taille256(2)          
                r = imageCible(x,y,1)+1; 
                g = imageCible(x,y,2)+1;
                b = imageCible(x,y,3)+1; 
                h256(r,g,b) = (h256(r,g,b)+1)/numel(imageCible);                  
            end
        end 

        % Quantification
        N = 4; 
        h64 = zeros(N,N,N);
        for i=1:N
            for j=1:N
                for k=1:N
                    somme = sum(sum(sum(h256(4*i-3:4*i,4*j-3:4*j,4*k-3:4*k))));
                    h64(i,j,k) = somme;
                end
            end
        end

        % Filtrage
        Mrgb = medfilt3(h64);
        
        % Signature de de l'image
        writematrix(Mrgb,im5, 'Delimiter' , 'tab');
        fclose('all');

    end

end