import os
import random

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

def name(names_list):
    first_syl = ["A", "Na", "Mo", "Ai", "Ba", "Be", "Sa", "E", "Bo", "Gu", "Bu", "Le", "Ba" , "Ar"]
    cons = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "l", "m", "n", "p", "q", "r", "s", "t", "th", "v", "w", "x", "y", "z"]
    vowel = ["a", "e", "i", "o", "u", "y"]
    middle_syl = ["az", "mor", "oth", "al", "el", "an"]
    last_syl = ["oth", "eros", "eos", "os", "ar", "son", "mon", "der", "aye", "oin", "er", "alam", "ael", "res", "iel"]
    roll = random.randint(0,99)
    """
    0-9: Shortish name
    10-94: Reasonable name
    95-99: Unreasonable name
    """
    name = ""
    unique = False
    while not unique:
        if roll < 10: #Just to test for now
            flip = random.randint(0,3)
            if flip == 0:
                name = random.choice(first_syl) + random.choice(cons)
            else:
                name = random.choice(first_syl) + random.choice(cons) + random.choice(last_syl)
        elif roll < 95:
            syllables = random.randint(1,3)
            name += random.choice(first_syl) + random.choice(cons)
            while syllables > 0:
                syllable = random.choice(middle_syl)
                name += syllable
                syllables -= 1
        else:
            repeats = random.randint(3,7)
            name = random.choice(first_syl) + random.choice(cons)
            repeat_syl = random.choice(cons) + random.choice(vowel)
            while repeats > 0:
                name += repeat_syl
                repeats -= 1
            flip = random.randint(0,1)
            if flip > 0:
                name += random.choice(cons)
        if not name in names_list:
            unique = True
    names_list.append(name)
    return name

#Script begins
random.seed()

title = "Grimoire"
subtitle = generate_subtitle()

body_content = "<p>Hello world!</p>"

total_html_string = generate_total_page(title, subtitle, body_content)
output_final_html(total_html_string)
