import random
import json
from card import Card
from deck_cards import DeckCards


# Небольшая заметка к получению значения карточки из JSON-файла:
# 1 строка - слово
# 2 строка - цвет слова
# 3 строка - цвет фона


def generate_cards(num_deck, index_img):
    path = f"assets/imageCards/{num_deck}/{index_img}.png"

class AllPlayerCards:
    def __init__(self, count_players):
        self.list_all_decks = []
        self.orderDecks = random.sample(range(1, count_players), 6)
        for i in range(len(self.orderDecks)):
            generate_cards(self.orderDecks[i], i + 1)


