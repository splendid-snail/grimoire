import language
import random
import markov
from language import archaic, article, ordinal
from html_output import paragraph
from name import magic_word

def generate_subtitle():
    first_words = ["Detailing the", "Being the", "Approaching the"]
    artes_adj = ["Ceremonial", "Arcane", "Lost", "Occult"]
    artes_noun = ["Art of", "Practice of", "Method for", "Path to"]
    artes_verb = ["Commanding", "Controlling", "Conjuring", "Drawing Forthe", "Evoking"]
    spirits = ["Spirits", "Spiritual Formes", "Beings", "Daemons"]
    final = ["of Divers Kindes", "of All Sortes", "Completely"]
    subtitle = random.choice(first_words) + " " + random.choice(artes_adj) + " " + random.choice(artes_noun) + " " + random.choice(artes_verb) + " " + random.choice(spirits) + " " + random.choice(final) + "\n"
    return subtitle

def write_intro():
    output = random.choice(language.general_intro)
    while "POS_ADJ" in output:
        output = output.replace("POS_ADJ", archaic(random.choice(language.positive_adj)), 1)
    while "TRUE_ADJ" in output:
        output = output.replace("TRUE_ADJ", archaic(random.choice(language.true_adj)), 1)
    while "NEG_ADJ_1" in output:
        output = output.replace("NEG_ADJ_1", archaic(random.choice(language.negative_adj)))
    while "FALSE_ADJ" in output:
        output = output.replace("FALSE_ADJ", archaic(random.choice(language.false_adj)), 1)
    while "CONSEQUENCE" in output:
        output = output.replace("CONSEQUENCE", random.choice(language.intro_consequences))
    return output

def set_realm_attribs(realm_attribs, output):
        first_attrib = random.choice(realm_attribs)
        second_attrib = first_attrib
        while second_attrib == first_attrib:
            second_attrib = random.choice(realm_attribs)
        third_attrib = random.choice(realm_attribs)
        while third_attrib == first_attrib or third_attrib == second_attrib:
            third_attrib = random.choice(realm_attribs)
        first_attrib = archaic(first_attrib)
        second_attrib = archaic(second_attrib)
        third_attrib = archaic(third_attrib)
        output += first_attrib + " and " + second_attrib
        continued = random.choice(language.realm_attrib_continued)
        continued = continued.replace("OBJECT", third_attrib)
        output += continued
        return output

def describe_realm(king):
    realm = king.realm
    flip = random.randint(0,1)
    output = ""
    if flip > 0: #passive intro
        output += random.choice(language.realm_intros_passive) + " " + archaic(random.choice(language.ruled_passive)) + " by the " + archaic(random.choice(language.king_adj)) + " " + archaic(king.title) + " " + king.name + ". "
    else: #active intro
        output += "The " + archaic(random.choice(language.king_adj)) + " " + archaic(king.title) + " " + king.name + " " + archaic(random.choice(language.ruled_active)) + " this realm. "
    output += random.choice(language.realm_attrib_intros)
    if realm == "North":
        output = set_realm_attribs(language.north_attribs, output)
    elif realm == "East":
        output = set_realm_attribs(language.east_attribs, output)
    elif realm == "South":
        output = set_realm_attribs(language.south_attribs, output)
    elif realm == "West":
        output = set_realm_attribs(language.west_attribs, output)
    elif realm == "Upper":
        output = set_realm_attribs(language.upper_attribs, output)
    elif realm == "Lower":
        output = set_realm_attribs(language.lower_attribs, output)
    return output

def describe_king(king):
    output = random.choice(language.king_intros)
    our_article = article(king.title)
    output = output.replace("NAME", king.name)
    output = output.replace("ARTICLE", our_article)
    output = output.replace("TITLE", king.title)
    if king.cont[0] != ".":
        output += " "
    output += king.cont
    output += " "
    output += random.choice(language.king_consequence_intros) + king.consequence
    output += " "
    output += random.choice(language.king_form_intros) + article(king.animal_form_one) + " " + archaic(king.animal_form_one) + " or " + article(king.animal_form_two) + " " + archaic(king.animal_form_two) + random.choice(language.king_form_endings)
    return output

def demon_intro(demon):
    output = "<strong>The " + ordinal(demon.order_in_realm) + " demon</strong> in the " + demon.realm + " realm is " + demon.name
    return output

