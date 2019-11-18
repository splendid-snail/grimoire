import random

# USED IN DEMON/KING GEN
animals = ["aardvark","alligator","antelope","ape","armadillo","baboon","badger","bat","bear","beaver","bison","boar","bull","camel","canary","capybara","cat","chameleon","cheetah","chimpanzee","chinchilla","chipmunk","cougar","cow","coyote","crocodile","crow","deer","dingo","dog","donkey","dromedary","elephant","elk","ewe","ferret","finch","fish","fox","frog","gazelle","gilamonster","giraffe","gnu","goat","gopher","gorilla","grizzlybear","groundhog","guineapig","hamster", "halibut", "hedgehog","hippopotamus","hog","horse","hyena","ibex","iguana","impala","jackal","jaguar","kangaroo","koala","lamb","lemur","leopard","lion","lizard","llama","lynx","mandrill","marmoset","mink","mole","mongoose","monkey","moose","mouse","mule","newt","ocelot","opossum","orangutan","oryx","otter","ox","panda","panther","parakeet","parrot","pig","platypus","polar Bear","porcupine","porpoise","puma","rabbit","raccoon","ram","rat","reindeer","reptile","rhinoceros","salamander","seal","sheep","shrew","silverfish","skunk","sloth","snake","squirrel","tapir","tiger","toad","turtle","walrus","warthog","weasel","whale","wildcat","wolf","wolverine","zebra"]
human_forms = ["nun", "prior", "abbot", "merchant", "monsignor", "clerk", "carpenter", "mason", "chef", "cook", "servant", "judge", "washerwoman", "fishmonger", "cooper", "fletcher", "peasant", "mayor", "jester", "clown", "maid", "clerk"]
human_descriptions = ["able","abnormal","absent-minded","adventurous","affectionate","agile","agreeable","amazing","ambitious","amiable","amusing","analytical","angelic","apathetic","apprehensive","ardent","artificial","artistic","assertive","attentive","average","awful","balanced","beautiful","beneficent","blue","blunt","boisterous","brave","bright","brilliant","buff","callous","candid","cantankerous","capable","careful","careless","caustic","cautious","charming","childish","childlike","cheerful","churlish","circumspect","civil","clean","clever","clumsy","coherent","cold","competent","composed","conceited","condescending","confident","confused","conscientious","considerate","content","cool","cooperative","cordial","courageous","cowardly","crafty","crass","critical","cruel","curious","cynical","dainty","decisive","deep","deferential","deft","delicate","delightful","demure","depressed","devoted","dextrous","diligent","direct","dirty","disagreeable","discerning","discreet","disruptive","distant","distraught","distrustful","dowdy","dramatic","dreary","drowsy","drugged","drunk","dull","dutiful","eager","earnest","easy-going","efficient","egotistical","elfin","emotional","energetic","enterprising","enthusiastic","evasive","even-tempered","exacting","excellent","excitable","experienced","fabulous","fastidious","ferocious","fervent","fiery","flabby","flaky","flashy","frank","friendly","funny","fussy","generous","gentle","gloomy","glutinous","good","grave","great","groggy","guarded","hateful","hearty","helpful","hesitant","hot-headed","hysterical","idiotic","idle","imaginative","immature","immodest","impatient","imperturbable","impetuous","impractical","impressionable","impressive","impulsive","inactive","incisive","incompetent","inconsiderate","inconsistent","indiscreet","indolent","industrious","inexperienced","insensitive","inspiring","intelligent","interesting","intolerant","inventive","irascible","irritable","irritating","jocular","jovial","joyous","judgmental","keen","kind","lame","lazy","lean","leery","lethargic","listless","lithe","lively","local","logickal","long-winded","lovable","love-lorn","lovely","maternal","mature","mean","meddlesome","mercurial","methodical","meticulous","mild","miserable","modest","moronic","morose","musical","naive","nasty","natural","naughty","negative","nervous","noisy","normal","nosy","numb","obliging","obnoxious","old-fashioned","orderly","ostentatious","outgoing","outspoken","passionate","passive","patient","peaceful","peevish","pensive","persevering","petulant","picky","plain","plain-speaking","playful","pleasant","plucky","polite","popular","positive","powerful","practical","prejudiced","pretty","proficient","proud","provocative","prudent","punctual","quarrelsome","querulous","quick","quick-tempered","quiet","reassuring","reclusive","reliable","reluctant","resentful","reserved","resigned","resourceful","respected","respectful","responsible","restless","revered","ridiculous","sad","saucy","sedate","selfish","sensible","sensitive","sentimental","serene","serious","sharp","short-tempered","shrewd","shy","silly","sincere","sleepy","slight","sloppy","slothful","slovenly","slow","smart","sneering","snobby","somber","sober","sophisticated","soulful","soulless","sour","spirited","spiteful","stable","staid","steady","stern","stoic","striking","strong","stupid","sturdy","subtle","sullen","sulky","supercilious","superficial","surly","suspicious","sweet","tactful","tactless","talented","testy","thinking","thoughtful","thoughtless","timid","tired","tolerant","touchy","tranquil","ugly","unaffected","unbalanced","uncertain","uncooperative","undependable","unemotional","unfriendly","unguarded","unhelpful","unimaginative","unmotivated","unpleasant","unpopular","unreliable","unstable","unsure","unthinking","unwilling","venal","versatile","vigilant","warm","warmhearted","wary","watchful","weak","well-behaved","willing","wonderful","volcanic","vulnerable","zealous"]
spirit_forms = ["angel","flame", "fire", "flaming fire","centaur","chimera","cockatrice","cyclops","djinn","dragon","dryad","dwarf","faun","gargoyle","ghast","ghost","ghoul","giant","goblin","golem","gorgon","gremlin","griffon","hag","harpy","hippogriff","hobgoblin","homonculus","hydra","imp","incubus","kappa","kobold","kraken","lamassu","leprechaun","lich","manticore","mermaid","merman","minotaur","mummy","nix","nymph","ogre","orc","pegasus","phoenix","poltergeist","roc","satyr","selkie","siren","spectre","sphinx","sprite","succubus","sylph","warg","werewolf","wight","wraith","wyvern"]
planets = ["Mercury", "Venus", "Earth", "Mars", "Saturn", "Uranus", "Neptune", "Pluto"]
voices = ["rough","beguiling","melodic","melodious","frightening","fearsome","mad","loud","oily","wheedling","reedy","pleading","desperate", "shaky", "booming"]
king_adj = ["mighty", "powerful", "cruel", "fearsome"]
trinkets = ["candle", "holy book", "whistle", "thorny twig", "mirror", "polished stone", "rough stone", "small bell", "great bell", "plate of food", "cup of ale", "bloody cloth", "torn rag", "painting fragment", "parchment of a prayer", "priest's collar", "sweet-smelling cloth", "old cloak", "nun's habit", "pie dish", "empty cup", "cracked mirror", "trumpet", "bugle", "lyre", "reed", "dried frog", "lifeless mouse", "old key", "small piece of chain"]

