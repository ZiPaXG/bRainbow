import pygame
from assets.config import GEOMETRY
from views.card_view import CardView
from models.deck import Deck


class GameView:
    # Доделать
    BACKGROUND_COLOR = (0, 81, 44)

    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height
        self.background_img = None
        self.players_cards_view = []
        self.rule_cards_view = []

    def add_player_cards_view(self, deck: Deck):
        lst_cards = deck.get_players_deck()
        for i in range(len(lst_cards)):
            deck_list = []
            for j in range(6):
                deck_list.append(CardView(lst_cards[i][j].img_path))
            self.players_cards_view.append(deck_list)

    def add_rule_cards_view(self, deck: Deck):
        lst_cards = deck.get_rule_deck()
        for i in range(len(lst_cards)):
            self.rule_cards_view.append(CardView(lst_cards[i].img_path))

    def redraw(self, display: pygame.Surface):
        if self.background_img is None:
            display.fill(GameView.BACKGROUND_COLOR, (0, 0, GEOMETRY['display'][0], GEOMETRY['display'][1]))
        for j in range(len(self.players_cards_view[0])):
            self.players_cards_view[0][j].draw(display, GEOMETRY['start_pos_card'][0] + 15 + GEOMETRY['card'][0] * j + GEOMETRY['dx_card'] * j, GEOMETRY['start_pos_card'][1])
        pygame.display.update()
