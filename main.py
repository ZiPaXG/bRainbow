import pygame as pg
from models.game import Game
from models.card import Card
from models.player import Player
from models.deck import Deck
from views.application import Application

''' 
    При чтении json-файла с картами:
    1 строка - название
    2 строка - цвет названия
    3 строка - цвет фона
    (4 строка - дополнительное обозначение для черной карты)
'''

list_players = list()
list_players.append(Player("ZiPaXG"))
deck = Deck()
deck.shuffleCards()
deck.give_cards(list_players)

# Запуск приложения
app = Application(deck)
app.run(list_players)

