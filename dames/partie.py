__author__ = "Jean-Francis Roy"
from damier import Damier


class Partie:
    def __init__(self):
        """
        Méthode d'initialisation d'une partie. On initialise 4 membres:
        - damier: contient le damier de la partie, celui-ci contenant le dictionnaire de pièces.
        - couleur_joueur_courant: le joueur à qui c'est le tour de jouer.
        - doit_prendre: un booléen représentant si le joueur actif doit absoluement effectuer une prise de pièce.
        - position_source_forcee: Une position avec laquelle le joueur actif doit absoluement jouer. Le seul moment
          où cette position est utilisée est après une prise: si le joueur peut encore prendre d'autres pièces adverses,
          il doit absolument le faire. Ce membre contient None si aucune position n'est forcée.
        """
        self.damier = Damier()
        self.couleur_joueur_courant = "blanc"
        self.doit_prendre = False
        self.position_source_forcee = None

    def valider_position_source(self, position_source):
        """
        Vérifie la validité de la position source, notamment:
        - Est-ce que la position contient une pièce? ok
        - Est-ce que cette pièce est de la bonne couleur? ok
        - Si le joueur doit absolument faire une prise, est-ce que la pièce choisie en la la possibilité?
        - Si le joueur doit absoluement continuer son mouvement avec une prise supplémentaire, a-t-il choisi la
          bonne pièce? ok

        ATTENTION: Utilisez self.couleur_joueur_courant, self.doit_prendre et self.position_source_forcee pour
                   connaître les informations nécessaires.
        ATTENTION: Bien que cette méthode valide plusieurs choses, les méthodes programmées dans le damier vous
                   simplifieront la tâche!

        :param position_source: La position source à valider.
        :return: Un couple où le premier élément représente la validité de la position (True ou False), et le
                 deuxième élément est un éventuel message d'erreur.
        """
        """# vérifie que la saisie est dans les bornes du damier:"""
        good_source=False
        msg=""
        if not self.damier.position_valide(position_source):
            msg="saisie de la source en dehors du Damier" # vérifie que la saisie est dans les bornes du damier
            good_source=False
            
        #""contient une piece à la source de la bonne couleur? :"""
        elif self.damier.get_piece(position_source)==None or self.damier.cases[position_source].couleur!=self.couleur_joueur_courant:
            msg="Pas de piece à cette place de votre couleur"
            good_source=False
        #Est-il possible de faire un déplacement avec la piece choisie ?:
        elif self.damier.lister_deplacements_possibles_a_partir_de_position(position_source, False)==None:
            msg="Vous devez fournir une position source qui permet de faire un déplacement"
        #La piece choisi permet -elle de faire une prise qui est obligatoire?:
        elif self.doit_prendre and self.damier.lister_deplacements_possibles_a_partir_de_position(position_source,True)==None:
            msg="Vous devez prendre une piece adverse"
            #print("liste doit prendre ",self.damier.lister_deplacements_possibles_de_couleur(self.couleur_joueur_courant, True))
        #La piece choisi est-elle celle avec une prise supplémentaire?:
        #elif self.doit_prendre and self.position_source_forcee!=position_source:
           # msg="Vous devez continuer avec la même piece car il ya des prises supplémentaires"
        else: good_source=True
            
       
        return (good_source, msg) 
        
        

    def valider_position_cible(self, position_source, position_cible):
        """
        Vérifie si oui ou non la position cible est valide, en fonction de la position source.ok
        ATTENTION: Vous avez déjà programmé la méthode nécessaire dans le damier!

        :return: Un couple où le premier élément représente la validité de la position (True ou False), et le
                 deuxième élément est un éventuel message d'erreur.
        """
        good_cible=False
        msg=""
        if not self.damier.position_valide(position_cible):
            msg="saisie de la cible en dehors du Damier" # vérifie que la saisie est dans les bornes du damier
            good_cible=False
        elif position_cible in self.damier.lister_deplacements_possibles_a_partir_de_position(position_source,False):
            #print("liste dans valider position cible ",self.damier.lister_deplacements_possibles_a_partir_de_position(position_source,False))
            good_cible=True
        else:
            msg="Position cible impossible"
        return (good_cible, msg)

    def demander_positions_deplacement(self):
        """
        Demande à l'utilisateur les positions sources et cible, et valide ces positions.
        ATTENTION: Validez les positions avec les méthodes appropriées!

        :return: Un couple de deux positions (source et cible). Chaque position est un couple (ligne, colonne).
        """
        saisie=False
        good_source=["",""]
        """boucle sur la validation de la saisie position source"""
        while saisie==False:       
            userInputSource=input("Joueur " + self.couleur_joueur_courant +  " entrez les positions sources une coordonnée ligne,colonne entre 0 et 7: ")
            print(userInputSource)
        
            """Validation de la saisie de la source """
            try:
                int(userInputSource.split(',')[0])
                int(userInputSource.split(',')[1])
            except:
                good_source[1]="Vous devez suivre le modéle : ligne, colonne"
                saisie=False
            else:
                posSource=(int(userInputSource.split(',')[0]),int(userInputSource.split(',')[1])) # génére le tuple de coordonnées
                good_source[0]=self.valider_position_source(posSource)[0]
                good_source[1]=self.valider_position_source(posSource)[1]
                           
            if good_source[1]!="":
                print("Saisie Incorrecte : ",good_source[1])
            else:
                saisie=True


        saisie=False
        good_cible=["",""]
        """boucle sur la validation de la saisie position cible"""
        while saisie==False:
            userInputCible=input("Joueur " + self.couleur_joueur_courant +  " entrez les positions cibles une coordonnée ligne,colonne entre 0 et 7: ")
            
            """Validation de la cible"""        
        
            try:
                int(userInputCible.split(',')[0])
                int(userInputCible.split(',')[1])
            except:
                good_cible[1]="Vous devez suivre le modéle : ligne, colonne"
                saisie=False
            else:
                posCible=(int(userInputCible.split(',')[0]),int(userInputCible.split(',')[1])) # génére le tuple de coordonnées
                good_cible[0]=self.valider_position_cible(posSource,posCible)[0]
                good_cible[1]=self.valider_position_cible(posSource,posCible)[1]
            
            if good_cible[1]!="":
                print("Saisie Incorrecte : ",good_cible[1])
            else:
                saisie=True
        
        return posSource, posCible
        
        
        

    def tour(self):
        """
        Cette méthode simule le tour d'un joueur, et doit effectuer les actions suivantes:
        - Assigne self.doit_prendre à True si le joueur courant a la possibilité de prendre une pièce adverse. ok
          (utilisez une méthode que vous avez déjà programmée dans le damier!)
        - Demander les positions source et cible (utilisez self.demander_positions_deplacement!) ok
        - Effectuer le déplacement (à l'aide de la méthode du damier appropriée)ok
        - Si une pièce a été prise lors du déplacement, c'est encore au tour du même joueur si celui-ci peut encore
          prendre une pièce adverse en continuant son mouvement. Utilisez les membres self.doit_prendre et
          self.position_source_forcee pour forcer ce prochain tour!
        - Si aucune pièce n'a été prise ou qu'aucun coup supplémentaire peut être fait avec la même pièce, c'est le
          tour du joueur adverse. Mettez à jour les membres de la classe en conséquence.
        """
        
        """Assigne self.doit_prendre à True si le joueur courant a la possibilité de prendre une pièce adverse
        """
        if self.damier.lister_deplacements_possibles_de_couleur(self.couleur_joueur_courant, True)!=None:
            print("le joueur doit prendre") # Vérifie si le joueur doit prendre
            self.doit_prendre=True
            
                    
        """Demander les positions source et cible (utilisez self.demander_positions_deplacement!)
        """
        position=self.demander_positions_deplacement()
        
        """Fait le déplacement de la piece :
        """
        """return: "ok" si le déplacement a été effectué sans prise, "prise" si une pièce adverse a été prise, et
                 "erreur" autrement."""
        status=self.damier.deplacer(position[0], position[1])
        print("Status deplacement ",status)
        print(self.damier)
        
        """Si une pièce a été prise lors du déplacement, c'est encore au tour du même joueur si celui-ci peut encore
          prendre une pièce adverse en continuant son mouvement. Utilisez les membres self.doit_prendre et
          self.position_source_forcee pour forcer ce prochain tour!
        """
        if status=="ok":
            if self.couleur_joueur_courant=="blanc":
                self.couleur_joueur_courant="noir"
            else:
                self.couleur_joueur_courant="blanc"
        if status=="prise" and self.damier.lister_deplacements_possibles_a_partir_de_position(position[1],True)!=None:
            self.position_source_forcee=position[1]
        elif status=="prise":
            self.doit_prendre=False
            if self.couleur_joueur_courant=="blanc":
                self.couleur_joueur_courant="noir"
            else:
                self.couleur_joueur_courant="blanc"
        
    """    
        if status=="prise" :
            self.position_source_forcee=position
        else:
            if self.couleur_joueur_courant=="blanc":
                self.couleur_joueur_courant="noir"
            elif self.couleur_joueur_courant=="noir":
                self.couleur_joueur_courant="blanc"
    """ 
        
        

    def jouer(self):
        """
        Démarre une partie. Tant que le joueur courant a des déplacements possibles (utilisez la méthode appriopriée!),
        un nouveau tour est joué.

        :return: La couleur ("noir", "blanc") du joueur gagnant.
        """
        
        while self.damier.lister_deplacements_possibles_de_couleur(self.couleur_joueur_courant, False)!=None:
            self.tour()
        if self.couleur_joueur_courant=="blanc":
            couleur="noir"
        else:
            couleur="blanc"
        return couleur

    def sauvegarder(self, nom_fichier):
        """
        Sauvegarde une partie dans un fichier. Le fichier condiendra:
        - Une ligne indiquant la couleur du joueur courant.
        - Une ligne contenant True ou False, si le joueur courant doit absolument effectuer une prise à son tour.
        - Une ligne contenant None si self.position_source_forcee est à None, et la position ligne,colonne autrement.
        - Le reste des lignes correspondent au damier. Voir la méthode convertir_en_chaine du damier pour le format.

        :param nom_fichier: Le nom du fichier où sauvegarder.
        :type nom_fichier: string.
        """
        pass

    def charger(self, nom_fichier):
        """
        Charge une partie dans à partir d'un fichier. Le fichier a le même format que la méthode de sauvegarde.

        :param nom_fichier: Le nom du fichier à charger.
        :type nom_fichier: string.
        """
        pass


if __name__ == "__main__":
    # Point d'entrée du programme. On initialise une nouvelle partie, et on appelle la méthode jouer().
    print(Damier())
    partie = Partie()

    # Si on veut sauvegarder une partie.
    #partie.sauvegarder("ma_partie.txt")

    # Si on veut charger un fichier.
    #partie.charger("exemple_partie.txt")

    gagnant = partie.jouer()
    
    print("------------------------------------------------------")
    print("Partie terminée! Le joueur gagnant est le joueur", gagnant)
