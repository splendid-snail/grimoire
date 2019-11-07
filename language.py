import random

# USED IN DEMON/KING GEN
animals = ["aardvark","alligator","antelope","ape","armadillo","baboon","badger","bat","bear","beaver","bison","boar","bull","camel","canary","capybara","cat","chameleon","cheetah","chimpanzee","chinchilla","chipmunk","cougar","cow","coyote","crocodile","crow","deer","dingo","dog","donkey","dromedary","elephant","elk","ewe","ferret","finch","fish","fox","frog","gazelle","gilamonster","giraffe","gnu","goat","gopher","gorilla","grizzlybear","groundhog","guineapig","hamster","hedgehog","hippopotamus","hog","horse","hyena","ibex","iguana","impala","jackal","jaguar","kangaroo","koala","lamb","lemur","leopard","lion","lizard","llama","lynx","mandrill","marmoset","mink","mole","mongoose","monkey","moose","mouse","mule","newt","ocelot","opossum","orangutan","oryx","otter","ox","panda","panther","parakeet","parrot","pig","platypus","polarbear","porcupine","porpoise","puma","rabbit","raccoon","ram","rat","reindeer","reptile","rhinoceros","salamander","seal","sheep","shrew","silverfox","skunk","sloth","snake","squirrel","tapir","tiger","toad","turtle","walrus","warthog","weasel","whale","wildcat","wolf","wolverine","zebra"]
human_forms = ["nun", "prior", "abbot", "merchant", "monsignor", "clerk"]
human_descriptions = ["able","abnormal","absent-minded","adventurous","affectionate","agile","agreeable","amazing","ambitious","amiable","amusing","analytical","angelic","apathetic","apprehensive","ardent","artificial","artistic","assertive","attentive","average","awful","balanced","beautiful","beneficent","blue","blunt","boisterous","brave","bright","brilliant","buff","callous","candid","cantankerous","capable","careful","careless","caustic","cautious","charming","childish","childlike","cheerful","churlish","circumspect","civil","clean","clever","clumsy","coherent","cold","competent","composed","conceited","condescending","confident","confused","conscientious","considerate","content","cool","cooperative","cordial","courageous","cowardly","crafty","crass","critical","cruel","curious","cynical","dainty","decisive","deep","deferential","deft","delicate","delightful","demure","depressed","devoted","dextrous","diligent","direct","dirty","disagreeable","discerning","discreet","disruptive","distant","distraught","distrustful","dowdy","dramatic","dreary","drowsy","drugged","drunk","dull","dutiful","eager","earnest","easy-going","efficient","egotistical","elfin","emotional","energetic","enterprising","enthusiastic","evasive","even-tempered","exacting","excellent","excitable","experienced","fabulous","fastidious","ferocious","fervent","fiery","flabby","flaky","flashy","frank","friendly","funny","fussy","generous","gentle","gloomy","glutinous","good","grave","great","groggy","guarded","hateful","hearty","helpful","hesitant","hot-headed","hysterical","idiotic","idle","imaginative","immature","immodest","impatient","imperturbable","impetuous","impractical","impressionable","impressive","impulsive","inactive","incisive","incompetent","inconsiderate","inconsistent","indiscreet","indolent","industrious","inexperienced","insensitive","inspiring","intelligent","interesting","intolerant","inventive","irascible","irritable","irritating","jocular","jovial","joyous","judgmental","keen","kind","lame","lazy","lean","leery","lethargic","listless","lithe","lively","local","logickal","long-winded","lovable","love-lorn","lovely","maternal","mature","mean","meddlesome","mercurial","methodical","meticulous","mild","miserable","modest","moronic","morose","musical","naive","nasty","natural","naughty","negative","nervous","noisy","normal","nosy","numb","obliging","obnoxious","old-fashioned","orderly","ostentatious","outgoing","outspoken","passionate","passive","patient","peaceful","peevish","pensive","persevering","petulant","picky","plain","plain-speaking","playful","pleasant","plucky","polite","popular","positive","powerful","practical","prejudiced","pretty","proficient","proud","provocative","prudent","punctual","quarrelsome","querulous","quick","quick-tempered","quiet","reassuring","reclusive","reliable","reluctant","resentful","reserved","resigned","resourceful","respected","respectful","responsible","restless","revered","ridiculous","sad","saucy","sedate","selfish","sensible","sensitive","sentimental","serene","serious","sharp","short-tempered","shrewd","shy","silly","sincere","sleepy","slight","sloppy","slothful","slovenly","slow","smart","sneering","snobby","somber","sober","sophisticated","soulful","soulless","sour","spirited","spiteful","stable","staid","steady","stern","stoic","striking","strong","stupid","sturdy","subtle","sullen","sulky","supercilious","superficial","surly","suspicious","sweet","tactful","tactless","talented","testy","thinking","thoughtful","thoughtless","timid","tired","tolerant","touchy","tranquil","ugly","unaffected","unbalanced","uncertain","uncooperative","undependable","unemotional","unfriendly","unguarded","unhelpful","unimaginative","unmotivated","unpleasant","unpopular","unreliable","unstable","unsure","unthinking","unwilling","venal","versatile","vigilant","warm","warmhearted","wary","watchful","weak","well-behaved","willing","wonderful","volcanic","vulnerable","zealous"]
spirit_forms = ["angel","bugbear","centaur","chimera","cockatrice","cyclops","demon","djinn","dragon","draugr","dryad","dwarf","faun","gargoyle","genie","ghast","ghost","ghoul","giant","goblin","golem","gorgon","gremlin","griffon","hag","harpy","hippogriff","hobgoblin","homonculus","hydra","imp","incubus","kappa","kobold","kraken","lamassu","leprechaun","lich","manticore","mermaid","merman","minotaur","mummy","nix","nymph","ogre","orc","pegasus","phoenix","poltergeist","roc","satyr","selkie","siren","spectre","sphinx","sprite","succubus","sylph","warg","werewolf","wight","witch","wraith","wyvern"]
planets = ["Mercury", "Venus", "Earth", "Mars", "Saturn", "Uranus", "Neptune", "Pluto"]
voices = ["rough","beguiling","melodic","melodious","frightening","fearsome","mad","loud","oily","wheedling","reedy","pleading","desperate", "shaky", "booming"]
he_can = ["make you invisible", "grant you riches", "make you grow big or small", "offer you invisible sights", "turn your rival into (animal_form)"]
king_adj = ["mighty", "powerful", "cruel", "fearsome"]


