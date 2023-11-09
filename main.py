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
    (4 строка - дополнительное обозначение для черной карты)
'''

list_players = list()
list_players.append(Player("ZiPaXG"))
deck = Deck()
deck.shuffleCards()
deck.give_cards(list_players)
game = Game(pg)

game.start_display(pg)
'''isRunning = True
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
            game.get_rools()
        case 1:
            # Сама игра (пока что основа в консоли)
            for i in range(len(deck.rule_deck)):
                print(deck.rule_deck[i])
                print(f"Игрок {list_players[0]} - выбирайте свою карту (введите от 1 до 6). "
                      f"Если выпала карта bRainbow - введите 7, если нет подходящей карты - введите 0")
                print(f"Колода: {list_players[0].hand_deck}")
                a = int(input())
                game.check_selected_card(list_players[0], deck.rule_deck[i], list_players[0].hand_deck, a-1)
                print(list_players[0].get_score())

            # Подсчет очков
            print("Общее количество очков: ")
            for i in range(len(list_players)):
                print(f"{list_players[i]} - {list_players[i].get_score()}")'''

