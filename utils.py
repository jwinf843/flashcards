def create_card(word, answer, type=None, example=None):
    return {
        'word': word,
        'answer': answer,
        'example': example,
        'type': type
        'deck': None,
        'timer': 0,
        'history': []
    }

def create_deck(name):
    return {
        'name': name,
        'cards': []
    }

def add_card_to_deck(deck, card):
    if card not in deck['cards']:
        deck['cards'].append(card)