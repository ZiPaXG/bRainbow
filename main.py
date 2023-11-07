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

list_players = list()
list_players.append(Player("ZiPaXG"))
deck = Deck()
deck.shuffleCards()
deck.give_cards(list_players)

isRunning = True
print("Вас приветствует игра bRainbow! ")
while isRunning:
    print("Выбирайте опцию:")
    print("1 - Начать игру")
    print("2 - Посмотреть правила")
    print("3 - Выйти из игры")
    a = int(input())
    match a:
        case 3:
            isRunning = not isRunning
        case 2:
            deck.get_rools()
        case 1:
            # Сама игра (пока что основа в консоли)
            for i in range(len(deck.rule_deck)):
                print(deck.rule_deck[i])
                print(f"Игрок {list_players[0]} - выбирайте свою карту (введите от 1 до 6). Если нет подходящей - напишите 0")
                a = int(input())
