import os
import random
import tarot
import name
import demons

def generate_total_page(title, subtitle, body_content):
    html_header = "<!DOCTYPE html>\n<html>\n\n<head>\n<title>" + title + "</title>\n<link rel=\"stylesheet\" href=\"styles.css\">\n</head>\n\n"
    html_body = "<body>\n<h1>" + title + "</h1>\n" + "<p><em>" + subtitle + "</em></p>\n" + body_content + "\n</body>\n\n</html>"
    return html_header + html_body

def output_final_html(total_html_string):
    html_file = open("grimoire.html", "w")
    html_file.write(total_html_string)
    html_file.close()

def generate_subtitle():
    first_words = ["Detailing the", "Being the", "Approaching the"]
    artes_adj = ["Ceremonial", "Arcane", "Lost", "Occult"]
    artes_noun = ["Art of", "Practice of", "Method for", "Path to"]
    artes_verb = ["Commanding", "Controlling", "Conjuring", "Drawing Forthe", "Evoking"]
    spirits = ["Spirits", "Spiritual Formes", "Beings", "Daemons"]
    final = ["of Divers Kindes", "of All Sortes", "Completely"]
    subtitle = random.choice(first_words) + " " + random.choice(artes_adj) + " " + random.choice(artes_noun) + " " + random.choice(artes_verb) + " " + random.choice(spirits) + " " + random.choice(final)
    return subtitle

#Script begins
random.seed()
title = "Grimoire"
subtitle = generate_subtitle()

#useful and necessary lists
names_list = []
tarot_deck = tarot.generate()
#random.shuffle(tarot_deck)
kings_list = demons.create_kings(names_list)
demons_list = demons.create_demons(kings_list, names_list, tarot_deck)

#Body content made here
body_content = "<p>Hello world!</p>"
total_html_string = generate_total_page(title, subtitle, body_content)
output_final_html(total_html_string)

#Debug and testing bits
"""
demon_count = 0
for demon in demons_list:
    demon_count += 1
    print(str(demon_count) + ". " + demon.rank + " " + demon.name + " who may appear as a " + demon.human_form)
"""

"""
for card in tarot_deck:
    print(str(card.number) + ". " + str(card.rank))
"""
