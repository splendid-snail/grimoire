import random

# USED IN DEMON/KING GEN
animals = ["aardvark","alligator","antelope","ape","armadillo","baboon","badger","bat","bear","beaver","bison","boar","bull","camel","canary","capybara","cat","chameleon","cheetah","chimpanzee","chinchilla","chipmunk","cougar","cow","coyote","crocodile","crow","cockerel","deer","dog","donkey","dromedary","elephant","elk","ewe","ferret","finch","fish","fox","frog","gazelle","giraffe","gnu","goat","gopher","gorilla","grizzlybear","groundhog","guineapig","hamster", "halibut", "hedgehog","hippopotamus","hog","horse","hyena","ibex","iguana","impala","jackal","jaguar","kangaroo","lamb","lemur","leopard","lion","lizard","lynx","mandrill","marmoset","mink","mole","mongoose","monkey","moose","mouse","mule","newt","ocelot","opossum","orangutan","oryx","otter","ox","panda","panther","parakeet","parrot","pig","platypus","polar Bear","porcupine","porpoise","puma","rabbit","raccoon","ram","rat","reindeer","reptile","rhinoceros","salamander","seal","sheep","shrew","silverfish","skunk","sloth","snake","squirrel","tapir","tiger","toad","turtle","walrus","warthog","weasel","whale","wildcat","wolf","wolverine","zebra"]
human_forms = ["nun", "prior", "abbot", "merchant", "monsignor", "clerk", "carpenter", "mason", "chef", "cook", "servant", "judge", "washerwoman", "fishmonger", "cooper", "fletcher", "peasant", "mayor", "jester", "clown", "maid", "clerk", "wainwright", "cooper", "farmer", "steeplejack", "baker", "chorister", "villein", "bailiff", "sherriff", "cottager", "yeoman", "barber", "chandler", "chaplain", "gardener", "herald", "harker", "minstrel"]
human_descriptions = ["able","abnormal","absent-minded","adventurous","affectionate","agile","agreeable","amazing","ambitious","amiable","amusing","analytical","angelic","apathetic","apprehensive","ardent","artificial","artistic","assertive","attentive","average","awful","balanced","beautiful","beneficent","blue","blunt","boisterous","brave","bright","brilliant","buff","callous","candid","cantankerous","capable","careful","careless","caustic","cautious","charming","childish","childlike","cheerful","churlish","circumspect","civil","clean","clever","clumsy","coherent","cold","competent","composed","conceited","condescending","confident","confused","conscientious","considerate","content","cool","cooperative","cordial","courageous","cowardly","crafty","crass","critical","cruel","curious","cynical","dainty","decisive","deep","deferential","deft","delicate","delightful","demure","depressed","devoted","dextrous","diligent","direct","dirty","disagreeable","discerning","discreet","disruptive","distant","distraught","distrustful","dowdy","dramatic","dreary","drowsy","drugged","drunk","dull","dutiful","eager","earnest","easy-going","efficient","egotistical","elfin","emotional","energetic","enterprising","enthusiastic","evasive","even-tempered","exacting","excellent","excitable","experienced","fabulous","fastidious","ferocious","fervent","fiery","flabby","flaky","flashy","frank","friendly","funny","fussy","generous","gentle","gloomy","glutinous","good","grave","great","groggy","guarded","hateful","hearty","helpful","hesitant","hot-headed","hysterical","idiotic","idle","imaginative","immature","immodest","impatient","imperturbable","impetuous","impractical","impressionable","impressive","impulsive","inactive","incisive","incompetent","inconsiderate","inconsistent","indiscreet","indolent","industrious","inexperienced","insensitive","inspiring","intelligent","interesting","intolerant","inventive","irascible","irritable","irritating","jocular","jovial","joyous","judgmental","keen","kind","lame","lazy","lean","leery","lethargic","listless","lithe","lively","local","logickal","long-winded","lovable","love-lorn","lovely","maternal","mature","mean","meddlesome","mercurial","methodical","meticulous","mild","miserable","modest","moronic","morose","musical","naive","nasty","natural","naughty","negative","nervous","noisy","normal","nosy","numb","obliging","obnoxious","old-fashioned","orderly","ostentatious","outgoing","outspoken","passionate","passive","patient","peaceful","peevish","pensive","persevering","petulant","picky","plain","plain-speaking","playful","pleasant","plucky","polite","popular","positive","powerful","practical","prejudiced","pretty","proficient","proud","provocative","prudent","punctual","quarrelsome","querulous","quick","quick-tempered","quiet","reassuring","reclusive","reliable","reluctant","resentful","reserved","resigned","resourceful","respected","respectful","responsible","restless","revered","ridiculous","sad","saucy","sedate","selfish","sensible","sensitive","sentimental","serene","serious","sharp","short-tempered","shrewd","shy","silly","sincere","sleepy","slight","sloppy","slothful","slovenly","slow","smart","sneering","snobby","somber","sober","sophisticated","soulful","soulless","sour","spirited","spiteful","stable","staid","steady","stern","stoic","striking","strong","stupid","sturdy","subtle","sullen","sulky","supercilious","superficial","surly","suspicious","sweet","tactful","tactless","talented","testy","thinking","thoughtful","thoughtless","timid","tired","tolerant","touchy","tranquil","ugly","unaffected","unbalanced","uncertain","uncooperative","undependable","unemotional","unfriendly","unguarded","unhelpful","unimaginative","unmotivated","unpleasant","unpopular","unreliable","unstable","unsure","unthinking","unwilling","venal","versatile","vigilant","warm","warmhearted","wary","watchful","weak","well-behaved","willing","wonderful","volcanic","vulnerable","zealous"]
spirit_forms = ["angel","flame", "fire", "flaming fire","centaur","chimera","cockatrice","cyclops","djinn","dragon","dryad","dwarf","faun","gargoyle","ghast","ghost","ghoul","giant","goblin","golem","gorgon","gremlin","griffon","hag","harpy","hippogriff","hobgoblin","homonculus","hydra","imp","incubus","kappa","kobold","kraken","lamassu","leprechaun","lich","manticore","mermaid","merman","minotaur","mummy","nix","nymph","ogre","orc","pegasus","phoenix","poltergeist","roc","satyr","selkie","siren","spectre","sphinx","sprite","succubus","sylph","warg","werewolf","wight","wraith","wyvern"]
planets = ["Mercury", "Venus", "Earth", "Mars", "Saturn", "Uranus", "Neptune"]
voices = ["rough","beguiling","melodic","melodious","frightening","fearsome","mad","loud","oily","wheedling","reedy","pleading","desperate", "shaky", "booming"]
king_adj = ["mighty", "powerful", "cruel", "fearsome"]
trinkets = ["candle", "holy book", "tin whistle", "thorny twig", "mirror", "polished stone", "rough stone", "small bell", "great bell", "plate of food", "cup of ale", "bloody cloth", "torn rag", "painting fragment", "parchment of a prayer", "priest's collar", "sweet-smelling cloth", "old cloak", "nun's habit", "pie dish", "dead cat", "empty cup", "cracked mirror", "trumpet", "bugle", "lyre", "reed", "dried frog", "lifeless mouse", "old key", "small piece of chain"]

