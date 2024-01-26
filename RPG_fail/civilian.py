import random
from persos import *

class Civilian(Character):
    def __init__(self, name, age = 18, strength = 1, weapon = 'Knife', typ='Civilian', mana=10, life = 500, spell='spit'):
        super().__init__(name, age, strength=1, weapon='Knife', typ='Civilian' ,mana=0, life=400)
        self.spell = spell

    def __str__(self):
        return self.name+" is a "+self.typ
    
    def Chance(self):
        a = random.randint(0, 5)
        if a == 1:
            self.life += 100