#UTILITY IN TEXT GEN
unmoddable_letters = ["a", "e", "i", "o", "u", "c"]
vowels = ["a", "e", "i", "o", "u"]
second_person_pronouns = ["you", "thou"]
second_person_poss_pronouns = ["your", "thy"]
colours = ["red", "green", "blue", "yellow", "black", "white"]

#REALM RELATED
north_attribs = ["cold", "earth", "snow",]
east_attribs = ["air", "clouds", "things of the intellect", "communication", "balance", "mists"]
south_attribs = ["fire", "creativity", "danger", "lively spirits","flames", "thrills"]
west_attribs = ["water", "beauty", "waves", "mysterious ripplings", "froth", "bubble"]
upper_attribs = ["light", "beams", "rays", "shafts", "feathers"]
lower_attribs = ["darkness", "sins", "hidden things", "shadows", "things that crawl", "clods", "roots", "bones"]

ruled_passive = ["ruled", "governed", "overseen", "maintained", "dominated"]
ruled_active = ["rules", "governs", "oversees", "maintains", "dominates"]
realm_intros_passive = ["This realm is", "This kingdom is", "Know that this realm is"]
realm_attrib_intros = ["It is the realm of ", "Here in this realm is ", "This is a realm with attributes of ", "Here are ", "This is the traditional home of ", "It has longe been known to the learned as the realm of ", "In this realm`s Pleroma are the spirits of ", "Among the strongest influences here are "]
realm_attrib_continued = [", where you shall finde OBJECT.", ", where you may find OBJECT.", ", where OBJECT shall be found.", ", where the influences of OBJECT are most strong."]

