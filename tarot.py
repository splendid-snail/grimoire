class Card:
    def __init__(self, number, name, suit, arcana):
        self.number = number
        self.name = name
        self.suit = suit
        self.arcana = arcana
        self.rank = 0


def generate_minor_suit(suit, deck, total_cards_made):
    suit_cards_made = 0
    card_types = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "Page", "Knight", "Queen", "King"]
    while suit_cards_made < 14:
        new_card_name = card_types[suit_cards_made] + " of " + suit
        new_card = Card(total_cards_made, new_card_name, suit, "Minor")
        if suit_cards_made > 8: #Cards of rank X or above are midranks
            new_card.rank = 1
        deck.append(new_card)
        suit_cards_made += 1
        total_cards_made += 1
    return deck, total_cards_made

def generate():
    major_arcana = ["The Fool", "The Magician", "The High Priestess", "The Empress", "The Emperor", "The Hierophant", "The Lovers", "The Chariot", "Strength", "The Hermit", "Wheel of Fortune", "Justice", "The Hanged Man", "Death", "Temperance", "The Devil", "The Tower", "The Star", "The Moon", "The Sun", "Judgement", "The World"]
    cards_made = 0
    tarot_deck = []

    while cards_made < 78:
        while cards_made < 22: #Major acana, followed by wands, pentacles, cups, swords
            new_card = Card(cards_made, major_arcana[cards_made], 0, "Major")
            new_card.rank = 2
            tarot_deck.append(new_card)
            cards_made += 1
        while cards_made < 36:
            tarot_deck, cards_made = generate_minor_suit("Wands", tarot_deck, cards_made)
        while cards_made < 49:
            tarot_deck, cards_made = generate_minor_suit("Pentacles", tarot_deck, cards_made)
        while cards_made < 63:
            tarot_deck, cards_made = generate_minor_suit("Cups", tarot_deck, cards_made)
        while cards_made < 77:
            tarot_deck, cards_made = generate_minor_suit("Swords", tarot_deck, cards_made)
    return tarot_deck
