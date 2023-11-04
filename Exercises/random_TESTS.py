mot = "Abrasracourcix"
fin = 1
debut =0
pas = 1
print(mot[debut:fin])
while fin < len (mot) :
    début = fin
    pas +=1
    fin += k
    if fin < len (mot) :
        print ( mot [ debut : fin ])
    else :
        print (mot[début:len(mot)])