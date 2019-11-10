import random

# USED IN DEMON/KING GEN
animals = ["aardvark","alligator","antelope","ape","armadillo","baboon","badger","bat","bear","beaver","bison","boar","bull","camel","canary","capybara","cat","chameleon","cheetah","chimpanzee","chinchilla","chipmunk","cougar","cow","coyote","crocodile","crow","deer","dingo","dog","donkey","dromedary","elephant","elk","ewe","ferret","finch","fish","fox","frog","gazelle","gilamonster","giraffe","gnu","goat","gopher","gorilla","grizzlybear","groundhog","guineapig","hamster", "halibut", "hedgehog","hippopotamus","hog","horse","hyena","ibex","iguana","impala","jackal","jaguar","kangaroo","koala","lamb","lemur","leopard","lion","lizard","llama","lynx","mandrill","marmoset","mink","mole","mongoose","monkey","moose","mouse","mule","newt","ocelot","opossum","orangutan","oryx","otter","ox","panda","panther","parakeet","parrot","pig","platypus","polar Bear","porcupine","porpoise","puma","rabbit","raccoon","ram","rat","reindeer","reptile","rhinoceros","salamander","seal","sheep","shrew","silverfish","skunk","sloth","snake","squirrel","tapir","tiger","toad","turtle","walrus","warthog","weasel","whale","wildcat","wolf","wolverine","zebra"]
human_forms = ["nun", "prior", "abbot", "merchant", "monsignor", "clerk"]
human_descriptions = ["able","abnormal","absent-minded","adventurous","affectionate","agile","agreeable","amazing","ambitious","amiable","amusing","analytical","angelic","apathetic","apprehensive","ardent","artificial","artistic","assertive","attentive","average","awful","balanced","beautiful","beneficent","blue","blunt","boisterous","brave","bright","brilliant","buff","callous","candid","cantankerous","capable","careful","careless","caustic","cautious","charming","childish","childlike","cheerful","churlish","circumspect","civil","clean","clever","clumsy","coherent","cold","competent","composed","conceited","condescending","confident","confused","conscientious","considerate","content","cool","cooperative","cordial","courageous","cowardly","crafty","crass","critical","cruel","curious","cynical","dainty","decisive","deep","deferential","deft","delicate","delightful","demure","depressed","devoted","dextrous","diligent","direct","dirty","disagreeable","discerning","discreet","disruptive","distant","distraught","distrustful","dowdy","dramatic","dreary","drowsy","drugged","drunk","dull","dutiful","eager","earnest","easy-going","efficient","egotistical","elfin","emotional","energetic","enterprising","enthusiastic","evasive","even-tempered","exacting","excellent","excitable","experienced","fabulous","fastidious","ferocious","fervent","fiery","flabby","flaky","flashy","frank","friendly","funny","fussy","generous","gentle","gloomy","glutinous","good","grave","great","groggy","guarded","hateful","hearty","helpful","hesitant","hot-headed","hysterical","idiotic","idle","imaginative","immature","immodest","impatient","imperturbable","impetuous","impractical","impressionable","impressive","impulsive","inactive","incisive","incompetent","inconsiderate","inconsistent","indiscreet","indolent","industrious","inexperienced","insensitive","inspiring","intelligent","interesting","intolerant","inventive","irascible","irritable","irritating","jocular","jovial","joyous","judgmental","keen","kind","lame","lazy","lean","leery","lethargic","listless","lithe","lively","local","logickal","long-winded","lovable","love-lorn","lovely","maternal","mature","mean","meddlesome","mercurial","methodical","meticulous","mild","miserable","modest","moronic","morose","musical","naive","nasty","natural","naughty","negative","nervous","noisy","normal","nosy","numb","obliging","obnoxious","old-fashioned","orderly","ostentatious","outgoing","outspoken","passionate","passive","patient","peaceful","peevish","pensive","persevering","petulant","picky","plain","plain-speaking","playful","pleasant","plucky","polite","popular","positive","powerful","practical","prejudiced","pretty","proficient","proud","provocative","prudent","punctual","quarrelsome","querulous","quick","quick-tempered","quiet","reassuring","reclusive","reliable","reluctant","resentful","reserved","resigned","resourceful","respected","respectful","responsible","restless","revered","ridiculous","sad","saucy","sedate","selfish","sensible","sensitive","sentimental","serene","serious","sharp","short-tempered","shrewd","shy","silly","sincere","sleepy","slight","sloppy","slothful","slovenly","slow","smart","sneering","snobby","somber","sober","sophisticated","soulful","soulless","sour","spirited","spiteful","stable","staid","steady","stern","stoic","striking","strong","stupid","sturdy","subtle","sullen","sulky","supercilious","superficial","surly","suspicious","sweet","tactful","tactless","talented","testy","thinking","thoughtful","thoughtless","timid","tired","tolerant","touchy","tranquil","ugly","unaffected","unbalanced","uncertain","uncooperative","undependable","unemotional","unfriendly","unguarded","unhelpful","unimaginative","unmotivated","unpleasant","unpopular","unreliable","unstable","unsure","unthinking","unwilling","venal","versatile","vigilant","warm","warmhearted","wary","watchful","weak","well-behaved","willing","wonderful","volcanic","vulnerable","zealous"]
spirit_forms = ["angel","bugbear","centaur","chimera","cockatrice","cyclops","demon","djinn","dragon","draugr","dryad","dwarf","faun","gargoyle","genie","ghast","ghost","ghoul","giant","goblin","golem","gorgon","gremlin","griffon","hag","harpy","hippogriff","hobgoblin","homonculus","hydra","imp","incubus","kappa","kobold","kraken","lamassu","leprechaun","lich","manticore","mermaid","merman","minotaur","mummy","nix","nymph","ogre","orc","pegasus","phoenix","poltergeist","roc","satyr","selkie","siren","spectre","sphinx","sprite","succubus","sylph","warg","werewolf","wight","witch","wraith","wyvern"]
planets = ["Mercury", "Venus", "Earth", "Mars", "Saturn", "Uranus", "Neptune", "Pluto"]
voices = ["rough","beguiling","melodic","melodious","frightening","fearsome","mad","loud","oily","wheedling","reedy","pleading","desperate", "shaky", "booming"]
he_can = ["make you invisible", "grant you riches", "make you grow big or small", "offer you invisible sights", "turn your rival into (animal_form)"]
king_adj = ["mighty", "powerful", "cruel", "fearsome"]
trinkets = ["candle", "holy book", "whistle", "thorny twig", "mirror", "polished stone", "rough stone", "small bell", "great bell", "plate of food", "cup of ale", "bloody cloth", "torn rag", "painting fragment", "parchment of a prayer", "priest's collar", "sweet-smelling cloth", "old cloak", "nun's habit", "pie dish", "empty cup", "cracked mirror", "trumpet", "bugle", "lyre", "reed", "dried frog", "lifeless mouse", "old key", "small piece of chain"]

