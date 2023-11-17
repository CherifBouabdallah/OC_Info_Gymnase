## Préparons la fenêtre 
import turtle
import random
import time

screen = turtle.Screen()
screen.setup(1000,1000) 
screen.title("TP3")
screen.bgcolor("white")
screen.tracer(0,0) 
turtle.hideturtle()
turtle.up()
turtle.color("red")
turtle.goto(350,400)
turtle.write("Score: ", align="center", font=("SF",25,"normal"))
done = False

turtle_list = []
letters = []
pos = []
score = [0]
L = ""
speed = 10

n_lettre = 8
alphab = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

for i in range(n_lettre):
    turtle_list.append(turtle.Turtle())

    random_letter = random.choice(alphab)

    while random_letter in letters:
        random_letter = random.choice(alphab)
    
    letters.append(random_letter)

    
    pos.append([random.randint(-450,450),500])

def afficher_lettre():
    for i in range(n_lettre):
        turtle_list[i].clear()
        turtle_list[i].hideturtle()
        turtle_list[i].up()
        turtle_list[i].color("purple")
        turtle_list[i].goto(pos[i])
        pos[i][1] -= speed
        turtle_list[i].write(letters[i],align="center",font=("SF",20,"bold"))
    
    screen.update()
    screen.ontimer(afficher_lettre, 50)

def f(L, score = score):
    i=letters.index(L)

    if i in letters:
        score[0] += 1
    else:
        score[0] += 1
    print (score[0])
    random_letter = random.choice(alphab)

    while random_letter in letters:
        random_letter = random.choice(alphab)

    letters[i] = random_letter
    pos[i] = [random.randint(-450,450),500]


def afficher_score(): 
    turtle.clear()
    turtle.goto(350,400)
    turtle.write("Score: {}".format(score[0]),align="center",font=("Courier",25,"normal")) 
    screen.update()


screen.onkey(lambda: f("a"), "a") 
screen.onkey(lambda: f("b"), "b") 
screen.onkey(lambda: f("c"), "c") 
screen.onkey(lambda: f("d"), "d") 
screen.onkey(lambda: f("e"), "e") 
screen.onkey(lambda: f("f"), "f") 
screen.onkey(lambda: f("g"), "g") 
screen.onkey(lambda: f("h"), "h") 
screen.onkey(lambda: f("i"), "i") 
screen.onkey(lambda: f("j"), "j") 
screen.onkey(lambda: f("k"), "k") 
screen.onkey(lambda: f("l"), "l") 
screen.onkey(lambda: f("m"), "m") 
screen.onkey(lambda: f("n"), "n") 
screen.onkey(lambda: f("o"), "o") 
screen.onkey(lambda: f("p"), "p") 
screen.onkey(lambda: f("q"), "q") 
screen.onkey(lambda: f("r"), "r") 
screen.onkey(lambda: f("s"), "s") 
screen.onkey(lambda: f("t"), "t") 
screen.onkey(lambda: f("u"), "u") 
screen.onkey(lambda: f("v"), "v") 
screen.onkey(lambda: f("w"), "w") 
screen.onkey(lambda: f("x"), "x") 
screen.onkey(lambda: f("y"), "y") 
screen.onkey(lambda: f("z"), "z")

while True:
    afficher_lettre()
    afficher_score()
    screen.listen()
    screen.mainloop()