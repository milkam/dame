__author__ = "Jean-Francis Roy"
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
                if not(damier.get_piece(position)): # verification si la case est vide
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
        #on crée les 4 possibilité et on vérifie leur possibilite 
        possibiliteNonVerifie = ((position[0]+1,position[1]+1),(position[0]+1,position[1]-1),(position[0]-1,position[1]+1),(position[0]-1,position[1]-1))
        print (position,possibiliteNonVerifie)
        possibilite = list()
        
        for i,j in possibiliteNonVerifie:
            if (damier.position_valide((i,j)) and doit_prendre == False):
                possibilite.append((i,j))
            elif (damier.get_piece((i,j))):
                nouvellepossibiliteNonVerifie = ((i+1,j+1),(i+1,j-1),(i-1,j+1),(i-1,j-1))
                for x,y in nouvellepossibiliteNonVerifie:
                    if(damier.position_valide((x,y))):
                        possibilite.append((x,y))
                        
                
                
        print (possibilite)
        
        """
        problème présent : 
            si on sait pas la couleur de la pièces, comment on sait si on avance ou pas. Donc à quoi ca sert de savoir si c'est un pion ou une dame?
            Comment on fait pour savoir la couleur d'une pièces, autre qu'en regardant le code unicode.
         """   
            
        
        
             
        

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
        
        #couleur = ""
        #typePion = ""
        #verification si c'est un pion ou une dame et sa couleur (Je sais pas si c'est mon système, mais je peux pas verifier la pièce directement
        #if (str(self.cases[(position)]).encode(encoding='utf_8') == str(Piece("blanc", "pion")).encode(encoding='utf_8')):
        #    couleur,typePion = "blanc","pion"
        #elif (str(self.cases[(position)]).encode(encoding='utf_8') == str(Piece("blanc", "dame")).encode(encoding='utf_8')):
        #    couleur,typePion = "blanc","dame"
        #elif (str(self.cases[(position)]).encode(encoding='utf_8') == str(Piece("noir", "pion")).encode(encoding='utf_8')):
        #    couleur,typePion = "noir","pion"
        #else: 
        #    couleur,typePion = "noir","dame"
        #print(couleur,typePion) # Verification de la couleur et du type
        
        #pion noir ne peut que descendre
        #pion blanc ne peut que monter
        
        
        pass

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
        pass

    def convertir_en_chaine(self):
        """
        Retourne une chaîne de caractères où chaque case est écrite sur une ligne distincte.
        Chaque ligne contient l'information suivante :
        ligne,colonne,couleur,type

        Cette méthode pourrait par la suite être réutilisée pour sauvegarder un damier dans un fichier.

        :return: La chaîne de caractères.
        """
        pass

    def charger_dune_chaine(self, chaine):
        """
        Remplit le damier à partir d'une chaîne de caractères comportant l'information d'une pièce sur chaque ligne.
        Chaque ligne contient l'information suivante :
        ligne,colonne,couleur,type

        :param chaine: La chaîne de caractères.
        :type chaine: string
        """
        pass

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
    position = (5,4)
    print("la position est valide? : ", damier.position_valide(position))
    thisPiece = damier.get_piece(position)
    print("la pi�ce est : ", thisPiece)
    damier.lister_deplacements_possibles_a_partir_de_position(position)
            
    print(damier)
