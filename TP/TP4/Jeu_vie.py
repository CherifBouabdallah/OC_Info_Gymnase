# JEU DE LA VIE
from tkinter import Tk, Canvas 
import random 
TAILLE = 600

grille = []
ligne = []


for i in range(60):
    ligne.append(0)
for i in range(60):
    grille.append(ligne.copy())

for i in range(50000
               ):
    grille[random.randint(0, 59)][random.randint(0, 59)] = 1
 
#for i in range(len(grille)): 
#    print(grille[i])

def Affiche(grille):
        canvas.delete("all")
        for x in range(len(grille)):
            for y in range(len(grille[x])):
                if grille[x][y] == 1:
                    canvas.create_rectangle(x*10,y*10,x*10+10,y*10+10,fill="red")

def Voisin(x, y):
    end = False
    nbr_v = 0
    for i in range(3):
        for j in range(3):
            if grille[((x-1)+i)%60][((y-1)+j)%60] == 1:
                nbr_v += 1
            if nbr_v == 1:
                nbr_v = 0
    return nbr_v

def Evolution(grille):
    g = []
    l = []
    for i in range(60):
        l.append(0)
    for i in range(60):
        g.append(ligne.copy())

    for x in range(len(grille)):
        for y in range(len(grille[x])):
            if Voisin(x, y) >= 1:
                g[x][y] = Voisin(x, y)
    grille = g
    Affiche(grille)



def PROG() :
    Affiche()
    Evolution(grille)
    window.after(100,PROG)


# Création de la fenêtre de dessin
window = Tk()
window.geometry(str(TAILLE) +"x"+str(TAILLE))
canvas = Canvas(window,width=TAILLE, height=TAILLE, borderwidth=0,
    highlightthickness=0,bg="white") 
canvas.pack()
window.after(100,PROG) 
window.mainloop()


