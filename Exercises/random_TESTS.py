import math # me permet d’utiliser math.sqrt(x) qui me donne la racine carrée de x
n = int(input ( " donner un entier plus grand que 10 ")) 
while n <10:
    n = int(input(" donner un entier plus grand que 10 ")) 
for i in range (0 , n ):
    if int (math.sqrt(i)) == math.sqrt(i): 
        print ( i )