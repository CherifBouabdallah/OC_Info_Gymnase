mot = 'Hello'

fichier = open('/Users/pi73xdo/Desktop/Cherif_Info/TP/Hooverphonic.txt', "r")
text_file = fichier.read()

def Crypt(mot):
    space = ""
    for i in mot:
        space += str(ord(i)) + " "
    return space

crypted = (Crypt(mot))
print(crypted)

def Decry(crypted):
    
    n = 0
    final = ""

    while n < len(crypted):
        temp_numbers = ""
        
        while n < len(crypted) and crypted[n] != " ":
            temp_numbers += crypted[n]
            n += 1
        
        decry = chr(int(temp_numbers))
        final += decry
        n += 1

    return final    
    
    
print(Decry(crypted))

