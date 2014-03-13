#! /usr/bin/env python
# -*- coding:Utf-8 -*-
'''

Created on 2014-03-10

@author: Michel Tremblay #111092463
'''
__author__ = "Michel Tremblay NI 111092463"
from piece import Piece


class Damier:
    """
    Classe représentant le damier d'un jeu de dames.
    """

    def __init__(self):
        """
        Méthode spéciale initialisant un nouveau damier.
        """
        # Dictionnaire de cases. La clé est une position (ligne, colonne), et la valeur une instance de la classe Piece.
        self.cases = {}

        # Appel de la méthode qui initialise un damier par défaut.
        self.initialiser_damier_par_default()

    def get_piece(self, position):
        """
        Récupère une pièce dans le damier.

        :param position: La position où récupérer la pièce.
        :type position: Tuple de coordonnées matricielles (ligne, colonne).
        :return: La pièce à cette position s'il y en a une, None autrement.
        """
        if (position in self.cases):
            return self.cases[(position)]
        else:
            return None
     
    def position_valide(self, position):
        """
        Vérifie si une position est valide (chaque coordonnée doit être dans les bornes).

        :param position: Un couple (ligne, colonne).
        :type position: tuple de deux éléments
        :return: True si la position est valide, False autrement
        """
        if(isinstance(position[0],int) and isinstance(position[1],int)): # verification que c'est un int
            if(position[0] >= 0 and position[0] <8 and position[1] >=0 and position[1] <8): # verification que le chiffre est dans le damier
                return True
            else:
                return False
        

    def lister_deplacements_possibles_a_partir_de_position(self, position, doit_prendre=False):
        """
        Cette méthode retourne une liste de positions qui sont accessibles par une pièce qui est placée sur la
        position reçue en paramètres. Un paramètre "doit_prendre" indique si la liste des positions retournée ne doit
        contenir que les positions résultant de la prise d'une autre pièce.

        Il y a donc au maximum 8 positions retournées:
        - Les 4 diagonales (les positions doivent être valides, et aucune autre pièce ne doit s'y trouver);
        - Les 4 sauts en diagonale (les positions doivent être valide, aucune pièce ne doit s'y trouver, et on doit
        sauter par dessus une pièce adverse.

        N'oubliez pas qu'un pion ne peut qu'avancer (et non reculer), mais peut effectuer une prise dans n'importe
        quelle direction. N'oubliez pas non plus qu'une dame peut avancer et reculer.

        :param position: La position de départ du déplacement.
        :type position: Tuple de deux éléments (ligne, colonne)
        :param doit_prendre: Indique si oui ou non on force la liste de positions à ne contenir que les déplacements
                             résultants de la prise d'une pièce adverse.
        :type doit_prendre: Booléen.
        :return: Une liste de positions où il est possible de se déplacer depuis la position "position".
        """
        #verification si c'est une dame ou un pion et creation des diagonale possible pour chacune d'elle
        possibilite = list()
        piece = self.cases[position]
        lig = position[0]
        col = position[1]
        
        #on crée les 4 possibilité et on vérifie leur possibilite 
        possibiliteNonVerifie = ((lig+1,col+1),(lig+1,col-1),(lig-1,col+1),(lig-1,col-1))
        
        
        for lig1,col1 in possibiliteNonVerifie: # iteration dans les possibilité
            # verification si la position est valide, si on doit prendre piece, et si il y a pas de piece a cette position
            if (self.position_valide((lig1,col1)) and doit_prendre == False and not self.get_piece((lig1,col1))): 
                if(piece.est_pion() and piece.est_blanc() and lig1<lig): # on verifie si c'est un pion blanc on peut juste monter
                    possibilite.append((lig1,col1))
                elif(piece.est_pion() and piece.est_noir() and lig1>lig):# on verifie si c'est un pion noir on peut juste descendre
                    possibilite.append((lig1,col1))
                elif(piece.est_dame()):
                    possibilite.append((lig1,col1))
  
            elif (self.get_piece((lig1,col1))): # si la position était invalide ou il y avait une piece ou on doit prendre, on regarde si cette position il y a une piece
                nouvPiece = self.cases[(lig1,col1)] # on assigne la piece à nouvPiece pous la piece à etre mangé
                if (nouvPiece.couleur != piece.couleur): # si la piece dans le chemin est pas de la même couleur, on peut la manger
                    if (lig1>lig and col1>col): lig2,col2 = (lig1+1,col1+1) #on doit rester sur la même trajectoir quand on saute sur une piece
                    elif (lig1>lig and col1<col): lig2,col2 = (lig1+1,col1-1)
                    elif (lig1<lig and col1>col): lig2,col2 = (lig1-1,col1+1)
                    elif (lig1<lig and col1<col): lig2,col2 = (lig1-1,col1-1)
                    if(self.position_valide((lig2,col2)) and not self.get_piece((lig2,col2))): # si la nouvelle destination est valide et qu'elle a pas de piece on l'ajoute
                        possibilite.append((lig2,col2))
 
        if (possibilite):        
            return possibilite
        else:
            return None
        
   
    def lister_deplacements_possibles_de_couleur(self, couleur, doit_prendre=False):
        """
        Fonction retournant la liste des positions (déplacements) possibles des pièces d'une certaine couleur. Encore
        une fois, un paramètre permet d'indiquer si on ne désire que les positions résultant de la prise d'une pièce
        adverse.

        ATTENTION: ne dupliquez pas de code déjà écrit! Réutilisez les fonctions déjà programmées!

        :param couleur: La couleur ("blanc", "noir") des pièces dont on considère le déplacement.
        :type couleur: string
        :param doit_prendre: Indique si oui ou non on force la liste de positions à ne contenir que les déplacements
                             résultants de la prise d'une pièce adverse.
        :return: Une liste de positions où les pièces de couleur "couleur" peuvent de se déplacer.
        """
        possibilite = list()
        
        for keys in self.cases.keys(): # on regarde toute les piece présente.
            piece = self.cases[keys]
            if (piece.couleur == couleur): # si la couleur demandé est celle de la piece courrante, on continue
                if (self.lister_deplacements_possibles_a_partir_de_position(keys,doit_prendre)):
                    possibilite.extend(self.lister_deplacements_possibles_a_partir_de_position(keys,doit_prendre)) #on ajoute aux possibilité cette possibilite si c'est possible
        
        if (possibilite):
            return possibilite
        else:
            return None

    def deplacer(self, position_source, position_cible):
        """
        Effectue un déplacement sur le damier. Si le déplacement est valide, on doit mettre à jour le dictionnaire
        self.cases, en déplaçant la pièce à sa nouvelle position.

        Cette méthode doit également:
        - Promouvoir un pion en dame si celui-ci atteint l'autre extrémité du plateau.
        - Supprimer une pièce adverse qui a été prise lors du déplacement, si c'est le cas.
        - Retourner un message indiquant "ok", "prise" ou "erreur".

        ATTENTION: Si le déplacement est effectué, cette méthode doit retourner "ok" si aucune prise n'a été faite,
                   et "prise" si une pièce a été prise.
        ATTENTION: Ne dupliquez pas de code! Vous avez déjà programmer (ou allez programmer) une méthode permettant
                   de trouver la liste des déplacements valides...

        :param position_source: La position source du déplacement.
        :type position_source: Tuple (ligne, colonne).
        :param position_cible: La position cible du déplacement.
        :type position_cible: Tuple (ligne, colonne).
        :return: "ok" si le déplacement a été effectué sans prise, "prise" si une pièce adverse a été prise, et
                 "erreur" autrement.
        """
        piece = self.get_piece(position_source)
        prise = False
        deplacement = False
        if(piece):
            if(position_cible in self.lister_deplacements_possibles_a_partir_de_position(position_source)):
                self.cases[(position_cible)]= self.cases[(position_source)]
                #on met a la position cible la position source
                del self.cases[(position_source)] 
                deplacement = True
                if(abs(position_cible[0]-position_source[0])>1 and abs(position_cible[1]-position_source[1])>1): # verification si la pièces à bougé de plus d'une case si oui elle a mangé
                    prise = True
                    #recherche du point entre les 2, (la pièces qui a été mangé)
                    lig=(position_source[0]+position_cible[0])/2
                    col=(position_source[1]+position_cible[1])/2
                    del self.cases[(lig,col)]# enleve la pièce qui était dedans par un espace vide
                
        if(prise and deplacement):
            return "prise"
        elif(deplacement):
            return "ok"
        else:
            return "erreur"
            
        
        
        
    def convertir_en_chaine(self):
        """
        Retourne une chaîne de caractères où chaque case est écrite sur une ligne distincte.
        Chaque ligne contient l'information suivante :
        ligne,colonne,couleur,type
        
        Cette méthode pourrait par la suite être réutilisée pour sauvegarder un damier dans un fichier.

        :return: La chaîne de caractères.
        """
        chaine = ""
        
        for i in range(0, 8):
            for j in range(0, 8):
                typeDePiece = ""
                couleur = ""
                piece = self.get_piece((i,j))
                if(piece):
                    couleur = piece.couleur
                    if(piece.est_pion()):
                        typeDePiece = "pion"
                    else:
                        typeDePiece = "dame"
                case = (str(i),str(j),couleur,typeDePiece)
                for string in case:
                    if (string):
                        chaine += string+","
                chaine = chaine[:-1] + "\n"
        return chaine
                    
    
    def charger_dune_chaine(self, chaine):
        """
        Remplit le damier à partir d'une chaîne de caractères comportant l'information d'une pièce sur chaque ligne.
        Chaque ligne contient l'information suivante :
        ligne,colonne,couleur,type

        :param chaine: La chaîne de caractères.
        :type chaine: string
        """
        self.cases.clear() # on vide le damier
        cases = (chaine.split('\n')) #on sépare les ligne dans une list
        for case in cases: # on itere sur chacune des case
            thisCase = case.split(',') # on creer une liste à partir d'une case
            if(len(thisCase)==4): # si la case comporte un pion ou une dame elle comportera 4 éléments
                position = (int(thisCase[0]),int(thisCase[1]))
                couleur = thisCase[2]
                typeDePiece = thisCase[3]
                self.cases[position] = Piece(couleur,typeDePiece)    # on instencie les pièce à leur position
                    
        
    def initialiser_damier_par_default(self):
        """
        Initialise un damier de base avec la position initiale des pièces.
        """
        self.cases.clear()
        self.cases[(7, 0)] = Piece("blanc", "pion")
        self.cases[(7, 2)] = Piece("blanc", "pion")
        self.cases[(7, 4)] = Piece("blanc", "pion")
        self.cases[(7, 6)] = Piece("blanc", "pion")
        self.cases[(6, 1)] = Piece("blanc", "pion")
        self.cases[(6, 3)] = Piece("blanc", "pion")
        self.cases[(6, 5)] = Piece("blanc", "pion")
        self.cases[(6, 7)] = Piece("blanc", "pion")
        self.cases[(5, 0)] = Piece("blanc", "pion")
        self.cases[(5, 2)] = Piece("blanc", "pion")
        self.cases[(5, 4)] = Piece("blanc", "pion")
        self.cases[(5, 6)] = Piece("blanc", "pion")
        self.cases[(2, 1)] = Piece("noir", "pion")
        self.cases[(2, 3)] = Piece("noir", "pion")
        self.cases[(2, 5)] = Piece("noir", "pion")
        self.cases[(2, 7)] = Piece("noir", "pion")
        self.cases[(1, 0)] = Piece("noir", "pion")
        self.cases[(1, 2)] = Piece("noir", "pion")
        self.cases[(1, 4)] = Piece("noir", "pion")
        self.cases[(1, 6)] = Piece("noir", "pion")
        self.cases[(0, 1)] = Piece("noir", "pion")
        self.cases[(0, 3)] = Piece("noir", "pion")
        self.cases[(0, 5)] = Piece("noir", "pion")
        self.cases[(0, 7)] = Piece("noir", "pion")

    def __repr__(self):
        """
        Cette méthode spéciale permet de modifier le comportement d'une instance de la classe Damier pour l'affichage.
        Faire un print(un_damier) affichera le damier à l'écran.
        """
        s = " +-0-+-1-+-2-+-3-+-4-+-5-+-6-+-7-+\n"
        for i in range(0, 8):
            s += str(i)+"| "
            for j in range(0, 8):
                if (i, j) in self.cases:
                    s += str(self.cases[(i, j)])+" | "
                else:
                    s += "  | "
            s += "\n +---+---+---+---+---+---+---+---+\n"

        return s


if __name__ == "__main__":
    # Ceci n'est pas le point d'entrée du programme principal, mais il vous permettra de faire de petits tests avec
    # vos fonctions du damier.
    
    damier = Damier()
    print(damier)
    #sauvegarde = damier.convertir_en_chaine()
    #position = (5,6)
    #print("la position: ",position, " est valide? : ", damier.position_valide(position))
    #thisPiece = damier.get_piece(position)
    #print("la pi�ce est : ", thisPiece)
    #print(damier.lister_deplacements_possibles_a_partir_de_position(position,True))
    #print(damier.lister_deplacements_possibles_de_couleur("blanc",False))
    #print(damier.deplacer((4,3), (2,5))) 
    #print(damier.deplacer((2,1),(3,2)))
    #input()
    #print(damier)
    #input()
    #damier.charger_dune_chaine(sauvegarde)
    #print(damier)
    #print(damier.convertir_en_chaine())
    
