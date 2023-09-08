import time 
import math

'''

r = 5
pi = 3.14159
aire= 2 * pi * r

bool(aire)
print(aire)
print(type(aire))



mon_age =100 # mon_age est 
ma_taille = 1.95 # est un 
mon_nom = "Dromard" # est
vrai= True # vrai est un booléen

print(type(mon_age)) # La sortie va être <class int> 
print(type(ma_taille + 10)) # La sortie va être <class float> 
print(type(mon_nom)) # La sortie va être <class str> 
print(type(vrai)) # La sortie va être <class bool>




number = (input('Donne un nombre à 4 chiffres '))
number_bb = (input('Donne un nombre à 4 chiffres '))


print(int(number) - 1)
print(int(number) + 1)

print(str(number)[0])
print(str(number)[1])
print(str(number)[2])
print(str(number)[3])

print(number_bb // number)
print(number_bb // number)




word = str(input("give me a word "))

L=["a", "e", "i", "o", "u", "y"] 
n = 0
n_v = 0

for n in word:
    if n in L:
        n_v += 1

print(n_v)




word = str(input("give me a word : "))
drow = 0

for i in range(len(word), 0, -1):
    drow = word[i-1]
    print(drow ,end="")
print()

'''




days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]


days.append("Monday")
days.insert(0, "Sunday")
del days[1]
del days[6]

for i in range(len(days)):
    print(days[i])