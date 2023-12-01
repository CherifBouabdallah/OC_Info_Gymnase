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
        
        


liste1 =[1 ,2 ,3 ,4 ,5 ,6] 
liste2=liste1
liste2.append(7)
print(liste1)


liste1 =[1 ,2 ,3 ,4 ,5 ,6] 
liste2=liste1.copy() 
liste2.append(7) 
print(liste1)



n = 0
lst=[3,4,3,2,5,6,3,5,4,6,7,2,4,1,2,1,2,1,1,1]
lst.sort()

for i in lst:
    if n != i:
        print(lst.count(i))
        n = i
    


list = [17, 38, 10, 25, 72]

list.sort()
list.append(12)
list.reverse()
print(list)



print("Hello","me", sep="+") 
print("Hello","me", sep="\n") 
print("Chemin du fichier:","Home", "usr","Bureau", sep="/")

print("Hello","me", end="!")



print(f'{123.45679:.2f}')
print(f'{123.45679:.4e}')




print(f'{10: 6d}') 
print(f'{100: 6d}') 
print(f'{10: 10d}') 
print(f'{10: >6d}') 
print(f'{10: <6d}') 
print(f'{10: ^6d}')



def func(mot, n=3): 
    return mot[:n]

print(func('no'))


a=10
def variable(n):
    a=3
    b= a+ 4
    print(f"Dans la fonction a={a} et b={b}")
    print("a=",a) 
    print("b=",b)

variable(5)




def func(end, start = 0,  step = 2):
    added = 0
    for i in range(start, end+1, step):
        added += i

    return added

lst = []
def prem(end, start = 2):
    for i in range(start, end+1):
        j = 2
        while i % j != 0 and j<i:
            j = j + 1
        if j == i:
            lst.append(i)
    return lst


print(prem(300))




lst = [4 ,567, 5, 8, 4]

def multi(list):
    for i in range(len(list)):
        list[i] *= 2
    print (list)

def invert(list):
    temp_lst = []

    for i in range((len(list)-1)):
        temp_lst.append(list[-(i+1)])
        
    temp_lst.append(list[0])
    print(list)
    print(temp_lst)

invert(lst)




notes = {'maths' : 6, 'fr' : 4 , 'histoire' : 5}

notes['Bio'] = 3

print(notes['fr'])
n = 0
for i in notes:
    n += notes[i]

moy = n/len(notes)

print(moy)
print(n)





telephones = { "Julien":"0712345678", "Julie":" 0787654321", "Juliette":"070707070707" }

prenoms = list(telephones.keys()) 
numeros = list(telephones.values()) 
print(prenoms)
print(numeros)

print("Juliette" in telephones) 
print("Marie" in telephones)

del telephones["Julien"]

print(telephones)



notes = {'maths' : 6, 'fr' : 4 , 'histoire' : 5, 'Bio' : 4}


for key in notes: 
    notes[key] += 1

    print(key, notes[key])


for key,val in notes.items():
    print(key, val-1)


    




word = str(input('GIBE ME A WORD MAN BEAUTUFUL : '))


def function(word):
    dic = {}


    for i in word:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1

    for i in dic:
        print('il y a', dic[i], i, 'dans le mot')



function(word)

'''

grille =[]
ligne =[]

for i in range(5):
    ligne.append(0) 

for i in range(5):
    grille.append(ligne.copy())

grille[2][3]=5
print(grille[2][3]) 
print(grille[4][3])


print("chaques lignes")
for i in range(len(grille)): 
    print(grille[i])


for x in range(len(grille)):
    for y in range(len(grille[x])):
        print(grille[x][y]) 