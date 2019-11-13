import os
import random
import tarot
import name
import demons
import text_output

def generate_total_page(title, subtitle, body_content):
    html_header = "<!DOCTYPE html>\n<html>\n\n<head>\n<title>" + title + "</title>\n<link rel=\"stylesheet\" href=\"styles.css\">\n</head>\n\n"
    html_body = "<body>\n<h1>" + title + "</h1>\n" + "<p><em>" + subtitle + "</em></p><hr>\n" + body_content + "\n</body>\n\n</html>"
    return html_header + html_body

def generate_realms(kings_list, demons_list):
    output = ""
    for king in kings_list:
        output += "<h2>Of the " + king.realm + " realm</h2>\n"
        output += "<p>" + text_output.describe_realm(king) + "</p>\n"
        output += "<h3>Of this realm's King</h3>\n"
        output += "</p>" + text_output.describe_king(king) + "</p>\n"
        output += "<h3>Of this realm's Demons</h3>\n"
        for demon in demons_list:
            if demon.realm == king.realm:
                output += "<p>" + text_output.describe_demon(demon) + "</p>\n"
                output += "<p>" + text_output.describe_ritual(demon) + "</p>\n"
        output += "<hr>\n"
    return output

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
    subtitle = random.choice(first_words) + " " + random.choice(artes_adj) + " " + random.choice(artes_noun) + " " + random.choice(artes_verb) + " " + random.choice(spirits) + " " + random.choice(final) + "\n"
    return subtitle

#Script begins
random.seed()
title = "Grimoire"
subtitle = generate_subtitle()

#useful and necessary lists
names_list = []
tarot_deck = tarot.generate()
random.shuffle(tarot_deck)
kings_list = demons.create_kings(names_list)
demons_list = demons.create_demons(kings_list, names_list, tarot_deck)

#Body content made here
body_content = generate_realms(kings_list, demons_list)
total_html_string = generate_total_page(title, subtitle, body_content)
output_final_html(total_html_string)

#Debug and testing bits

kingcount = 0
while kingcount < 6:
    print(text_output.describe_realm(kings_list[kingcount]))
    print(text_output.describe_king(kings_list[kingcount]))
    print()
    kingcount += 1

demon_count = 0
for demon in demons_list:
    demon_count += 1
    print(text_output.describe_demon(demon))
    print(text_output.describe_ritual(demon))
    print()

"""
for card in tarot_deck:
    print(str(card.number) + ". " + str(card.rank))
"""
