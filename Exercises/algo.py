
l = [7,3,2,11,1, 6, 30, -5, 12, -7, 1]


#for i in range(len(l)-1):
#    temp1 = l[i]
#    temp2 = l[i+1]
#    if l[i] > l[i+1]:
#        l[i] = temp2
#        l[i+1] = temp1
def mini_bulle(l):
    for a in range((len(l)-1)):
        for i in range(len(l)-(a+1)):
            temp1 = l[i]
            temp2 = l[i+1]
            if l[i] > l[i+1]:
                l[i] = temp2
                l[i+1] = temp1  
    return l

def mini_select(l):
    min = l[a]
    for i in range(len(l)):
        if i < min:
            min = l[i]

# Tri par insertion

def mini_insert(l):
    for n in range(1,len(l)): # n index du premier élément non trié
        i=n-1 # index du dernier élément trié 
        print(n,i, l)
        val=l[n] # j'enregistre la valeur dans val

    if n > val:
        l[n] 

    ''' Compléter ce programme pour qu'il:
        1. décale les éléments triés plus grand que val d'une position.
        2. enregistre val juste après le premier élément plus petit ou égale à val '''



print(l)