upper_ranks = ["Archduke", "President", "Prince", "Despot", "Duke"]
mid_ranks = ["Marquiz", "Count", "Earl"]
low_ranks = ["Knight", "Baronet", "Seigneur", "Viscount"]
king_titles = ["Lord", "King", "Emperor", "Basileus"]



#UTILITY IN TEXT GEN
unmoddable_letters = ["a", "e", "i", "o", "u", "c"]
vowels = ["a", "e", "i", "o", "u"]
second_person_pronouns = ["you", "thou"]
second_person_poss_pronouns = ["your", "thy"]
colours = ["red", "green", "blue", "yellow", "black", "white"]
true_adj = ["truthful", "truthy", "right", "correct", "appropriate"]
false_adj = ["false", "falsy", "wrong", "incorrect"]
positive_adj = ["good", "great", "true", "lovely", "strong", "fair", "cunning", "woundrous", "witty"]
negative_adj = ["bad", "awful", "weak", "false", "ugly", "unfair", "silly", "conceited", "rotten"]
compass_points = ["north", "east", "south", "west", "centre"]
strengths = ["powerful", "wise", "strong", "clever", "able", "capable", "learned"]


#INTRO related
general_intro = ["This book will show you the TRUE_ADJ and TRUE_ADJ means of conjuring spirits POS_ADJ and NEG_ADJ_1, although it must be said that most of them indeed are NEG_ADJ_1 and great care must be taken in contacting and summoning them. Indeed, before you would do such a thing, it is important that you read and mark well the POS_ADJ instructions in this booke, for only in following them to the Letter shall you avoid the FALSE_ADJ and the risk of CONSEQUENCE."]

