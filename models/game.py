from models.card import Card
from models.player import Player

class Game:

    @staticmethod
    def get_rules():
        print("Всего будет 24 раунда. Каждому игроку будет выдана колода из 6 карт")
        print("Также есть общая колода карт (24 карты). Они будут вытягиваться поочереди. К ним применяются следующие правила: ")
        print("Правило 1: На карте из общей колоды указано <Цвет> - берем карту, название которой есть цвет окраски основного слова")
        print("Правило 2: На карте из общей колоды название написано черным - берем карту, название которой есть цвет фона")
        print("Правило 3: Выпала карта bRainbow - нужно быстрее всех забрать ее")
        print("Правило 4: На карте из общей колоды указано <Название> - берем карту с цветом названия основного слова, который указан")

    @staticmethod
    def check_selected_card(player: Player, deck_card: Card, player_cards: list[Card], num_card):
        print(deck_card)
        print(f'{player_cards} - {num_card}')
        if num_card == 6:
            if deck_card.gameRule != "bRainbow":
                player.add_score(3)

        elif num_card != -1:
            if deck_card.fgColor == "черный":
                if player_cards[num_card].name != deck_card.bgColor:
                    player.add_score(3)
            elif deck_card.gameRule == "цвет":
                if player_cards[num_card].name != deck_card.fgColor:
                    player.add_score(3)
            elif deck_card.gameRule == "название":
                if player_cards[num_card].fgColor != deck_card.name:
                    player.add_score(3)
        else:
            if deck_card.fgColor == "черный":
                for i in range(len(player_cards)):
                    if deck_card.bgColor == player_cards[i].name:
                        player.add_score(3)
                        break
            elif deck_card.gameRule == "цвет":
                for i in range(len(player_cards)):
                    if deck_card.fgColor == player_cards[i].name:
                        player.add_score(3)
                        break
            elif deck_card.gameRule == "название":
                for i in range(len(player_cards)):
                    if deck_card.name == player_cards[i].fgColor:
                        player.add_score(3)
                        break
            elif deck_card.gameRule == "bRainbow":
                player.add_score(3)
        print(player.get_score())
