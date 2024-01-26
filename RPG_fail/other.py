def print_character_attributes(character):
    print("Character Attributes:")
    print(f"Name: {character.name}")
    print(f"Age: {character.age}")
    print(f"Strength: {character.strength}")
    print(f"Weapon: {character.weapon}")
    print(f"Type: {character.typ}")
    print(f"Mana: {character.mana}")
    print(f"Life: {character.life}")
    print(f"Spell: {getattr(character, 'spell', None)}")

def setting_teller(location):
    print('This place is named', location.city,'it is located in the state of', location.province, 'in a country named', location.country)

    def __del__(self):
        print("No more of this place")
    
    def __repr__(self):
        return self.city + self.province + self.country
    
    def __str__(self):
        return self.city + self.province + self.country + self.typ
