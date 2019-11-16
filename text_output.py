import language
import random
import markov
from language import archaic, article, ordinal

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
    if demon.rank == 0:
        output += random.choice(language.low_rank_skills)
    elif demon.rank == 1:
        output += random.choice(language.mid_rank_skills)
    else:
        output += random.choice(language.high_rank_skills)
    output += "."
    return output

def demon_rank(demon):
    if demon.rank == 0:
        output = random.choice(language.low_rank_intros)
    elif demon.rank == 1:
        output = random.choice(language.mid_rank_intros)
    else:
        output = random.choice(language.high_rank_intros)
    output = output.replace("RANK", demon.rank)
    output = output.replace("KING_NAME", demon.king.name)
    return output

def demon_planet(demon):
    output = random.choice(language.demon_planet)
    output = output.replace("DEMON_NAME", demon.name)
    output = output.replace("PLANET_NAME", demon.planet)
    return output

def describe_demon(demon):
    output = demon_intro(demon)
    output += ". "
    output += demon_rank(demon)
    output += " "
    output += demon_voice(demon)
    output += " "
    output += demon_forms(demon)
    output += " "
    output += demon_skills(demon)
    output += " "
    output += demon_planet(demon)
    return output

def describe_ritual(demon):
    output = ""
    if demon.card.rank == 0 or demon.card.rank == 1:
        flip = random.randint(0,1)
        if flip > 0:
            ritual_type = "dance"
            #intro
            output += "<p>" + random.choice(language.dance_ritual_intros) + "</p>\n"
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
            output = output.replace("POSS_PRONOUN", poss_pronoun)
            output = output.replace("PART_ONE", part_one)
            output = output.replace("PART_TWO", part_two)
            #third step
            output += "<p>" + random.choice(language.dance_ritual_final_steps) + "</p>\n"
            verb = archaic(random.choice(language.dance_ritual_verbs))
            poss_pronoun = archaic(random.choice(language.second_person_poss_pronouns))
            part = archaic(random.choice(language.dance_ritual_parts))
            output = output.replace("VERB", verb)
            output = output.replace("PART", part)
            output = output.replace("POSS_PRONOUN", poss_pronoun)            
        else:
            ritual_type = "circle"
            output += "<p>" + random.choice(language.circle_ritual_intros) + "</p>\n"
    else:
        ritual_type = "sacrifice"
        output += "<p>" + random.choice(language.sacrifice_ritual_intros) + "</p>\n"
    output += "<p>Now at the climax of the ritual, to invoke the " + demon.rank + " " + demon.name + ", say the following words:</p>\n"
    output += "<p>By "+ markov.incantation() + "</p>\n"
    output = output.replace("NAME", demon.name)
    return output
