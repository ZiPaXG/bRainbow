import pygame as pg
from models.game import Game
from models.card import Card
from models.player import Player
from models.deck import Deck

''' 
    При чтении json-файла с картами:
    1 строка - название
    2 строка - цвет названия
    3 строка - цвет фона
'''

game = Game(pg)
game.start(pg)

