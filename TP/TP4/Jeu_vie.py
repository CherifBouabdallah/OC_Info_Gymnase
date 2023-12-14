# JEU DE LA VIE
from tkinter import Tk, Canvas
import random
TAILLE = 600

# Création de la grille
Grille = [ ] 
for i in range(60):
    Grille.append([0]*60)

# Remplissage Aléatoire de la grille
for i in range(500):
    x = random.randint(0,59)
    y = random.randint(0,59)
    Grille[x][y] = 1

# Affichage des carrés dans la grille
def Affiche():
    canvas.delete("all")
    for x in range(60) :
       for y in range(60) :
           if Grille[x][y] == 1:
             xx = x * 10
             yy = y * 10
             c="red"
             canvas.create_rectangle(xx,yy,xx+10,yy+10,fill=c)
             
# Compte le nombre de voisins dans la grille
def CompteVoisins(x,y) :
    count = 0
    V = [(x-1,y-1), (x,y-1),(x+1,y-1),(x-1,y),(x+1,y),(x-1,y+1), (x,y+1),(x+1,y+1)]
    # La liste V, est la liste possible des voisins en partant de x,y. 
    for dx,dy in V:
        count += Grille[(dx)%60][(dy)%60]
    return count

# Evolution de la grille en fonction des voisins
def Evolution():
    global Grille
    Grille2 = [ ] # init nouvelle grille vide
    for i in range(60):
        Grille2.append([0]*60)

    for x in range(60) :
       for y in range(60) :
            nbVoisins = CompteVoisins(x,y)

            if Grille[x][y] == 0 and nbVoisins == 3 :
                    Grille2[x][y] = 1

            if Grille[x][y] == 1 and nbVoisins in [2,3] :
                    Grille2[x][y] = 1
    Grille = Grille2

# Programme principal
def PROG() :
    Affiche()
    Evolution()
    Mafenetre.after(100,PROG)


# Création de la fenêtre de dessin
Mafenetre = Tk()
Mafenetre.geometry(str(TAILLE) +"x"+str(TAILLE))
canvas = Canvas(Mafenetre,width=TAILLE, height=TAILLE, borderwidth=0, highlightthickness=0,bg="lightgray")
canvas.pack()
Mafenetre.after(100,PROG)
Mafenetre.mainloop()
