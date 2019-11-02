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
<<<<<<< HEAD
    final = ["of Divers Kindes", "of All Sortes", "Completely"]
    subtitle = random.choice(first_words) + " " + random.choice(artes_adj) + " " + random.choice(artes_noun) + " " + random.choice(artes_verb) + " " + random.choice(spirits) + " " + random.choice(final)
    return subtitle

def name():
    first_syl = ["Az", "Nab", "Mor", "Ai", "Bath", "Beth", "Sal", "Eli", "Bot", "Gus", "Bu", "Ler", "Bar" "Ab", "Arg"]
    middle_syl = ["az", "mor", "oth", "al", "ell", "el", "all", "an"]
    last_syl = ["oth", "eros", "eos", "os", "ar", "son", "mon", "der", "aye", "oin", "er", "alam", "ael", "res", "iel"]
    roll = random.randint(0,99)
    """
    0-9: Short name
    10-94: Reasonable name
    95-99: Unreasonable name
    """
    print(roll)


=======
    final = ["of Divers Kindes", "of All Sortes", "Completely", "as it had been Passed Downe"]
    subtitle = random.choice(first_words) + " " + random.choice(artes_adj) + " " + random.choice(artes_noun) + " " + random.choice(artes_verb) + " " + random.choice(spirits) + " " + random.choice(final)
    return subtitle

>>>>>>> 9125373e323356f81a3bb15ca1cf30a336194a46

#Script begins
title = "Grimoire"
subtitle = generate_subtitle()
body_content = "<p>Hello world!</p>"
total_html_string = generate_total_page(title, subtitle, body_content)
<<<<<<< HEAD
random.seed()
name()
=======
>>>>>>> 9125373e323356f81a3bb15ca1cf30a336194a46
output_final_html(total_html_string)