intro_consequences = ["utter dissolution by Demonic forces", "your absolute destruction at the talons of spirits Vicious.", "being destroyed utterly by forces beyond your comprehension."]


#REALM RELATED
north_attribs = ["cold things", "earth", "snow",]
east_attribs = ["air", "clouds", "things of the intellect", "communication", "balance", "mists"]
south_attribs = ["fire", "creativity", "danger", "lively spirits","flames", "thrills"]
west_attribs = ["water", "beauty", "waves", "mysterious ripplings", "froth", "bubble"]
upper_attribs = ["light", "beams", "rays", "shafts", "feathers"]
lower_attribs = ["darkness", "sins", "hidden things", "shadows", "things that crawl", "clods", "roots", "bones"]

ruled_passive = ["ruled", "governed", "overseen", "maintained", "dominated"]
ruled_active = ["rules", "governs", "oversees", "maintains", "dominates"]
realm_intros_passive = ["This realm is", "This kingdom is", "Know that this realm is"]
realm_attrib_intros = ["It is the realm of ", "Here in this realm is ", "This is a realm with attributes of ", "Here are ", "This is the traditional home of ", "It has longe been known to the learned as the realm of ", "In this realm`s Pleroma are the spirits of ", "Among the strongest influences here are "]
realm_attrib_continued = [", which is the domain of OBJECT.", " and also OBJECT.", ", where you shall fine also OBJECT.", ", where the influences of OBJECT are most strong."]

#King description bits
king_intros = ["The lorde of this realm, NAME, is ARTICLE TITLE"]
king_continue = ["with a fearsome countenance, known to drive men mad at the merest sight.", "known to beguile and mystify, drawing men in with his grotesque yet compelling visage.", "of seeming good cheer, but mistake him not, he is a fearesome being.", "who maketh all who know him quake with fear at the mere sound of his grotesque name.", "whose name fills men and beasts alike with fear, and the sound of this name, pronounced properly, is akin to a dire scream.", "whose name makes men and beast alike quake with fear.", ". He must not be trifled with or even called, or the consequences may go beyond your own life and into that of your loved ones.", ". He is a vindictive lord, and will smite with cruelty anyone who he notices."]
king_consequence_intros = ["If you anger him, ", "If you should cross or anger him, ", "If you raise his wrath ", "Be wary of attracting his attention, else, ", "Beware of his wrath, for once raised, ", "Should you incur his ire, "]
king_consequence = ["he shall destroy your very soul.", "you shall never againe sleepe, and soon you shall die.", "it shall be the end of all that you love and hold dear, and you can look forward to naught but death.", "you shall never again find joy in your life, which will be much shortened, and shall end with your complete dissolution.", "you will find yourself quickly turned into ARTICLE ANIMAL, and all human pleasure shall be lost to you, and you shall quickly die. ", "you can look forward to a short life turned into ARTICLE ANIMAL before you quickly are killed.", "you shall Die.", "it shall be your end.", "your most beloved friend shall be turned into ARTICLE ANIMAL, which you shall be made to watch, and then you shall both die."]
king_form_intros = ["When he is willing, he has also been known to appear in the form of ", "If and only if it pleases him, he may also appear as ", "Going about unknown in the world of men, he may take the form of ", "To observe the affairs of demons and men undetected, he may go about as ", "While the formes can not be evoked directly, at his Will he may go about as ", "His preferred disguise is as "]
king_form_endings = [". But it matters not, for you shall not see him.", ", but you shall never know in either case that it is him.", ". Whichever it may be, he remains a mortal risk to you.", ", this latter of an unnatural colour."]

