import language
import random
from language import archaic

def describe_realm(king):
    output = ""
    realm = king.realm
    flip = random.randint(0,1)
    if flip > 0: #passive intro
        output += random.choice(language.realm_intros_passive) + " " + archaic(random.choice(language.ruled_passive)) + " by the " + archaic(random.choice(language.king_adj)) + " " + archaic(king.title) + " " + king.name + ". "
    else: #active intro
        output += "The " + archaic(random.choice(language.king_adj)) + " " + archaic(king.title) + " " + king.name + " " + archaic(random.choice(language.ruled_active)) + " this realm. "
    output += random.choice(language.realm_attrib_intros)
    if realm == "North":
        output += "North stuff"
    elif realm == "East":
        output += "East stuff"
    elif realm == "South":
        output += "South stuff"
    elif realm == "West":
        output += "West stuff"
    elif realm == "Upper":
        output += "Upper stuff"
    elif realm == "Lower":
        output += "Lower stuff"
    return output