#UTILITY IN TEXT GEN
unmoddable_letters = ["a", "e", "i", "o", "u", "c"]
vowels = ["a", "e", "i", "o", "u"]

#REALM RELATED
north_attribs = ["cold", "earth"]
east_attribs = ["air", "the intellect", "communication", "balance"]
south_attribs = ["fire", "creativity", "danger", "lively spirits"]
west_attribs = ["water", "beauty "]
upper_attribs = ["light"]
lower_attribs = ["darkness", "sins", "hidden things", "shadows", "things that crawl"]
ruled_passive = ["ruled", "governed", "overseen", "maintained", "dominated"]
ruled_active = ["rules", "governs", "oversees", "maintains", "dominates"]
realm_intros_passive = ["This realm is", "This kingdom is", "Know that this realm is"]
realm_attrib_intros = ["It is the realm of ", "Here in this realm is ", "Here you shall find "]

def archaic(word):
    #don't mess with capitals if the whole word is upper
    if not word.isupper():
        roll = random.randint(0,99)
    # One-in-five chance of an initial capital
        if roll < 20:
            word = word.capitalize()
    # One-in-ten chance of a terminal addition, subject to suitability
    roll = random.randint(0,99)

    if roll < 20 and not word[-1] in unmoddable_letters and not (word[-2:] == "ed"):
        if  word[-1] == "l":
            flip = random.randint(0,1)
            if flip > 0:
                word = word + "l"
            else:
                word = word + "le"
        elif word[-1] == "s":
            if not word[-2] in vowels:
                word = word + "es"
        else:
            word = word + "e"

    if word[-2:] == "ed":
        flip = random.randint(0,1)
        if flip > 0:
            word = word[:-2] + "`d"
    return word

def article(word):
    if word[0] in vowels:
        article = "an"
    else:
        article = "a"
    return article
