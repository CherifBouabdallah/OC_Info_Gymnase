class Character:
    nbr = 0
    dico_typ = {}
    dico_weapon = {}
    dico_weapon_power = {}

    def __init__(self, name, age = 18, strength = 1, weapon = 'Knife', typ='Civilian', mana=10, life = 500):
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
            victim.life -= Character.dico_weapon_power[self.weapon] + self.power
            self.mana -= 1
        else:
            victim.life -= self.power

    def fight(self, oppo):
        while self.life > 0 and oppo.life > 0:
            self.hit(oppo)
            oppo.hit(self)
            print(self.life, oppo.life)
        if self.life > oppo.life:
            print(self.name, 'wins with', self.life, 'points of life using', self.weapon, 'against', oppo.name, 'that was using', oppo.weapon)
            del(self)
        else:
            print(oppo.name, 'wins with', oppo.life, 'points of life using', oppo.weapon, 'against', self.name, 'that was using', self.weapon)
            del(oppo)


    def reset_life(self):
        self.life = 100

    @property
    def power(self):
        return self.mana + self.age + self.strength
    
    @property
    def intro(self):
        return "Your character's name is "+self.name+ ' and he is ' + str(self.age)+' years old. His strength is ' + str(self.strength)+' and he holds some ' + self.weapon+ '. As a ' + self.typ+ ', he has '+ str(self.mana) + ' mana and ' + str(self.life) + ' points of life.'

        
    def __del__(self):
        print(self.name, 'is dead, haha.')
    
    def __repr__(self):
        return self.name+" is "+str(self.age)+" years old."
    
    def __str__(self):
        return self.name+ ' is '+str(self.age)+" and he is "+self.typ
    