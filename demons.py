import name
import random
import sigils
import language
from language import archaic, article

class Demon:
    def __init__(self, name, card, king):

        self.name = name
        self.card = card
        self.king = king
        self.realm = king.realm
        self.order = 0 #serial number, starts at 1, assigned in demon creation function
        if card.rank == 0:
            self.rank = random.choice(language.low_ranks)
            self.skill = random.choice(language.normal_skills)
        elif card.rank == 1:
            self.rank = random.choice(language.mid_ranks)
            self.skill = random.choice(language.normal_skills)
        else:
            self.rank = random.choice(language.upper_ranks)
            self.skill = random.choice(language.high_rank_skills)
        self.skill = self.skill.replace("ANIMAL", archaic((random.choice(language.animals) + "s")))
        self.skill = self.skill.replace("POS_ADJ", archaic(random.choice(language.positive_adj)))
        self.skill = self.skill.replace("TRUE_ADJ", archaic(random.choice(language.true_adj)))
        self.skill = self.skill.replace("STRENGTH", archaic(random.choice(language.strengths)))
        #insert twisted sword easter egg here
        self.animal_form = random.choice(language.animals)
        self.human_form = random.choice(language.human_descriptions) + " " + random.choice(language.human_forms)
        self.spirit_form = random.choice(language.spirit_forms)
        self.lucky_number = random.randint(1,99)
        self.planet = random.choice(language.planets)
        self.trinket = random.choice(language.trinkets)
        self.voice = random.choice(language.voices)
        if self.card.suit == "Swords":
            if self.card.name[:4] == "VII ":
                self.skill = "maketh thee drunk and give thee Five swords"
            elif self.card.name[:3] == "IX ":
                self.skill = "maketh thy foes Wake in the night surrounded by the Swords that shall be their Death"





class King:
    def __init__(self, name, realm):

        self.name = name
        self.title = random.choice(language.king_titles)
        self.realm = realm
        animals_set = False
        while not animals_set:
            self.animal_form_one = random.choice(language.animals)
            self.animal_form_two = random.choice(language.animals)
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
            new_demon.order = demons_made
            #make sigil here
            sigils.create_sigil(new_demon)

    return demons_list

def generate_king_consequence():
    consequence = random.choice(language.king_consequence)
    if "ANIMAL" in consequence:
        animal = archaic(random.choice(language.animals))
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

        cont = random.choice(language.king_continue)
        while cont in used_continues:
            cont = random.choice(language.king_continue)
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
