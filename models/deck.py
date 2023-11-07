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
            self.rule_deck.append(Card("bRainbow", "", "", f"assets/imageCards/ruleCards/bRainbowCard.png", True))
        with open('assets/data/cards_rule.json', 'r', encoding='UTF-8') as json_file:
            list_cards = list(json.load(json_file).values())
            for i in range(5):
                self.rule_deck.append(Card(list_cards[0][i][0], list_cards[0][i][1], list_cards[0][i][2], f"assets/imageCards/ruleCards/blackCards/{i+1}.png", True))
            for i in range(8):
                self.rule_deck.append(Card(list_cards[1][i][0], list_cards[1][i][1], list_cards[1][i][2], f"assets/imageCards/ruleCards/colorCards/{i+1}.png", True))
            for i in range(8):
                self.rule_deck.append(Card(list_cards[2][i][0], list_cards[2][i][1], list_cards[2][i][2], f"assets/imageCards/ruleCards/nameCards/{i+1}.png", True))

    def shuffleCards(self):
        random.shuffle(self.rule_deck)
        random.shuffle(self.players_deck)

    def give_cards(self, list_players:list[Player]):
        for i in range(len(list_players)):
            list_players[i].hand_deck = self.players_deck[i]

    def get_rools(self):
        print("Всего будет 24 раунда. Каждому игроку будет выдана колода из 6 карт")
        print("Также есть общая колода карт (24 карты). Они будут вытягиваться поочереди. К ним применяются следующие правила: ")
        print("Правило 1: На карте из общей колоды указано <Цвет> - берем карту, название которой есть цвет окраски основного слова")
        print("Правило 2: На карте из общей колоды название написано черным - берем карту, название которой есть цвет фона")
        print("Правило 3: Выпала карта bRainbow - нужно быстрее всех забрать ее")
        print("Правило 4: На карте из общей колоды указано <Название> - берем карту с цветом названия основного слова, который указан")