#Demon description bits
consequences_intros = ["If he is not appeased, it could be that", "Do not anger him, or else", "As a consequence of incurring his wrath", "If you maketh him mad", "If you trouble him excessively", "If he is not pleased with your gift or your reason", "If this beast is in a malevolent mood", "If it is not your lucky day", "If your calculations are not properly reasoned", "If you contact him at the wrong time"]
consequences_list = ["you will be turned into ARTICLE ANIMAL", "you will be killed by ARTICLE HUMAN_DESCRIPTION HUMAN_FORM", "you will lose your Hair", "you will be bitten by ARTICLE ANIMAL", "you will fall into a lake", "you will be set upon by a mob", "you will be betrayed by a loved one", "you will be humiliated in public", "you will wet yourself", "you will soil yourself"]

he_can_intros = ["His office is to ", "When beguiled, he can ", "He can ", "When charmed he is of a good nature, & will ", "He can ", "He may ", "According to his whim he may ", "If you please him, he may ", "He knoweth how to "]

normal_skills = ["sow discords", "steale Treasures and take them where he is Commanded","deceive thy Foes","give you commande of ANIMAL","giveth answers to All things, past, present and to come", "make men knowing in all Handicraft proffescions", "makethe men STRENGTH in Phylosophy and other sciences", "giveth the favour of friends and foes","giveth TRUE_ADJ honour and dignity to any", "transport men suddenly from one Country into another", "teach all Languages or Tongues presently", "destroy Dignities", "changeth the places of the dead", "cause the Spirits under him to gather together upon their Sepulchres", "giveth riches to a man", "teacheth ye the art of geometry & all ye Liberal sciences","teach the TRUE_ADJ Art of Astronomy","restoreth lost dignity and honours", "maketh men STRENGTH in all artes and sciences","knoweth hidden things and can discover Treasures", "maketh one POS_ADJ in all manner of Ways", "inflame Men and women alike with TRUE_ADJ love", "causeth great Battles and conflicts", "knoweth the POS_ADJ virtues of Herbs and special Stones", "knoweth all the TRUE_ADJ movements of the planets", "knoweth of wars and how the soldiers wille and shalle meet", "maketh men witty and bold","causeth wounds to putrefy that are made by Arrows and Archers", "reconcileth friends", "come to discover things hidden or lost", "fetcheth back runaways", "make you STRENGTH and win arguments", "bring quickly artificers together from all places of the world"]

high_rank_skills = ["telleth TRUE_ADJ of all things past & present", "make one POS_ADJ Knowing in Astrology and all ye Liberall sciences ", "giveth good Familiars and can bewary Treasures", "giveth men the understanding of Birds, lowering of Bullocks, Barking of Doggs & other Creatures", "sheweth ye the TRUE_ADJ meaning of all questions you can ask", "cause Earthquakes", "transmute all Metalls intro gold","giveth true answers to your Demands", "turn all mettals into Gold", "set Citties Castles and great Places on fire", "teacheth the art of astronomy, Arithmitic, geomitry and all other handicrafts absolutely", "maketh a man invisible", "Build houses & high Towers", "destroy thy Enemy's desires and thoughts", "speak marvelously of all POS_ADJ sciences"]

