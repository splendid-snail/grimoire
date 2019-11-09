import name
import random
from language import archaic, spirit_forms, human_descriptions, human_forms, planets, animals, trinkets, king_continue, king_consequence

class Demon:
    def __init__(self, name, card, king):
        upper_ranks = ["Archduke", "President", "Prince", "Despot", "Duke"]
        mid_ranks = ["Marquiz", "Count", "Earl"]
        low_ranks = ["Knight", "Baronet", "Seigneur", "Viscount"]
        self.name = name
        self.card = card
        self.king = king
        self.realm = king.realm
        if card.rank == 0:
            self.rank = archaic(random.choice(low_ranks))
        elif card.rank == 1:
            self.rank = archaic(random.choice(mid_ranks))
        else:
            self.rank = archaic(random.choice(upper_ranks))
        #insert twisted sword easter egg here
        self.animal_form = archaic(random.choice(animals))
        self.human_form = archaic(random.choice(human_descriptions)) + " " + archaic(random.choice(human_forms))
        self.spirit_form = archaic(random.choice(spirit_forms))
        self.lucky_number = random.randint(1,99)
        self.planet = archaic(random.choice(planets))
        self.trinket = archaic(random.choice(trinkets))
        """
        To add:
        * voice
        * consequences (split by rank?)
        * skills
        * sign of presence / voice
        """

class King:
    def __init__(self, name, realm):
        titles = ["Lord", "King", "Emperor", "Basileus"]
        self.name = name
        self.title = random.choice(titles)
        self.realm = realm
        animals_set = False
        while not animals_set:
            self.animal_form_one = random.choice(animals)
            self.animal_form_two = random.choice(animals)
            if self.animal_form_one != self.animal_form_two:
                animals_set = True

def create_demons(kings_list, names_list, tarot_deck):
    """WORK IN PROGRESS"""
    demons_made = 0
    demons_list = []
    for king in kings_list:
        demons_to_make = 13
        while demons_to_make > 0:
            new_demon = Demon(name.new(names_list), tarot_deck[demons_made], king)
            demons_list.append(new_demon)
            demons_to_make -= 1
            demons_made += 1
    return demons_list

def create_kings(names_list):
    kings_made = 0
    kings_list = []
    realms = ["North", "East", "South", "West", "Upper", "Lower"]
    used_continues = []
    used_consequences = []
    while kings_made < 6:
        new_king = King(name.new(names_list), realms[kings_made])

        cont = random.choice(king_continue)
        while cont in used_continues:
            cont = random.choice(king_continue)
        used_continues.append(cont)
        new_king.cont = cont

        consequence = random.choice(king_consequence)
        while consequence in used_consequences:
            consequence = random.choice(king_consequence)
        used_consequences.append(consequence)
        new_king.consequence = consequence

        kings_list.append(new_king)
        kings_made += 1
        
    return kings_list