#King description bits
king_intros = ["The lorde of this realm, NAME, is ARTICLE TITLE"]
king_continue = ["with a fearsome countenance, known to drive men mad at the merest sight.", "known to beguile and mystify, drawing men in with his grotesque yet compelling visage.", "of seeming good cheer, but mistake him not, he is a fearesome being.", "who maketh all who know him quake with fear at the mere sound of his grotesque name.", "whose name fills men and beasts alike with fear, and the sound of this name, pronounced properly, is akin to a dire scream.", "whose name makes men and beast alike quake with fear.", ". He must not be trifled with or even called, or the consequences may go beyond your own life and into that of your loved ones.", ". He is a vindictive lord, and will smite with cruelty anyone who he notices."]
king_consequence_intros = ["If you anger him, ", "If you should cross or anger him, ", "If you raise his wrath ", "Be wary of attracting his attention, else, ", "Beware of his wrath, for once raised, ", "Should you incur his ire, "]
king_consequence = ["he shall destroy your very soul.", "you shall never againe sleepe, and soon you shall die.", "it shall be the end of all that you love and hold dear, and you can look forward to naught but death.", "you shall never again find joy in your life, which will be much shortened, and shall end with your complete dissolution.", "you will find yourself quickly turned into ARTICLE ANIMAL, and all human pleasure shall be lost to you, and you shall quickly die. ", "you can look forward to a short life turned into ARTICLE ANIMAL before you quickly are killed.", "you shall Die.", "it shall be your end.", "your most beloved friend shall be turned into ARTICLE ANIMAL, which you shall be made to watch, and then you shall both die."]
king_form_intros = ["When he is willing, he has been known to appear in the form of ", "If and only if it pleases him, he may appear as ", "Going about unknown in the world of men, he may take the form of ", "To observe the affairs of demons and men undetected, he may go about as ", "While the formes can not be evoked directly, at his Will he may go about as ", "His preferred disguise is as "]
king_form_endings = [". But it matters not, for you shall not see him.", ", but you shall never know in either case that it is him.", ". Whichever it may be, he remains a mortal risk to you.", ", this latter of an unnatural colour."]

#Demon description bits
consequences_intros = ["If he is not appeased, it could be that", "Do not anger him, or else", "As a consequence of incurring his wrath", "If you maketh him mad", "If you trouble him excessively", "If he is not pleased with your gift or your reason", "If this beast is in a malevolent mood", "If it is not your lucky day", "If your calculations are not properly reasoned", "If you contact him at the wrong time"]
consequences_list = ["you will be turned into ARTICLE ANIMAL", "you will be killed by ARTICLE HUMAN_DESCRIPTION HUMAN_FORM", "you will lose your Hair", "you will be bitten by ARTICLE ANIMAL", "you will fall into a lake", "you will be set upon by a mob", "you will be betrayed by a loved one", "you will be humiliated in public", "you will wet yourself", "you will soil yourself"]

he_can_intros = ["His office is to ", "When beguiled, he can ", "He can ", "When charmed he is of a good nature, and will ", "He can ", "He may ", "According to his whim he may ", "If you please him, he may ", ""]

low_rank_skills = ["inflame Men with womens Love, and women with mens love", "reconcileth friends", "come to discover things hidden or lost", "fetcheth back runaways", "make you Eloquent and win arguments"]
mid_rank_skills = ["giveth honour and dignity to any", "teach all Languages or Tongues presently", "destroy Dignities", "changeth the places of the dead", "cause the Spirits under him to gather together upon their Sepulchres", "giveth riches to a man"]
high_rank_skills = ["telleth of all things past and present", "sheweth ye the meaning of all questions you can ask", "cause Earthquakes", "giveth true answers to your Demands", "turn all mettals into Gold"]

