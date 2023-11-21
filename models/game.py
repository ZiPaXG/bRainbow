from models.card import Card
from models.player import Player


class Game:
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
