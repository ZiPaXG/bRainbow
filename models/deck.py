from models.card import Card
import json

class Deck:
    def __init__(self):
        self.deck = []
        with open('assets/data/cards_dict.json', 'r', encoding='UTF-8') as json_file:
            list_cards = list(json.load(json_file).values())
            for i in range(len(list_cards)):
                card_list = []
                for j in range(6):
                    card_list.append(Card(list_cards[i][j][0], list_cards[i][j][1], list_cards[i][j][2], f'assets/imageCards/deckCards/{i+1}/{j+1}.png'))
                self.deck.append(card_list)

deck = Deck()