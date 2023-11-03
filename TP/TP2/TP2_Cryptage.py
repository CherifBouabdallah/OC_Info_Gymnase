mot = 'Hello World'

fichier = open('/Users/pi73xdo/Desktop/Cherif_Info/TP/TP2/Hooverphonic.txt', "r")
text_file = fichier.read()

fichier2 = open('/Users/pi73xdo/Desktop/Cherif_Info/TP/TP2/Madaboutyou.txt', "a")

mystere = open('/Users/pi73xdo/Desktop/Cherif_Info/TP/TP2/mystere1.txt', "r")
mystere_file = mystere.read()

def Crypt(mot):
    space = ""
    for i in mot:
        space += str(ord(i)) + " "
    return space

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
    

word_cry = Crypt(mot)
print(word_cry)
#print(Decry(mystere_file))


#encrypted = Crypt(text_file)
#print(encrypted, file=fichier3)
#fichier3.close()

def NewName(file_name):
    new_name = ""
    for i in range(len(file_name)):
        if file_name[i] != ".":
            new_name += file_name[i]
        else:
            new_name += "_encrypted."

    return new_name

def CryptAndRename(file_name):
    encrypted = Crypt(text_file)
    encrypted_file = open('/Users/pi73xdo/Desktop/Cherif_Info/TP/TP2/' + NewName(file_name), "w")
    print(encrypted, file=(encrypted_file))
    encrypted_file.close()


def CryptASCII(word, key):
    n=0
    final = ""
    space = ""
    for i in word:
        space += str(ord(i) + key) + " "

    while n < len(space):
            temp_numbers = ""

            while n < len(space) and space[n] != " ":
                temp_numbers += space[n]
                n += 1

            decry = chr(int(temp_numbers))
            final += decry
            n += 1

    return final

def DecryptASCII(word, key):
    n=0
    final = ""
    space = ""
    for i in word:
    


print(CryptASCII("Hello World", 8))
print(DecryptASCII("Pmttw%_evi%`{sv", 8))