low_rank_intros = ["He is ARTICLE RANK of this realm, humbly serving his king KING_NAME.", "He is a mere and lowly RANK of this realm, barely noticed by his king KING_NAME and thereby more able to serve you.", "He is a humble RANK of the REALM and capable of lesser cantrips.", "He is a humble RANK.", "He is a lowly RANK.", "He is ARTICLE RANK.", "He is ARTICLE RANK in this realm.", "He is a lesser RANK.", "He is a lesser RANK in this realm."]
mid_rank_intros = ["He is ARTICLE RANK and a Marshal of lesser spirits.", "He is a RANK and a middling leader in this realm.", "He is ARTICLE RANK.", "He is ARTICLE RANK in the army of KING_NAME.", "He is ARTICLE RANK in this realm."]
high_rank_intros = ["He is a mighty RANK of this realm, leading the other spirits here.", "He is a powerful RANK.", "He is a great RANK of this realm.", "He is an immense and powerful RANK.", "He is a great imposing RANK of this realm, close in power to his king KING_NAME & a frightening lord.", "He is a mighty RANK.", "He is a great RANK."]

demon_voices = ["If he speaketh to you, it shall be in a VOICE_TYPE voice.", "He speaks in a VOICE_TYPE voice.", "His voice soundeth VOICE_TYPE when you call on him.", "If he speaketh to you, it is in a VOICE_TYPE voice.", "His voice is strange and VOICE_TYPE.", "His voyce is VOICE_TYPE.", "You shall hear him speak in a VOICE_TYPE voice."]

demon_animal_form = ["When in disguise he goes about as ARTICLE ANIMAL", "He may appear first as ARTICLE ANIMAL", "He has shewn himself as ARTICLE ANIMAL", "You may see him firste as ARTICLE ANIMAL", "He disguises himself as ARTICLE ANIMAL"]
demon_spirit_form = [", and in his spirit form he may appear as ARTICLE SPIRIT_FORM.", ", and his demonic form is like to that of ARTICLE SPIRIT_FORM.", " and in the spirit realm as ARTICLE SPIRIT_FORM.", " and he shows himself to initiates as ARTICLE SPIRIT_FORM."]

demon_human_form = ["To walk among men or visit you in publick, he will appear as ARTICLE HUMAN_FORM.", "To go among men he also appeareth as ARTICLE HUMAN_FORM.", "To walk among men he also appeareth as ARTICLE HUMAN_FORM.", "He also appeareth in the form of ARTICLE HUMAN_FORM.", "He may also come to you as ARTICLE HUMAN_FORM to drive a bargain.", "He may also come forth in human forme as ARTICLE HUMAN_FORM.", "He may appeare to you as ARTICLE HUMAN_FORM.", "He may appeare to you as ARTICLE HUMAN_FORM who shall beguile you.", "He can bewitch men into seeing him as ARTICLE HUMAN_FORM.", "He goes about unknown among men as ARTICLE HUMAN_FORM."]

demon_commands_low = ["As a humble DEMON_RANK in the forces of his Lord KING_NAME, DEMON_NAME commands a smalle company of SUM spirits.", "Being a mere DEMON_RANK in KING_NAME's forces, he has about him just SUM loyal familiars.", "As a DEMON_RANK, DEMON_NAME commands SUM spirits which may do your bidding.", "There are SUM spirits in attendance of him, who may do your bidding."]
demon_commands_mid = ["The DEMON_RANK DEMON_NAME commands a moderate force of SUM spirits who he may show you."]
demon_commands_high = ["DEMON_NAME commands a host of SUM spirits & demons, whom he may place at thy command."]

demon_trinket_bits = ["Before attempting to summon the DEMON_RANK DEMON_NAME you will need to find ARTICLE TRINKET and keep it about you.", "In order to conjure and evoke the DEMON_RANK DEMON_NAME, you must make sure you have with you ARTICLE TRINKET, for it shall be required in the summoning.", "Necessary for the summoning or evocation of DEMON_NAME the DEMON_RANK shall be ARTICLE TRINKET, which shall please DEMON_NAME greatly."]

