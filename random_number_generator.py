import random
range = 100
x = random.randrange(range)

guess = int(input('Devine un nbr entre 1 et'+str(range)+":" ))


while guess != x:
    if x < guess:
        print("too big")
    else:
        print ("too small")
    guess = int(input('Devine un nbr entre 1 et'+str(range)+":" ))
print ("félicitations")
