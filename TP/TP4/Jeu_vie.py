from tkinter import Tk, Canvas
import random
TAILLE = 600

grille = []
numbers = [0, 0, 0]
color1 = 'gold'
color2 = 'grey25'
time = 1

for i in range(60):
    grille.append([0]*60)

for i in range(500):
    x = random.randint(0,59)
    y = random.randint(0,59)
    grille[x][y] = 1

for i in range(500):
    x = random.randint(0,59)
    y = random.randint(0,59)
    if grille[x][y] != 1:
        grille[x][y] = 2

def Affiche():
    canvas.delete("all")
    numbers[2] = 0
    for x in range(60) :
       for y in range(60) :
           if grille[x][y] == 2:
             xx2 = x * 10
             yy2 = y * 10
             c= color2
             canvas.create_rectangle(xx2,yy2,xx2+10,yy2+10,fill=c)
             numbers[2] += 1

    numbers[1] = 0
    for x in range(60) :
       for y in range(60) :
           if grille[x][y] == 1:
             xx = x * 10
             yy = y * 10
             c2= color1
             canvas.create_rectangle(xx,yy,xx+10,yy+10,fill=c2)
             numbers[1] += 1

def CompteVoisins(x,y) :
    count = 0
    V = [(x-1,y-1), (x,y-1),(x+1,y-1),(x-1,y),(x+1,y),(x-1,y+1), (x,y+1),(x+1,y+1)]
    for dx,dy in V:
        if grille[(dx)%60][(dy)%60] == 1:
            count += 1
    return count

def CompteVoisins2(x,y) :
    count = 0
    V = [(x-1,y-1), (x,y-1),(x+1,y-1),(x-1,y),(x+1,y),(x-1,y+1), (x,y+1),(x+1,y+1)]
    for dx,dy in V:
        if grille[(dx)%60][(dy)%60] == 2:
            count += 1
    return count


def Evolution():
    global grille
    grille2 = [ ]
    
    for i in range(60):
        grille2.append([0]*60)

    did = random.randint(1, 1000)
    for x in range(60) :
       for y in range(60) :
            nbVoisins = CompteVoisins(x,y)
            nbVoisins2 = CompteVoisins2(x,y)

            if grille[x][y] == 0 and nbVoisins == 3 :
                    grille2[x][y] = 1

            if grille[x][y] == 1 and nbVoisins in [2,3] :
                    grille2[x][y] = 1

            if grille[x][y] == 0 and nbVoisins2 == 3 :
                    grille2[x][y] = 2

            if grille[x][y] == 2 and nbVoisins2 in [2,3] :
                    grille2[x][y] = 2
            
            did = random.randint(1, 500)
            if did >= 1000-1:
                print('active')
                sa = random.randint(1,2)
                if sa == 1:
                    for i in range(random.randint(1, 500)):
                        grille2[random.randint(0,59)][random.randint(0,59)] = 1
                else:
                    for i in range(random.randint(1, 500)):
                        grille2[random.randint(0,59)][random.randint(0,59)] = 2

    grille = grille2


def Data(nbr, name, x, y):
    canvas.create_text(x,y,font=("Purisa", 20 , "bold"), text=name+str(nbr))


def PROG() :
    Affiche()
    Evolution()
    window.after(time,PROG)
    numbers[0] += 1
    Data(numbers[0], 'Gen : ', 100, 25)
    Data(numbers[1], 'Number1 : ', 100, 50)
    Data(numbers[2], 'Number2 : ', 100, 75)



window = Tk()
window.geometry(str(TAILLE) +"x"+str(TAILLE))
canvas = Canvas(window,width=TAILLE, height=TAILLE, borderwidth=0, highlightthickness=0,bg="white")
canvas.pack()
window.after(time,PROG)
window.mainloop()