def demon_voice(demon):
    output = random.choice(language.demon_voices)
    output = output.replace("VOICE_TYPE", demon.voice)
    return output

def demon_forms(demon):
    output = random.choice(language.demon_animal_form)
    indef_article = article(demon.animal_form)
    output = output.replace("ANIMAL", archaic(demon.animal_form))
    output = output.replace("ARTICLE", indef_article)

    output += random.choice(language.demon_spirit_form)
    indef_article = article(demon.spirit_form)
    output = output.replace("ARTICLE", indef_article)
    output = output.replace("SPIRIT_FORM", archaic(demon.spirit_form))

    output += " " + random.choice(language.demon_human_form)
    indef_article = article(demon.human_form)
    output = output.replace("ARTICLE", indef_article)
    output = output.replace("HUMAN_FORM", archaic(demon.human_form))
    return output

def demon_skills(demon):
    output = " " + random.choice(language.he_can_intros)
    output += demon.skill
    output += "."
    return output

def demon_rank(demon):
    if demon.card.rank == 0:
        output = random.choice(language.low_rank_intros)
    elif demon.card.rank == 1:
        output = random.choice(language.mid_rank_intros)
    else:
        output = random.choice(language.high_rank_intros)
    output = output.replace("RANK", demon.rank)
    output = output.replace("KING_NAME", demon.king.name)
    return output

def demon_commands(demon):
    if demon.card.rank == 0:
        output = random.choice(language.demon_commands_low)
        sum = str(random.randint(2,5))
        output = output.replace("SUM", sum)
    elif demon.card.rank == 1:
        output = random.choice(language.demon_commands_mid)
        sum = str(random.randint(10,30))
        output = output.replace("SUM", sum)
    else:
        output = random.choice(language.demon_commands_high)
        sum = str(random.randint(30,102))
        output = output.replace("SUM", sum)
    output = output.replace("DEMON_NAME", demon.name)
    output = output.replace("DEMON_RANK", demon.rank)
    output = output.replace("KING_NAME", demon.king.name)
    return output

def demon_planet(demon):
    output = random.choice(language.demon_planet)
    output = output.replace("DEMON_NAME", demon.name)
    output = output.replace("PLANET_NAME", demon.planet)
    return output

def describe_demon(demon):
    output = "<div id=\"" + demon.name + "\">"
    output += demon_intro(demon)
    output += ". "
    output += demon_rank(demon)
    output += " "
    output += demon_commands(demon)
    output += " "
    output += demon_voice(demon)
    output += " "
    output += demon_forms(demon)
    output += " "
    output += demon_skills(demon)
    output += " "
    output += demon_planet(demon)
    output += "</div>"
    return output