#UTILITY IN TEXT GEN
unmoddable_letters = ["a", "e", "i", "o", "u", "c"]
vowels = ["a", "e", "i", "o", "u"]

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
king_continue = ["with a fearsome countenance, known to drive men mad at the merest sight.", "known to beguile and mystify, drawing men in with a grotesque but compelling visage.", "of seeming good cheer, but mistake him not, he is a fearesome being.", "who maketh all who know him quake with fear at the mere sound of his grotesque name.", "whose name fills men and beasts alike with fear, and the sound of this name, pronounced properly, is akin to a dire scream.", "whose name makes men and beast alike quake with fear.", ". He must not be trifled with or even called, or the consequences may go beyond your own life and into that of your loved ones.", ". He is a vindictive lord, and will smite with cruelty anyone who he notices."]
king_consequence_intros = ["If you anger him, ", "If you should cross or anger him, ", "If you raise his wrath ", "Be wary of attracting his attention, else, ", "Beware of his wrath, for once raised, ", "Should you incur his ire, "]
king_consequence = ["he shall destroy your very soul.", "you shall never againe sleepe, and soon you shall die.", "it shall be the end of all that you love and hold dear, and you can look forward to naught but death.", "you shall never again find joy in your life, which will be much shortened, and shall end with your complete dissolution.", "you will find yourself quickly turned into ARTICLE ANIMAL, and all human pleasure shall be lost to you, and you shall quickly die. ", "you can look forward to a short life turned into ARTICLE ANIMAL before you quickly are killed.", "you shall Die.", "it shall be your end.", "your most beloved friend shall be turned into ARTICLE ANIMAL, which you shall be made to watch, and then you shall both die."]
king_form_intros = ["When he is willing, he has been known to appear in the form of ", "If and only if it pleases him, he may appear as ", "Going about unknown in the world of men, he may take the form of ", "To observe the affairs of demons and men undetected, he may go about as ", "While the formes can not be evoked directly, at his Will he may go about as ", "His preferred disguise is as "]
king_form_endings = [". But it matters not, for you shall not see him.", ", but you shall never know in either case that it is him.", ". Whichever it may be, he remains a mortal risk to you.", ", this latter of an unnatural colour."]

#Demon description bits
consequences_intros = ["If he is not appeased, it could be that", "Do not anger him, or else", "As a consequence of incurring his wrath", "If you maketh him mad", "If you trouble him excessively", "If he is not pleased with your gift or your reason", "If this beast is in a malevolent mood", "If it is not your lucky day", "If your calculations are not properly reasoned", "If you contact him at the wrong time"]
consequences_list = ["you will be turned into ARTICLE ANIMAL", "you will be killed by ARTICLE HUMAN_DESCRIPTION HUMAN_FORM", "you will lose your Hair", "you will be bitten by ARTICLE ANIMAL", "you will fall into a lake", "you will be set upon by a mob", "you will be betrayed by a loved one", "you will be humiliated in public", "you will wet yourself", "you will soil yourself"]

low_rank_intros = ["He is a RANK of this realm, humbly serving his king KING_NAME.", "He is a mere and lowly RANK of this realm, barely noticed by his king KING_NAME and thereby more able to serve you.", "He is a humble RANK of the REALM and capable of lesser cantrips.", "He is a humble RANK.", "He is a lowly RANK.", "He is a RANK.", "He is a RANK in this realm.", "He is a lesser RANK.", "He is a lesser RANK in this realm."]
mid_rank_intros = ["He is a RANK and a Marshal of lesser spirits.", "He is a RANK and a middling leader in this realm.", "He is a RANK.", "He is a RANK in the army of KING_NAME.", "He is a RANK in this realm."]
high_rank_intros = ["He is a mighty RANK of this realm, leading the other spirits here.", "He is a powerful RANK.", "He is a great RANK of this realm.", "He is an immense and powerful RANK.", "He is a great imposing RANK of this realm, close in power to his king KING_NAME and a frightening lord.", "He is a mighty RANK.", "He is a great RANK."]

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
        elif word[-1] == "s":
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
                word = word + "e"

    if word[-2:] == "ed":
        flip = random.randint(0,1)
        if flip > 0:
            word = word[:-2] + "`d"
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