low_rank_intros = ["He is a RANK of this realm, humbly serving his king KING_NAME.", "He is a mere and lowly RANK of this realm, barely noticed by his king KING_NAME and thereby more able to serve you.", "He is a humble RANK of the REALM and capable of lesser cantrips.", "He is a humble RANK.", "He is a lowly RANK.", "He is a RANK.", "He is a RANK in this realm.", "He is a lesser RANK.", "He is a lesser RANK in this realm."]
mid_rank_intros = ["He is a RANK and a Marshal of lesser spirits.", "He is a RANK and a middling leader in this realm.", "He is a RANK.", "He is a RANK in the army of KING_NAME.", "He is a RANK in this realm."]
high_rank_intros = ["He is a mighty RANK of this realm, leading the other spirits here.", "He is a powerful RANK.", "He is a great RANK of this realm.", "He is an immense and powerful RANK.", "He is a great imposing RANK of this realm, close in power to his king KING_NAME and a frightening lord.", "He is a mighty RANK.", "He is a great RANK."]

demon_voices = ["If he speaketh to you, it shall be in a VOICE_TYPE voice.", "He speaks in a VOICE_TYPE voice.", "His voice soundeth VOICE_TYPE when you call on him.", "If he speaketh to you, it is in a VOICE_TYPE voice.", "His voice is strange and VOICE_TYPE.", "His voyce is VOICE_TYPE.", "You shall hear him speak in a VOICE_TYPE voice."]

demon_animal_form = ["When in disguise he goes about as ARTICLE ANIMAL", "He may appear first as ARTICLE ANIMAL", "He has shewn himself as ARTICLE ANIMAL", "You may see him firste as ARTICLE ANIMAL", "He disguises himself as ARTICLE ANIMAL"]
demon_spirit_form = [", and in his spirit form he may appear as ARTICLE SPIRIT_FORM.", ", and his demonic form is like to that of ARTICLE SPIRIT_FORM.", " and in the spirit realm as ARTICLE SPIRIT_FORM.", " and he shows himself to initiates as ARTICLE SPIRIT_FORM."]

demon_human_form = ["To walk among men or visit you in publick, he will appear as ARTICLE HUMAN_FORM.", "To go among men he appeareth as ARTICLE HUMAN_FORM.", "To walk among men he appeareth as ARTICLE HUMAN_FORM.", "He also appeareth in the form of ARTICLE HUMAN_FORM.", "He may also come to you as ARTICLE HUMAN_FORM to drive a bargain.", "He may come forth in human forme as ARTICLE HUMAN_FORM.", "He may appeare to you as ARTICLE HUMAN_FORM.", "He may appeare to you as ARTICLE HUMAN_FORM who shall beguile you.", "He can bewitch men into seeing him as ARTICLE HUMAN_FORM.", "He goes about unknown among men as ARTICLE HUMAN_FORM."]

demon_planet = ["Though an infernal spirit DEMON_NAME is subject to Heavenly influences. The Planet influencing his actions is PLANET_NAME.", "Under the influence of Celestial bodies, you may find him easier to contact when PLANET_NAME is in Ascendency.", "His Planetary influence is PLANET_NAME.", "DEMON_NAME's Planetary influence is under PLANET_NAME."]

# Used in ritual generation
dance_ritual_intros = ["To gaine the attention of DEMON_NAME, you will need to Acte out the following motions.", "This demon is most pleased by deliberate motions, and this is how he is conjured.", "DEMON_NAME is a being of Chaos, and will be most pleased with you if you shew a Dance for him.", "Go through the following physical motions to conjure this DEMON_RANK DEMON_NAME."]

dance_ritual_verbs = ["wave", "wiggle", "gyrate", "push out", "focus upon", "swirl", "shake"]
dance_ritual_parts = ["left hand", "right hand", "left fist", "right fist", "hands", "fists", "finger of POSS_PRONOUN left hand", "finger of POSS_PRONOUN right hand", "left foot", "right foot", "head", "right arm", "left arm", "right leg", "left leg"]
dance_ritual_first_steps = ["First, VERB POSS_PRONOUN PART, for by this means you shall attract the Demon's attention.", "The first step is to VERB POSS_PRONOUN PART, which shall attract the Demon's attention.", "The first step is to attract the demon's attention. To do so, SECOND_PRONOUN must VERB POSS_PRONOUN PART."]
dance_ritual_second_steps = ["When this is done, the next thing is to VERB_ONE POSS_PRONOUN PART_ONE while you  VERB_TWO POSS_PRONOUN PART_TWO."]
dance_ritual_final_steps = ["Continue this last thing until your brow is beaded with sweat, and then lastly VERB POSS_PRONOUN PART in climax, while you chant \"MAGIC_WORD, MAGIC_WORD\".", "Keep doing this until you reach a frenzy, and finally VERB POSS_PRONOUN PART while you chant \"MAGIC_WORD, MAGIC_WORD\"."]


