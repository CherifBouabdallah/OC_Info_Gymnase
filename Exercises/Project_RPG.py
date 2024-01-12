import time
import math

class Character:
    nbr = 0
    civilians = 0
    merc = 0
    def __init__(self, name, age = 18, strength = 1, weapon = 'gun', typ='Civilian', dico):
        self.name = name
        self.age = age
        self.strength = strength
        self.weapon = weapon
        self.typ = typ

        Character.nbr += 1

        if self.typ == 'Civilian':
            Character.civilians += 1
        if self.typ == 'Merc':
            Character.merc += 1

        if not isinstance(age, int):
            raise TypeError('The age is not a number !')
        if age < 0 or age > 1000:
            raise ValueError('Inappropriate age !')
        
        if not isinstance(strength, int):
            raise TypeError('The strenght is not a number !')
        if strength < 0 or strength > 10:
            raise ValueError('Are you trying to be strong ?!')
        
class Place:
    nbr = 0
    def __init__(self, city, province, country='NUSA'):
        self.city = city
        self.country = country
        self.province = province
        Character.nbr += 1
        if city == 'Yverdon' or city == 'yverdon':
            raise NameError('Yverdon is too dangerous for your character !')
        Place.nbr += 1

def setting_teller(location):
    print('This place is named', location.city, ', it is located in the state of', location.province, 'in a country named', location.country)


me = Character('V', 19, 5, 'plane', 'Merc')
me2 = Character('w')
me3 = Character('x', 5)
me4 = Character('y', strength=6, weapon='knife')

location = Place('Night City', 'NUSA', 'New California')


setting_teller(location)
print(me.name)
print(me.age)
print(me.strength)
print(me.weapon)
print(me.typ)
print(Character.nbr)
print(Place.nbr)