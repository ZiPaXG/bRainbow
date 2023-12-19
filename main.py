from models.player import Player
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

# Запуск приложения
app = Application(list_players)
app.run()