circle_ritual_intros = ["This demon is most taken with signs and sigils, and will require geomantic encouragement before he will shew himself to you.", "DEMON_NAME is known to be bound by sigils, and to conjure him you will need to prepare your Chalke.", "DEMON_NAME is a creature of infernal Rules and will obey you presently if you Chalk the correct figures.", "This DEMON_RANK is Mystified by arcane chalkings and may obey you if you practice the following.", "His conjuration relies upon the correct figures, and this is how they are Chalked.", "To summon the DEMON_RANK DEMON_NAME, you will need to carefully construct the following figures.", "To summon DEMON_NAME thou must mark the following signs on the Floor.", "To raise his spirit you will need to Chalk the following.", "Gaining his attention relies on chalking and invoking the following."]
circle_ritual_first_steps = ["First, clean and sweep a Roome, as high as possible in the house and as far away from other people.", "First you must prepare a space. Choose a quiet and secluded room in a Family house.", "You will need a warm and closed room, without windows of any kind, to perform his Rite."]
circle_ritual_second_steps = ["With the room prepared, take a COLOUR chalk or Pencile and enscribe a circle of SIZE feet upon the floor.", "Take now a COLOUR chalk and draw a circle of SIZE feet upon the floor.", "This found, take thee a COLOUR chalk or other staine and draw a circle of exactly SIZE feet upon the floor.", "Next is to take a COLOUR chalk and draw a circle of SIZE feet upon the floor.", "Next, for the required Circle, take a COLOUR chalk and inscribe one of SIZE feet."]
circle_ritual_final_steps = ["All this done, around the perimeter of the Circle, write the following words respectively at the points North, South, East and West: <strong>WORD_ONE, WORD_TWO, WORD_THREE, WORD_FOUR</strong>."]


