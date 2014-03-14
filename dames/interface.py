#! /usr/bin/env python
# -*- coding:Utf-8 -*-
'''

Created on 2014-03-10

@author: Michel Tremblay #111092463
'''
from tkinter import *
from partie import *
from damier import *

__author__ = "Michel Tremblay NI 111092463"

class Interface:
    """
    Classe représentant l'interface Utilisateur
    """

    def __init__(self):
        """
        Initialisation de l'interface utilisateur
        """
        self.damier = Damier()
        self.startpositionlist = ()
        self.destinationpositionlist = ()
        self.affiche_interface_primaire()
        
    
                            

    def affiche_interface_primaire(self):
        fenetre = Tk()
        
        def movepiece():
            start,dest = startposition.get(),destinationposition.get()
            if(len(start)>2 and len(dest)>2): # si il y a des donnée on y va 
                self.startpositionlist = (int(start[0]),int(start[2]))
                self.destinationpositionlist = (int(dest[0]),int(dest[2]))
                self.damier.deplacer((self.startpositionlist), (self.destinationpositionlist))
                gamewindow.delete(1.0, END) # on reset le damier
                gamewindow.insert(END, self.damier) # on réinsert le damier
                startposition.set("") # on reset le start position
                destinationposition.set("") # on reset le destination
                
               
        
        fenetre.title("Jeux de Dame")
        fenetre.geometry("280x500+450+50")
        #creation du menu en haut qui gère le jeux
        topmenu = Menu(fenetre)
        gamemenu = Menu(topmenu,tearoff=0)
        gamemenu.add_command(label="Start Game",command=self.start)
        gamemenu.add_command(label="Save Game",command=self.save)
        gamemenu.add_command(label="Load Last Game",command=self.load)
        gamemenu.add_command(label="Quit",command=fenetre.quit)
        topmenu.add_cascade(label="Game",menu=gamemenu)
        
        helpmenu = Menu(topmenu,tearoff=0)
        helpmenu.add_command(label="About us",command=self.aboutus)
        topmenu.add_cascade(label="Help",menu=helpmenu)
        fenetre.config(menu=topmenu)

        #boite de prise de source et destination
        startposition=StringVar()
        destinationposition=StringVar()
        textstartpos=Label(fenetre, text="Position départ: lig col",width=40,height=3)
        textstartpos.pack()
        boxstartposition = Entry(textvariable=startposition,width=5)       
        boxstartposition.pack()
        textdestpos=Label(fenetre, text="Position destination: lig col",width=40,height=3)
        textdestpos.pack()
        boxdestinationposition = Entry(textvariable=destinationposition,width=5)
        boxdestinationposition.pack()

        #boutton pour faire bouger les pieces        
        move=Button(fenetre, text="Move", command=movepiece)
        move.pack()

        #insertion du damier
        gamewindow = Text(fenetre,width=200,height=200)
        gamewindow.insert(END, self.damier)
        gamewindow.pack()
        fenetre.mainloop()
        
         

    
    def save(self):
        print("save")
        return
    def load(self):
        print("load")
        return
    def start(self):
        print("start")
        return
    def aboutus(self):
        import tkinter.messagebox
        tkinter.messagebox.showinfo("About US","        Made by\n  Michel Tremblay\n              &    \nJean-Francois Paty")
        return
        

            
if __name__ == "__main__":
    interface = Interface()
    interface
