import time
import math

class Character:
    nbr = 0
    dico_typ = {}
    dico_weapon = {}
    dico_weapon_power = {}

    def __init__(self, name, age = 18, strength = 1, weapon = 'Knife', typ='Civilian', mana=10, life = 100):
        self.name = name
        self.age = age
        self.strength = strength
        self.weapon = weapon
        self.typ = typ
        self.mana = mana
        self.life = life

        Character.nbr += 1

        if self.typ in Character.dico_typ:
            Character.dico_typ[self.typ] += 1
        else:
            Character.dico_typ[self.typ] = 1

        if self.weapon in Character.dico_weapon:
            Character.dico_weapon[self.weapon] += 1
        else:
            Character.dico_weapon[self.weapon] = 1

        Character.dico_weapon_power['Blades'] = 5
        Character.dico_weapon_power['Gun'] = 10
        Character.dico_weapon_power['Knife'] = 3

    
        if not isinstance(age, int):
            raise TypeError('The age is not a number !')
        if age < 0 or age > 1000:
            raise ValueError('Inappropriate age !')
        
        if not isinstance(strength, int):
            raise TypeError('The strenght is not a number !')
        if strength < 0 or strength > 10:
            raise ValueError('Are you trying to be strong ?!')
        

    def fatigue(self): 
        self.mana -= 2
    def repose(self): 
        self.mana += 2

    def potion(self, vie):
        self.life += vie

    def hit(self, victim):
        if self.weapon in Character.dico_weapon_power:
            victim.life -= Character.dico_weapon_power[self.weapon]
            self.mana -= 1
        else:
            victim.life -= self.stength

    def fight(self, oppo):
        while self.life > 0 and oppo.life > 0:
            self.hit(oppo)
            oppo.hit(self)
            print(self.life, oppo.life)
        if self.life > oppo.life:
            print(self.name, 'wins with', self.life, 'points of life using', self.weapon, 'against', oppo.name, 'that was using', oppo.weapon)
        else:
            print(oppo.name, 'wins with', oppo.life, 'points of life using', oppo.weapon, 'against', self.name, 'that was using', self.weapon)

    def reset_life(self):
        self.life = 100
        
class Place:
    nbr = 0
    dico_typ = {}
    dico_typ_power = {}
    def __init__(self, city, province, country='NUSA', typ='City'):
        self.city = city
        self.country = country
        self.province = province
        self.typ = typ
        if city == 'Yverdon' or city == 'yverdon':
            raise NameError('Yverdon is too dangerous for your character !')
        Place.nbr += 1
    
        Place.dico_typ_power['City'] = 5
        Place.dico_typ_power['Forest'] = 10
        Place.dico_typ_power['Desert'] = 3

        if self.typ in Place.dico_typ:
            Place.dico_typ[self.typ] += 1
        else:
            Place.dico_typ[self.typ] = 1


def setting_teller(location):
    print('This place is named', location.city,'it is located in the state of', location.province, 'in a country named', location.country)


me = Character('V', 19, 5, 'Blades', 'Merc')
me2 = Character('W', typ='Merc', weapon='Gun')
me3 = Character('X', 5)
me4 = Character('Y', strength=6, weapon='Gun')

location = Place('Night City', 'New California', 'NUSA')


setting_teller(location)
print(Character.dico_typ)
print(Character.dico_weapon)
print(Character.dico_weapon_power)
print(me.life)
print(me2.life)
#me.fight(me2)
#me.fight(me3)
print(Place.dico_typ_power)
print(Place.dico_typ)
