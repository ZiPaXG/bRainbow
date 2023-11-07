from models.card import Card
from models.player import Player
import json
import random

class Deck:
    def __init__(self):
        self.players_deck = []
        self.rule_deck = []

        # Создание колоды карт для игроков
        with open('assets/data/cards_dict.json', 'r', encoding='UTF-8') as json_file:
            list_cards = list(json.load(json_file).values())
            for i in range(len(list_cards)):
                card_list = []
                for j in range(6):
                    card_list.append(Card(list_cards[i][j][0], list_cards[i][j][1], list_cards[i][j][2], f'assets/imageCards/deckCards/{i+1}/{j+1}.png'))
                self.players_deck.append(card_list)

        # Создание колоды карт правил
        for i in range(3):
            self.rule_deck.append(Card("bRainbow", "", "", f"assets/imageCards/ruleCards/bRainbowCard.png", "bRainbow"))
        with open('assets/data/cards_rule.json', 'r', encoding='UTF-8') as json_file:
            list_cards = list(json.load(json_file).values())
            for i in range(5):
                self.rule_deck.append(Card(list_cards[0][i][0], list_cards[0][i][1], list_cards[0][i][2], f"assets/imageCards/ruleCards/blackCards/{i+1}.png", f"{list_cards[0][i][3]}"))
            for i in range(8):
                self.rule_deck.append(Card(list_cards[1][i][0], list_cards[1][i][1], list_cards[1][i][2], f"assets/imageCards/ruleCards/colorCards/{i+1}.png", "цвет"))
            for i in range(8):
                self.rule_deck.append(Card(list_cards[2][i][0], list_cards[2][i][1], list_cards[2][i][2], f"assets/imageCards/ruleCards/nameCards/{i+1}.png", "название"))

    def shuffleCards(self):
        random.shuffle(self.rule_deck)
        random.shuffle(self.players_deck)

    def give_cards(self, list_players: list[Player]):
        for i in range(len(list_players)):
            list_players[i].hand_deck = self.players_deck[i]




