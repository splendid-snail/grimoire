import random

first_syl = ["A", "Na", "Mo", "Ai", "Ba", "Be", "Sa", "E", "Bo", "Gu", "Bu", "Le", "Ba" , "Ar", "Ger", "Dar", "Da", "Cha", "Char", "Haz", "Ha", "He", "Her", "Hor", "Bor", "Ado", "Camu", "Zu"]
cons = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "l", "m", "n", "p", "q", "r", "s", "t", "th", "v", "w", "x", "y", "z"]
vowel = ["a", "e", "i", "o", "u", "y"]
middle_syl = ["az", "mor", "oth", "al", "el", "an", "mar"]
last_syl = ["oth", "eros", "eos", "os", "ar", "son", "mon", "der", "aye", "oin", "er", "alam", "ael", "res", "iel", "mab"]



def magic_word():
    syllables = random.randint(1,3)
    word = random.choice(first_syl) + random.choice(cons)
    while syllables > 0:
        syllable = random.choice(middle_syl)
        word += syllable
        syllables -= 1
    return word

def new(names_list):
    roll = random.randint(0,99)
    """
    0-9: Shortish name
    10-94: Reasonable name
    96-99: Unreasonable name
    """
    name = ""
    unique = False
    while not unique:
        if roll < 10:
            flip = random.randint(0,3)
            if flip == 0:
                name = random.choice(first_syl) + random.choice(cons)
            else:
                name = random.choice(first_syl) + random.choice(cons) + random.choice(last_syl)
        elif roll < 96:
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