altar_types = ["a wooden altar", "altar of wood", "steel altar", "altar of steel", "bone altar", "altar of bone", "any altar you can find", "an altar taken from a church or cathedral", "an altar you have made yourself from driftwood", "a church altar", "a driftwood altar", "an altar", "a rough altar", "a sort of altar", "something like an altar", "an altar of any sorte"]
sacrifice_places = ["dark room", "dark and forlorn woods", "building that has been Abandoned", "Church fallen out of use", "abandoned house", "lonely house", "quiet basement", "cellar", "disused cellar", "room Sealed from within"]
sacrifice_animals = ["lamb", "goat", "cat", "mouse", "dog", "pig", "cow", "deer", "monkey"]
sacrifice_tools = ["iron sword", "hammer", "razor", "shard of mirror", "blunt tool", "stone", "candlestick holder", "pipe", "plank"]
sacrifice_ritual_intros = ["As DEMON_NAME is a powerful DEMON_RANK in the army of KING_TITLE KING_NAME, you will need to make a sacrifice in order to evoke him.", "DEMON_NAME is a powerful DEMON_RANK in KING_TITLE KING_NAME's army, and demands a sacrificial ritual before he will shew himself.", "To conjure or confer with DEMON_NAME, you will need to carry out a sacrificial ritual.", "Before DEMON_NAME will Shew himself to you, you must peform the following sacrifice.", "DEMON_NAME will not show himself or listen to you, until you have appeased him with the following Sacrifice."]
sacrifice_animal_intros = ["Obtain ARTICLE ANIMAL.", "First get thee ARTICLE ANIMAL.", "First get a fine ANIMAL, the best you can find.", "You will first need to get thyself ARTICLE ANIMAL, for it is this that you shall sacrifice."]
sacrifice_ritual_first_steps = ["You shall need to find the right place. This sacrifice must be conducted in ARTICLE SACRIFICE_PLACE.", "You will need to carry out this rite in ARTICLE SACRIFICE_PLACE.", "This ritual must be performed in ARTICLE SACRIFICE_PLACE.", "You will suffer the most dire consequences if this ritual is not performed in ARTICLE SACRIFICE_PLACE.", "If you do not perform this rite in ARTICLE SACRIFICE_PLACE the most dire consequences shall come back to you."]
sacrifice_ritual_second_steps = ["In this place, you must now prepare ALTAR_TYPE, and do so solemnly.", "Next, in this place you must prepare ALTAR_TYPE. You may feel fear while you do so, but to appease DEMON_NAME you must do it while showing good cheer.", "Now in this place prepare ALTAR_TYPE. You must keep it clean.", "Next keeping thy mind focused upon thy task, prepare ALTAR_TYPE in the place you have chosen.", "Now will you need to prepare ALTAR_TYPE there.", "Next prepare there ALTAR_TYPE."]
sacrifice_ritual_third_steps = ["At last, setting the bound and restrained ANIMAL upon thy altar, take ARTICLE TOOL in thy hand.", "Next set the ANIMAL upon the altar, restrained as necessary, then brace thyself and take up ARTICLE TOOL.", "Next place the well-bound ANIMAL upon the altar and taketh ARTICLE TOOL.", "Next take ARTICLE TOOL and set the ANIMAL upon thy altar, taking care that it is well bound."]
sacrifice_ritual_songs = ["Before you commit the final deed, focus thy mind upon the word of power: MAGIC_WORD.", "As you steel thyself for the deed, first imagine, then begin to chant aloud the magic word \"MAGIC_WORD, MAGIC_WORD\".", "Next as you prepare to slay the beast, chant louder and louder \"MAGIC_WORD, MAGIC_WORD\"."]
sacrifice_ritual_climax = ["As you enter a properly Magickal state, at last slay the ANIMAL with thy TOOL.", "At last, slay the ANIMAL with thy TOOL and let its blood flow over the altar.", "At last slay the ANIMAL with thy TOOL and let its blood runneth into a Cup.", "You know what must be done next. When it is done, thou art ready to consult the great DEMON_RANK DEMON_NAME.", "Kill now the ANIMAL with thy TOOL and in this last act of violence you shall have appeased the great DEMON_RANK DEMON_NAME.", "And the last Acte in pleasing the great DEMON_NAME is to kill the ANIMAL with thy TOOL."]

def archaic(word):
    #don't mess with capitals if the whole word is upper
    if not word.isupper():
        roll = random.randint(0,99)
    # One-in-five chance of an initial capital
        if roll < 20:
            word = word.capitalize()
    # One-in-ten chance of a terminal addition, subject to suitability
    roll = random.randint(0,99)

    if roll < 20 and not word[-1] in unmoddable_letters and not word[-2:] == "ed":
        if  word[-1] == "l":
            flip = random.randint(0,1)
            if flip > 0:
                word = word + "l"
            else:
                word = word + "le"
        elif word[-1] == "s" and not word[-2:] == "es":
            word = word[:-1]
            flip = random.randint(0,1)
            if flip > 0 or word[-2] == "r":
                word = word + "es"
            else:
                word = word + "eth"
        else:
            if word[-1] == "g":
                word = word + "ge"
            else:
                if not word[-2:] == "er":
                    word = word + "e"

    if word[-2:] == "ed":
        flip = random.randint(0,1)
        if flip > 0:
            word = word[:-2] + "`d"
    if word[-2:] == "es":
        word = word[:-2] + "eth"
    return word

def article(word):
    if word[0].lower() in vowels:
        article = "an"
    else:
        article = "a"
    return article

def ordinal(number):
    last_digit = number % 10
    if last_digit == 1:
        if not number == 11:
            new_number = str(number) + "st"
    elif last_digit == 2:
        if not number == 12:
            new_number = str(number) + "nd"
    elif last_digit == 3:
        if not number == 13:
            new_number = str(number) + "rd"
    else:
        new_number = str(number) + "th"
    if number == 11 or number == 12 or number == 13:
        new_number = str(number) + "th"
    return new_number