demon_planet = ["Though an infernal spirit DEMON_NAME is subject to Heavenly influences and the Planet PLANET_NAME inflences his actions.", "Under the influence of Celestial bodies, you may find him easier to contact when PLANET_NAME is in Ascendency.", "His Planetary influence is PLANET_NAME.", "DEMON_NAME's Planetary influence is under PLANET_NAME."]

demon_description_addenda = ["DEMON_NAME is a notably cruel demon.", "He is a notorious liar even by the standards of Hell. Do not trust him.", "This spirit delights in games and riddles.", "This spirit's frightening visage can drive men mad.", "Summon him with caution, for he is FALSE_ADJ.", "As TRUE_ADJ as it is possible for one of his rank to be, you can largely trust what DEMON_NAME says."]

demon_sigil_intros = ["His seale lookes like this, which he will owne and submit unto:", "His sigil looks like this:", "His seale is thus made:","His seale is thus to me made:","His sigil is thus to be made:","His seale appeareth thus:", "This is his seal:", "This is his sigil:", "His sigil appeareth thus:", "This is his seale:", "His sigil is thus to be made and used as directed:"]

# Used in ritual generation
pre_ritual_prep = ["Before attempting to summon the DEMON_RANK DEMON_NAME, you will need to PREP and PREP. You will also need to prepare the TRINKET.", "Before summoning DEMON_RANK DEMON_NAME, PREP and PREP and obtain a useful TRINKET.", "Before the ritual can begin you must PREP & PREP and get the TRINKET."]
prep_options = ["bathe thyself thoroughly", "light fragrant incense", "prepare several candles", "meditate for a day", "spit at a church", "spend a day thinking on the Demon's name", "find a Cat and pull its Tail"]


dance_ritual_intros = ["To gaine the attention of DEMON_NAME, you will need to Acte out the following motions.", "This demon is most pleased by deliberate motions, and this is how he is conjured.", "DEMON_NAME is a being of Chaos, and will be most pleased with you if you shew a Dance for him.", "Go through the following physical motions to conjure this DEMON_RANK DEMON_NAME."]

dance_ritual_verbs = ["wave", "wiggle", "gyrate", "push out", "focus thy mental effort upon", "swirl", "shake", "gesture with", "move obscenely"]
dance_ritual_parts = ["left hand", "right hand", "left fist", "right fist", "hands", "fists", "finger of POSS_PRONOUN left hand", "finger of POSS_PRONOUN right hand", "left foot", "right foot", "head", "right arm", "left arm", "right leg", "left leg"]
dance_ritual_first_steps = ["First, VERB POSS_PRONOUN PART, for by this means you shall attract the Demon's attention.", "The first step is to VERB POSS_PRONOUN PART, which shall attract the Demon's attention.", "The first step is to attract the demon's attention. To do so, SECOND_PRONOUN must VERB POSS_PRONOUN PART."]
dance_ritual_second_steps = ["When this is done, the next thing is to VERB_ONE POSS_PRONOUN PART_ONE while you  VERB_TWO POSS_PRONOUN PART_TWO."]
dance_ritual_final_steps = ["Continue this last thing until your brow is beaded with sweat, and then lastly VERB POSS_PRONOUN PART in climax, while you chant \"MAGIC_WORD, MAGIC_WORD\", and all the while hold the TRINKET close about you.", "Keep doing this until you reach a frenzy, keeping the TRINKET held close about you at all times, & finally VERB POSS_PRONOUN PART while you chant \"MAGIC_WORD, MAGIC_WORD\"."]
dance_ritual_truly_final_steps = ["As you feel the dark Power rise within you, use the TRINKET to trace the seale of DEMON_NAME in the Aire, chanting \"MAGIC_WORD\" as you do.", "At the very last, while chanting \"MAGIC_WORD, MAGIC_WORD\" use the TRINKET to trace DEMON_RANK DEMON_NAME's Seale in the air before you.", "At last, keeping up the Chant use the TRINKET to trace mighty DEMON_NAME's Sigil in the aire before you.", "At last, trace DEMON_NAME's sigil in the aire before you with the TRINKET while you chant \"MAGIC_WORD\"."]

