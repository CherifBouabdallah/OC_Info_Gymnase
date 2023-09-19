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






days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]


days.append("Monday")
days.insert(0, "Sunday")
del days[1]
del days[6]

for i in range(len(days)):
    print(days[i])




alphabet= ["a", "b", "c", "d", "e", "f", "g", "h", "i ", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s ", "t", "u", "v", "w", "x", "y", "z"]

del alphabet[13]
del alphabet[10]

alphabet.remove("d")
alphabet.remove("b")
alphabet.remove("t")
alphabet.remove("z")


print(alphabet)





liste = [3,4,3,3,5,6,7,1,2,6,7,8,3,2,1]
lst = []

for i in liste:
    if i not in lst:
        lst.append(i)

print(lst)

liste = lst
print(liste)




notes = [ 5, 3, 6, 2.5, 4.5, 5, 3]

moyenne = 0
somme = 0

notes.sort()
del notes[0]

for i in notes:
    somme += i
    moyenne = somme/len(notes)

print(moyenne)






for n in range(-1, len(lst), 2):
    print(lst[n-1:n+1])



a=7
b=9

while b <= len(lst) or a >= 0:
    print(lst[a:b])
    a -= 1
    b += 1





lst = [3,4,3,3,5,6,7,1,2,6,7,8,3,2,1]

n = int(input('what is a number for ya : '))

if len(lst) < n:
    print('no')
    exit()

while len(lst) % n != 0:
    lst.append(0)


for div in n:
    print()




lst = ["Pierre", "Paul", "Jacques"]

for i in lst:
    if i[-1] == "e":
        print(i)
        
        
'''

liste1 =[1 ,2 ,3 ,4 ,5 ,6] 
liste2=liste1
liste2.append(7)
print(liste1)


liste1 =[1 ,2 ,3 ,4 ,5 ,6] 
liste2=liste1.copy() 
liste2.append(7) 
print(liste1)