def describe_ritual(demon):
    output = ""
    if demon.card.rank == 0 or demon.card.rank == 1:
        flip = random.randint(0,1)
        if flip > 0:
            #DANCE RITUAL
            #intro
            output += paragraph(random.choice(language.dance_ritual_intros))
            #first step
            output += "<p>" + random.choice(language.dance_ritual_first_steps) + "</p>\n"
            verb = archaic(random.choice(language.dance_ritual_verbs))
            poss_pronoun = archaic(random.choice(language.second_person_poss_pronouns))
            second_pronoun = archaic(random.choice(language.second_person_pronouns))
            part = archaic(random.choice(language.dance_ritual_parts))
            output = output.replace("VERB", verb)
            output = output.replace("PART", part)
            output = output.replace("POSS_PRONOUN", poss_pronoun)
            output = output.replace("SECOND_PRONOUN", second_pronoun)
            #second step
            output += "<p>" + random.choice(language.dance_ritual_second_steps) + "</p>\n"
            verb_one = archaic(random.choice(language.dance_ritual_verbs))
            verb_two = archaic(random.choice(language.dance_ritual_verbs))
            poss_pronoun = archaic(random.choice(language.second_person_poss_pronouns))
            part_one = archaic(random.choice(language.dance_ritual_parts))
            part_two = archaic(random.choice(language.dance_ritual_parts))
            output = output.replace("VERB_ONE", verb_one)
            output = output.replace("VERB_TWO", verb_two)
            output = output.replace("PART_ONE", part_one)
            output = output.replace("PART_TWO", part_two)
            output = output.replace("POSS_PRONOUN", poss_pronoun)
            #third step
            output += "<p>" + random.choice(language.dance_ritual_final_steps) + "</p>\n"
            verb = archaic(random.choice(language.dance_ritual_verbs))
            poss_pronoun = archaic(random.choice(language.second_person_poss_pronouns))
            part = archaic(random.choice(language.dance_ritual_parts))
            output = output.replace("VERB", verb)
            output = output.replace("PART", part)
            output = output.replace("POSS_PRONOUN", poss_pronoun)
            output = output.replace("MAGIC_WORD", magic_word())
        else:
            #CIRCLE RITUAL
            output += paragraph(random.choice(language.circle_ritual_intros))
            #first step
            output += paragraph(random.choice(language.circle_ritual_first_steps))
            #second step
            output += paragraph(random.choice(language.circle_ritual_second_steps))
            size = str(random.randint(4,10))
            colour = archaic(random.choice(language.colours))
            output = output.replace("SIZE", size)
            output = output.replace("COLOUR", colour)
            hands = ["left", "right"]
            flip = random.randint(0,1)
            if flip > 0:
                output += " You must do this with your " + archaic(random.choice(hands)) + " hand, or "
                consequence = random.choice(language.consequences_list)
                if "ANIMAL" in consequence:
                    animal = archaic(random.choice(language.animals))
                    our_article = article(animal)
                    consequence = consequence.replace("ANIMAL", animal)
                    consequence = consequence.replace("ARTICLE", our_article)
                if "HUMAN_FORM" in consequence:
                    human_form = archaic(random.choice(language.human_forms))
                    human_description = archaic(random.choice(language.human_descriptions))
                    our_article = article(human_description)
                    consequence = consequence.replace("HUMAN_DESCRIPTION", human_description)
                    consequence = consequence.replace("HUMAN_FORM", human_form)
                    consequence = consequence.replace("ARTICLE", our_article)
                output += consequence + "."
            output += "</p>\n"
            #third step
            output += paragraph(random.choice(language.circle_ritual_final_steps))
            word_one = magic_word()
            word_two = magic_word()
            word_three = magic_word()
            word_four = magic_word()
            output = output.replace("WORD_ONE", word_one)
            output = output.replace("WORD_TWO", word_two)
            output = output.replace("WORD_THREE", word_three)
            output = output.replace("WORD_FOUR", word_four)
    else:
        #SACRIFICE RITUAL
        #Intro
        output += paragraph(random.choice(language.sacrifice_ritual_intros))
        output += paragraph(random.choice(language.sacrifice_animal_intros))
        animal = archaic(random.choice(language.sacrifice_animals))
        this_article = archaic(article(animal))
        output = output.replace("ARTICLE", this_article)
        output = output.replace("ANIMAL", animal)

        #First step - place
        output += paragraph(random.choice(language.sacrifice_ritual_first_steps))
        place = archaic(random.choice(language.sacrifice_places))
        our_article = archaic(article(place))
        output = output.replace("ARTICLE", our_article)
        output = output.replace("SACRIFICE_PLACE", place)
        #Second step - altar
        output += paragraph(random.choice(language.sacrifice_ritual_second_steps))
        altar = archaic(random.choice(language.altar_types))
        output = output.replace("ALTAR_TYPE", altar)
        #Third step - get the tool and the animal together
        output += paragraph(random.choice(language.sacrifice_ritual_third_steps))
        tool = archaic(random.choice(language.sacrifice_tools))
        our_article = archaic(article(tool))
        output = output.replace("ANIMAL", animal)
        output = output.replace("TOOL", tool)
        output = output.replace("ARTICLE", our_article)
        #Song step - because why not
        output += paragraph(random.choice(language.sacrifice_ritual_songs))
        new_magic_word = magic_word()
        output = output.replace("MAGIC_WORD", new_magic_word)
        #And the climax
        output += paragraph(random.choice(language.sacrifice_ritual_climax))
        output = output.replace("ANIMAL", animal)
        output = output.replace("TOOL", tool)
        output = output.replace("DEMON_NAME", demon.name)
        output = output.replace("DEMON_RANK", demon.rank)
    #Invocation begins
    output += "<p>Now at this Climax of the ritual, to invoke the " + demon.rank + " " + demon.name + " intone the following:</p>\n"
    output += "<p>By "+ markov.incantation(50) + "</p>\n"
    output = output.replace("DEMON_NAME", demon.name)
    output = output.replace("DEMON_RANK", demon.rank)
    output = output.replace("KING_NAME", demon.king.name)
    output = output.replace("KING_TITLE", demon.king.title)
    return output
