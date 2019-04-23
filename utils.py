import json

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
        
def save_deck(deck_name):
    filename = '{}.txt'.format(deck_name)
    with open(filename, 'w') as outfile:
        json.dump(deck, outfile)
        
def load_deck(deck_name):
    filename = '{}.txt'.format(deck_name)
    with open(filename) as json_file:
        deck = json.load(json_file)
        return deck
        