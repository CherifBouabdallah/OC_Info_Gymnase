'''
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


print(l)



u=1
for i in range(10):
    u=u+1 
    u=2*u






n = 50
prix = 120


l_valeur = [50, 20, 10, 5, 2, 1]
l_billets = [0, 0, 0, 0, 0, 0] 


while prix > 0:
    for i in range(len(l_valeur)):
        valeur = l_valeur[i]
        if prix >= valeur:
            l_billets[i] = prix // valeur
            prix -= l_billets[i] * valeur

print(l_billets)


'''


n = 6
d = 10000

d_reste = (1/2)**n

print(d*d_reste)
print(d-(d*d_reste))

