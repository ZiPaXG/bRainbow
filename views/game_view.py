import pygame
from assets.config import GEOMETRY
from models.player import Player
from views.card_view import CardView
from models.card import Card
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
        self.font = pygame.font.SysFont('Arial', 48)

    def add_player_cards_view(self, deck: Deck):
        lst_cards = deck.get_players_deck()
        for i in range(len(lst_cards)):
            deck_list = []
            for j in range(6):
                deck_list.append(CardView(lst_cards[i][j].img_path))
            self.players_cards_view.append(deck_list)

    def add_rule_cards_view(self, deck: Deck):
        lst_cards = deck.get_rule_deck()

        # вставляем рубашку карт правил
        lst_cards.insert(0, Card("back", "", "", f"assets/imageCards/back.png"))
        for i in range(len(lst_cards)):
            self.rule_cards_view.append(CardView(lst_cards[i].img_path))

    def redraw(self, display: pygame.Surface, player: Player):
        if self.background_img is None:
            display.fill(GameView.BACKGROUND_COLOR, (0, 0, GEOMETRY['display'][0], GEOMETRY['display'][1]))

        display.blit(self.font.render(f'Очки: {player.get_score()}', False, (255, 255, 255)), (10, 10))
        if len(self.rule_cards_view) > 1:
            # отрисовка рубашки карт с правилами
            self.rule_cards_view[0].draw(display, GEOMETRY['start_pos_back'][0], GEOMETRY['start_pos_back'][1])

            # отрисовка игровой карты
            self.rule_cards_view[1].draw(display, GEOMETRY['start_pos_game_card'][0], GEOMETRY['start_pos_game_card'][1])

        else:
            self.rule_cards_view[0].is_visible_border = False

        # отрисовка карт игрока
        for j in range(len(self.players_cards_view[0])):
            self.players_cards_view[0][j].draw(display, GEOMETRY['start_pos_cards'][0] + 15 + GEOMETRY['card'][0] * j +
                                               GEOMETRY['dx_card'] * j, GEOMETRY['start_pos_cards'][1])

        # Проверка на позицию мыши
        for j in range(len(self.players_cards_view[0])):
            self.players_cards_view[0][j].check_collide_rect(display)
        self.rule_cards_view[0].check_collide_rect(display)

        pygame.display.update()
