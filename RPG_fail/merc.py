from persos import*

class Merc(Character):
    def __init__(self, name, age = 32, strength = 10, weapon = 'Gun', typ='Merc', mana=5, life = 600, spell='Punch'):
        super().__init__(name, age, strength, weapon, typ, mana, life)
        self.spell = spell

    def __str__(self):
        return self.name+" is a "+self.typ+"and he is stronger than you."