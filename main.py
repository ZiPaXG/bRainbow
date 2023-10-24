import pygame as pg
from models.game import Game
from models.card import Card
from models.player import Player

pg.init()
game = Game(pg)
game.start(pg)
