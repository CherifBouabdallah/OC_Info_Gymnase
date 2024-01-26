from persos import *
from merc import *
from civilian import *
from place import *
from other import *


me = Merc('V', life=5000s)
me2 = Character('W', typ='Merc', weapon='Gun')
me3 = Character('X', 50)
me4 = Character('Y', strength=6, weapon='Gun')
me5 = Civilian('Z')

location = Place('Night City', 'New California', 'NUSA')

print(Character.dico_typ)
print(Character.dico_weapon)
print_character_attributes(me)

me.fight(me2)
me.reset_life()
me.fight(me3)