circle_ritual_intros = ["This demon is most taken with signs and sigils, and will require geomantic encouragement before he will shew himself to you.", "DEMON_NAME is known to be bound by sigils, and to conjure him you will need to prepare your Chalke.", "DEMON_NAME is a creature of infernal Rules & will obey you presently if you Chalk the correct figures.", "This DEMON_RANK is Mystified by arcane chalkings and may obey you if you practice the following.", "His conjuration relies upon the correct figures, and this is how they are Chalked.", "To summon the DEMON_RANK DEMON_NAME, you will need to carefully construct the following figures.", "To summon DEMON_NAME thou must mark the following signs on the Floor.", "To raise his spirit you will need to Chalk the following.", "Gaining his attention relies on chalking and invoking the following."]
circle_ritual_first_steps = ["First, clean and sweep a Roome, as high as possible in the house and as far away from other people.", "First you must prepare a space. Choose a quiet and secluded room in a Family house.", "You will need a warm and closed room, without windows of any kind, to perform his Rite."]
circle_ritual_second_steps = ["With the room prepared, take a COLOUR chalk or Pencile and enscribe a circle of SIZE feet upon the floor.", "Take now a COLOUR chalk and draw a circle of SIZE feet upon the floor.", "This found, take thee a COLOUR chalk or other staine and draw a circle of exactly SIZE feet upon the floor.", "Next is to take a COLOUR chalk and draw a circle of SIZE feet upon the floor.", "Next, for the required Circle, take a COLOUR chalk and inscribe a Diameter of SIZE feet."]
circle_ritual_trinket_steps= ["Next, take the TRINKET which you have prepared & place it carefully at the COMPASS point, taking utmost care as you do so.", "Next, take the TRINKET which you have prepared and place it at the COMPASS point of the circle."]
circle_ritual_final_steps = ["All this done, around the perimeter of the Circle, write the following words respectively at the points North, South, East & West: <strong>WORD_ONE, WORD_TWO, WORD_THREE, WORD_FOUR</strong>."]
sigil_to_circle = ["Finally Chalke his seale throughout the diameter of the circle."]

