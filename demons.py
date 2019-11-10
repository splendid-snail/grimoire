import name
import random
from language import archaic, article, spirit_forms, human_descriptions, human_forms, planets, animals, trinkets, king_continue, king_consequence, voices

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
            self.rank = random.choice(low_ranks)
        elif card.rank == 1:
            self.rank = random.choice(mid_ranks)
        else:
            self.rank = random.choice(upper_ranks)
        #insert twisted sword easter egg here
        self.animal_form = random.choice(animals)
        self.human_form = random.choice(human_descriptions) + " " + random.choice(human_forms)
        self.spirit_form = random.choice(spirit_forms)
        self.lucky_number = random.randint(1,99)
        self.planet = random.choice(planets)
        self.trinket = random.choice(trinkets)
        self.voice = random.choice(voices)
        """
        To add:
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
        order_in_realm = 1
        while demons_to_make > 0:
            new_demon = Demon(name.new(names_list), tarot_deck[demons_made], king)
            new_demon.order_in_realm = order_in_realm
            demons_list.append(new_demon)
            demons_to_make -= 1
            order_in_realm += 1
            demons_made += 1
    return demons_list

def generate_king_consequence():
    consequence = random.choice(king_consequence)
    if "ANIMAL" in consequence:
        animal = archaic(random.choice(animals))
        indef_article = article(animal)
        consequence = consequence.replace("ANIMAL", animal)
        consequence = consequence.replace("ARTICLE", indef_article)
    return consequence

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

        consequence = generate_king_consequence()
        while consequence in used_consequences:
            consequence = generate_king_consequence()
        used_consequences.append(consequence)
        new_king.consequence = consequence

        kings_list.append(new_king)
        kings_made += 1

    return kings_list
