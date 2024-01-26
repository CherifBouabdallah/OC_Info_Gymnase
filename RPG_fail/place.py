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