altar_types = ["a wooden altar", "altar of wood", "steel altar", "altar of steel", "bone altar", "altar of bone", "any altar you can find", "an altar taken from a church or cathedral", "an altar you have made yourself from driftwood", "a church altar", "a driftwood altar", "an altar", "a rough altar", "a sort of altar", "something like an altar", "an altar of any sorte"]
sacrifice_places = ["dark room", "dark & forlorn woods", "building that has been Abandoned", "Church fallen out of use", "abandoned house", "lonely house", "quiet basement", "cellar", "disused cellar", "room Sealed from within"]
sacrifice_animals = ["lamb", "goat", "cat", "mouse", "dog", "pig", "cow", "deer", "monkey"]
sacrifice_tools = ["iron sword", "hammer", "razor", "shard of mirror", "blunt tool", "stone", "candlestick holder", "pipe", "plank", "sword", "knife", "blade"]
sacrifice_ritual_intros = ["As DEMON_NAME is a powerful DEMON_RANK in the army of KING_TITLE KING_NAME, you will need to make a sacrifice in order to evoke him.", "DEMON_NAME is a powerful DEMON_RANK in KING_TITLE KING_NAME's army, and demands a sacrificial ritual before he will shew himself.", "To conjure or confer with DEMON_NAME, you will need to carry out a sacrificial ritual.", "Before DEMON_NAME will Shew himself to you, you must peform the following sacrifice.", "DEMON_NAME will not show himself or listen to you, until you have appeased him with the following Sacrifice."]
sacrifice_animal_intros = ["Obtain ARTICLE ANIMAL.", "First get thee ARTICLE ANIMAL.", "First get a fine ANIMAL, the best you can find.", "You will first need to get thyself ARTICLE ANIMAL, for it is this that you shall sacrifice."]
sacrifice_ritual_first_steps = ["You shall need to find the right place. This sacrifice must be conducted in ARTICLE SACRIFICE_PLACE.", "You will need to carry out this rite in ARTICLE SACRIFICE_PLACE.", "This ritual must be performed in ARTICLE SACRIFICE_PLACE.", "You will suffer the most dire consequences if this ritual is not performed in ARTICLE SACRIFICE_PLACE.", "If you do not perform this rite in ARTICLE SACRIFICE_PLACE the most dire consequences shall come back to you."]
sacrifice_ritual_second_steps = ["In this place, you must now prepare ALTAR_TYPE, & do so solemnly. When you are done, place the TRINKET upon the altar.", "Next, in this place you must prepare ALTAR_TYPE and place the TRINKET upon it. You may feel fear while you do so, but to appease DEMON_NAME you must do it whilst seeming to show good cheer.", "Now in this place prepare ALTAR_TYPE. Make this altar & the space around it as clean as possible, and place the TRINKET upon the altar.", "Next keeping thy mind focused upon thy task, prepare ALTAR_TYPE in the place you have chosen. Then place the TRINKET upon the altar.", "Now will you need to prepare ALTAR_TYPE there. Having done so, place the TRINKET upon the altar.", "Next prepare there ALTAR_TYPE and place the TRINKET upon the altar."]
sacrifice_ritual_third_steps = ["At last, setting the bound & restrained ANIMAL upon thy altar, take ARTICLE TOOL in thy hand.", "Next set the ANIMAL upon the altar, restrained as necessary, then brace thyself and take up ARTICLE TOOL.", "Next place the well-bound ANIMAL upon the altar and taketh ARTICLE TOOL.", "Next take ARTICLE TOOL & set the ANIMAL upon thy altar, taking care that it is well bound."]
sacrifice_ritual_songs = ["Before you commit the final deed, focus thy mind upon the word of power: MAGIC_WORD.", "As you steel thyself for the deed, first imagine, then begin to chant aloud the magic word \"MAGIC_WORD, MAGIC_WORD\".", "Next as you prepare to slay the beast, chant louder and louder \"MAGIC_WORD, MAGIC_WORD\"."]
sacrifice_ritual_climax = ["As you enter a properly Magickal state, at last slay the ANIMAL with thy TOOL. Now use the blood to draw the sigil of DEMON_NAME on the ground before you.", "At last, slay the ANIMAL with thy TOOL and let its blood flow over the altar. At last use the blood to draw the sigil of DEMON_NAME on the ground before you.", "At last slay the ANIMAL with thy TOOL and let its blood runneth into a Cup. Now pour the cup onto the ground before you & trace the sigil of DEMON_NAME on the ground before you.", "Next is to kill the ANIMAL with thy TOOL. When the deed is done, spread its blood about the floor in the pattern of great DEMON_NAME's sigil. thou art ready to consult the great DEMON_RANK DEMON_NAME.", "Kill now the ANIMAL with thy TOOL and spread the blood about the floor in the figure of the demon's Seale. In this last act of violence you shall have appeased the great DEMON_RANK DEMON_NAME.", "And the last Acte in pleasing the great DEMON_NAME is to kill the ANIMAL with thy TOOL and use the blood to draw the sigil of DEMON_NAME on the ground before you."]

post_ritual_phrase = ["If this being done He does not appear, rehearse the Conjuration severall times, & DEMON_RANK DEMON_NAME shall in POS_ADJ truth shew Himself to you.", "If after this last being done you do not meete the DEMON_RANK DEMON_NAME, repeat this Conjuration in a louder voice and he will in POS_ADJ appeare.", "Then if you do not sense his presence, repeat the Incantation until you Doe.", "If you do not then meete with DEMON_RANK DEMON_NAME, repeat the incantation againe, but louder.", "If this does not worke to raise the demon, simply try againe the next day at midnight, this time performing the rite Naked."]


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
        elif word[-1] == "s" and not word[-2:] == "es" and not word[-2:] == "us":
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

    if (word[-2:] == "ed") and not (word[-3:] == "eed"):
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
