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
        - Est-ce que la position contient une pièce?
        - Est-ce que cette pièce est de la bonne couleur?
        - Si le joueur doit absolument faire une prise, est-ce que la pièce choisie en la la possibilité?
        - Si le joueur doit absoluement continuer son mouvement avec une prise supplémentaire, a-t-il choisi la
          bonne pièce?

        ATTENTION: Utilisez self.couleur_joueur_courant, self.doit_prendre et self.position_source_forcee pour
                   connaître les informations nécessaires.
        ATTENTION: Bien que cette méthode valide plusieurs choses, les méthodes programmées dans le damier vous
                   simplifieront la tâche!

        :param position_source: La position source à valider.
        :return: Un couple où le premier élément représente la validité de la position (True ou False), et le
                 deuxième élément est un éventuel message d'erreur.
        """
        pass

    def valider_position_cible(self, position_source, position_cible):
        """
        Vérifie si oui ou non la position cible est valide, en fonction de la position source.
        ATTENTION: Vous avez déjà programmé la méthode nécessaire dans le damier!

        :return: Un couple où le premier élément représente la validité de la position (True ou False), et le
                 deuxième élément est un éventuel message d'erreur.
        """
        pass

    def demander_positions_deplacement(self):
        """
        Demande à l'utilisateur les positions sources et cible, et valide ces positions.
        ATTENTION: Validez les positions avec les méthodes appropriées!

        :return: Un couple de deux positions (source et cible). Chaque position est un couple (ligne, colonne).
        """
        pass

    def tour(self):
        """
        Cette méthode simule le tour d'un joueur, et doit effectuer les actions suivantes:
        - Assigne self.doit_prendre à True si le joueur courant a la possibilité de prendre une pièce adverse.
          (utilisez une méthode que vous avez déjà programmée dans le damier!)
        - Demander les positions source et cible (utilisez self.demander_positions_deplacement!)
        - Effectuer le déplacement (à l'aide de la méthode du damier appropriée)
        - Si une pièce a été prise lors du déplacement, c'est encore au tour du même joueur si celui-ci peut encore
          prendre une pièce adverse en continuant son mouvement. Utilisez les membres self.doit_prendre et
          self.position_source_forcee pour forcer ce prochain tour!
        - Si aucune pièce n'a été prise ou qu'aucun coup supplémentaire peut être fait avec la même pièce, c'est le
          tour du joueur adverse. Mettez à jour les membres de la classe en conséquence.
        """
        pass

    def jouer(self):
        """
        Démarre une partie. Tant que le joueur courant a des déplacements possibles (utilisez la méthode appriopriée!),
        un nouveau tour est joué.

        :return: La couleur ("noir", "blanc") du joueur gagnant.
        """
        pass

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
    partie = Partie()

    # Si on veut sauvegarder une partie.
    #partie.sauvegarder("ma_partie.txt")

    # Si on veut charger un fichier.
    #partie.charger("exemple_partie.txt")

    gagnant = partie.jouer()

    print("------------------------------------------------------")
    print("Partie terminée! Le joueur gagnant est le joueur", gagnant)
