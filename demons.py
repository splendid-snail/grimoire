import name
import random

#Lists used in demon generation
animals = ["aardvark","alligator","antelope","ape","armadillo","baboon","badger","bat","bear","beaver","bison","boar","bull","camel","canary","capybara","cat","chameleon","cheetah","chimpanzee","chinchilla","chipmunk","cougar","cow","coyote","crocodile","crow","deer","dingo","dog","donkey","dromedary","elephant","elk","ewe","ferret","finch","fish","fox","frog","gazelle","gilamonster","giraffe","gnu","goat","gopher","gorilla","grizzlybear","groundhog","guineapig","hamster","hedgehog","hippopotamus","hog","horse","hyena","ibex","iguana","impala","jackal","jaguar","kangaroo","koala","lamb","lemur","leopard","lion","lizard","llama","lynx","mandrill","marmoset","mink","mole","mongoose","monkey","moose","mouse","mule","newt","ocelot","opossum","orangutan","oryx","otter","ox","panda","panther","parakeet","parrot","pig","platypus","polarbear","porcupine","porpoise","puma","rabbit","raccoon","ram","rat","reindeer","reptile","rhinoceros","salamander","seal","sheep","shrew","silverfox","skunk","sloth","snake","squirrel","tapir","tiger","toad","turtle","walrus","warthog","weasel","whale","wildcat","wolf","wolverine","zebra"]

human_forms = ["nun", "prior", "abbot", "merchant", "monsignor", "clerk"]

human_descriptions = ["able","abnormal","absent-minded","adventurous","affectionate","agile","agreeable","amazing","ambitious","amiable","amusing","analytical","angelic","apathetic","apprehensive","ardent","artificial","artistic","assertive","attentive","average","awful","balanced","beautiful","beneficent","blue","blunt","boisterous","brave","bright","brilliant","buff","callous","candid","cantankerous","capable","careful","careless","caustic","cautious","charming","childish","childlike","cheerful","churlish","circumspect","civil","clean","clever","clumsy","coherent","cold","competent","composed","conceited","condescending","confident","confused","conscientious","considerate","content","cool","cooperative","cordial","courageous","cowardly","crafty","crass","critical","cruel","curious","cynical","dainty","decisive","deep","deferential","deft","delicate","delightful","demure","depressed","devoted","dextrous","diligent","direct","dirty","disagreeable","discerning","discreet","disruptive","distant","distraught","distrustful","dowdy","dramatic","dreary","drowsy","drugged","drunk","dull","dutiful","eager","earnest","easy-going","efficient","egotistical","elfin","emotional","energetic","enterprising","enthusiastic","evasive","even-tempered","exacting","excellent","excitable","experienced","fabulous","fastidious","ferocious","fervent","fiery","flabby","flaky","flashy","frank","friendly","funny","fussy","generous","gentle","gloomy","glutinous","good","grave","great","groggy","guarded","hateful","hearty","helpful","hesitant","hot-headed","hysterical","idiotic","idle","imaginative","immature","immodest","impatient","imperturbable","impetuous","impractical","impressionable","impressive","impulsive","inactive","incisive","incompetent","inconsiderate","inconsistent","indiscreet","indolent","industrious","inexperienced","insensitive","inspiring","intelligent","interesting","intolerant","inventive","irascible","irritable","irritating","jocular","jovial","joyous","judgmental","keen","kind","lame","lazy","lean","leery","lethargic","listless","lithe","lively","local","logickal","long-winded","lovable","love-lorn","lovely","maternal","mature","mean","meddlesome","mercurial","methodical","meticulous","mild","miserable","modest","moronic","morose","musical","naive","nasty","natural","naughty","negative","nervous","noisy","normal","nosy","numb","obliging","obnoxious","old-fashioned","orderly","ostentatious","outgoing","outspoken","passionate","passive","patient","peaceful","peevish","pensive","persevering","petulant","picky","plain","plain-speaking","playful","pleasant","plucky","polite","popular","positive","powerful","practical","prejudiced","pretty","proficient","proud","provocative","prudent","punctual","quarrelsome","querulous","quick","quick-tempered","quiet","reassuring","reclusive","reliable","reluctant","resentful","reserved","resigned","resourceful","respected","respectful","responsible","restless","revered","ridiculous","sad","saucy","sedate","selfish","sensible","sensitive","sentimental","serene","serious","sharp","short-tempered","shrewd","shy","silly","sincere","sleepy","slight","sloppy","slothful","slovenly","slow","smart","sneering","snobby","somber","sober","sophisticated","soulful","soulless","sour","spirited","spiteful","stable","staid","steady","stern","stoic","striking","strong","stupid","sturdy","subtle","sullen","sulky","supercilious","superficial","surly","suspicious","sweet","tactful","tactless","talented","testy","thinking","thoughtful","thoughtless","timid","tired","tolerant","touchy","tranquil","ugly","unaffected","unbalanced","uncertain","uncooperative","undependable","unemotional","unfriendly","unguarded","unhelpful","unimaginative","unmotivated","unpleasant","unpopular","unreliable","unstable","unsure","unthinking","unwilling","venal","versatile","vigilant","warm","warmhearted","wary","watchful","weak","well-behaved","willing","wonderful","volcanic","vulnerable","zealous"]

spirit_forms = ["angel","bugbear","centaur","chimera","cockatrice","cyclops","demon","djinn","dragon","draugr","dryad","dwarf","faun","gargoyle","genie","ghast","ghost","ghoul","giant","goblin","golem","gorgon","gremlin","griffon","hag","harpy","hippogriff","hobgoblin","homonculus","hydra","imp","incubus","kappa","kobold","kraken","lamassu","leprechaun","lich","manticore","mermaid","merman","minotaur","mummy","nix","nymph","ogre","orc","pegasus","phoenix","poltergeist","roc","satyr","selkie","siren","spectre","sphinx","sprite","succubus","sylph","warg","werewolf","wight","witch","wraith","wyvern"]

planets = ["Mercury", "Venus", "Earth", "Mars", "Saturn", "Uranus", "Neptune", "Pluto"]

class Demon:
    def __init__(self, name, card, king):
        upper_ranks = ["Archduke", "President", "Prince", "Despot", "Duke"]
        mid_ranks = ["Marquiz", "Count", "Earl"]
        low_ranks = ["Knight", "Baronet", "Seigneur", "Viscount"]
        self.name = name
        self.card = card
        self.king = king
        self.realm = king.realm
        if card.rank == 0:
            self.rank = random.choice(low_ranks)
        elif card.rank == 1:
            self.rank = random.choice(mid_ranks)
        else:
            self.rank = random.choice(upper_ranks)
        #insert twisted sword easter egg here
        self.animal_form = random.choice(animals)
        self.human_form = random.choice(human_descriptions) + " " + random.choice(human_forms)
        self.spirit_form = random.choice(spirit_forms)
        self.lucky_number = random.randint(1,99)
        self.planet = random.choice(planets)
        """
        To add:
        * voice
        * consequences
        * skills
        * sign of presence / voice
        """



class King:
    def __init__(self, name, realm):
        titles = ["Lord", "King", "Emperor", "Basileus"]
        self.name = name
        self.title = random.choice(titles)
        self.realm = realm
        animals_set = False
        while not animals_set:
            self.animal_form_one = random.choice(animals)
            self.animal_form_two = random.choice(animals)
            if self.animal_form_one != self.animal_form_two:
                animals_set = True

def create_demons(kings_list, names_list, tarot_deck):
    """WORK IN PROGRESS"""
    demons_made = 0
    demons_list = []
    for king in kings_list:
        demons_to_make = 13
        while demons_to_make > 0:
            new_demon = Demon(name.new(names_list), tarot_deck[demons_made], king)
            demons_list.append(new_demon)
            demons_to_make -= 1
            demons_made += 1
    return demons_list

def create_kings(names_list):
    kings_made = 0
    kings_list = []
    realms = ["North", "East", "South", "West", "Upper", "Lower"]
    while kings_made < 6:
        new_king = King(name.new(names_list), realms[kings_made])
        kings_list.append(new_king)
        kings_made += 1
    return kings_list
