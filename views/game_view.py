import pygame
from assets.config import *
from models.player import Player
from views.card_view import CardView
from models.card import Card
from models.deck import Deck

class GameView:
    BACKGROUND_COLOR = (0, 81, 44)

    def __init__(self, width: float, height: float):
        self.current_state = STATES['menu']
        self.width = width
        self.height = height
        self.background_img = None
        self.players_cards_view = []
        self.rule_cards_view = []
        self.font_very_big = pygame.font.SysFont('Arial', 84)
        self.font_big = pygame.font.SysFont('Arial', 48)
        self.font_middle = pygame.font.SysFont('Arial', 36)
        self.menu_rectangles = [
            pygame.Rect(0, 0, 0, 0),
            pygame.Rect(0, 0, 0, 0),
            pygame.Rect(0, 0, 0, 0)
        ]

    def add_player_cards_view(self, deck: Deck):
        lst_cards = deck.get_players_deck()

        # вставляем карту не выбирать
        lst_cards.insert(0, [Card("dont_select", "", "", "assets/imageCards/dont_select.png")])
        print(lst_cards)
        for i in range(len(lst_cards)):
            deck_list = []
            for j in range(len(lst_cards[i])):
                deck_list.append(CardView(lst_cards[i][j].img_path, True))
            self.players_cards_view.append(deck_list)

    def add_rule_cards_view(self, deck: Deck):
        lst_cards = deck.get_rule_deck()

        # вставляем рубашку карт правил
        lst_cards.insert(0, Card("back", "", "", "assets/imageCards/back.png"))
        for i in range(len(lst_cards)):
            self.rule_cards_view.append(CardView(lst_cards[i].img_path, True if lst_cards[i].name == 'bRainbow' else False))

    def draw_menu(self, display: pygame.Surface):
        display.blit(self.font_very_big.render('bRainbow', False, (255, 255, 255)), (650, 200))

        text_start = self.font_big.render('Играть', False, (255, 255, 255))
        self.menu_rectangles[0] = text_start.get_rect()
        self.menu_rectangles[0].x, self.menu_rectangles[0].y = 650, 350
        display.blit(text_start, (650, 350))

        text_rule = self.font_big.render('Правила', False, (255, 255, 255))
        self.menu_rectangles[1] = text_rule.get_rect()
        self.menu_rectangles[1].x, self.menu_rectangles[1].y = 650, 450
        display.blit(text_rule, (650, 450))

        text_exit = self.font_big.render('Выйти', False, (255, 255, 255))
        self.menu_rectangles[2] = text_exit.get_rect()
        self.menu_rectangles[2].x, self.menu_rectangles[2].y = 650, 550
        display.blit(text_exit, (650, 550))
        print(self.menu_rectangles)

    def redraw(self, display: pygame.Surface, player: Player):
        display.fill(GameView.BACKGROUND_COLOR, (0, 0, GEOMETRY['display'][0], GEOMETRY['display'][1]))

        if self.current_state == STATES['menu']:
            self.draw_menu(display)

        elif self.current_state == STATES['game']:
            display.blit(self.font_big.render(f'Очки: {player.get_score()}', False, (255, 255, 255)), (10, 10))

            if len(self.rule_cards_view) > 1:
                if len(self.rule_cards_view) > 2:
                    # отрисовка рубашки карт с правилами
                    self.rule_cards_view[0].draw(display, GEOMETRY['start_pos_back'][0], GEOMETRY['start_pos_back'][1])

                # отрисовка игровой карты
                self.rule_cards_view[1].draw(display, GEOMETRY['start_pos_game_card'][0], GEOMETRY['start_pos_game_card'][1])

                # отрисовка карт игрока
                self.players_cards_view[0][0].draw(display, GEOMETRY['start_pos_dont_select'][0], GEOMETRY['start_pos_dont_select'][1])
                for j in range(0, len(self.players_cards_view[1])):
                    self.players_cards_view[1][j].draw(display, GEOMETRY['start_pos_cards'][0] + 15 + GEOMETRY['card'][0] * j +
                                                    GEOMETRY['dx_card'] * j, GEOMETRY['start_pos_cards'][1])

                # Проверка на позицию мыши
                self.players_cards_view[0][0].check_collide_rect(display)
                for j in range(len(self.players_cards_view[1])):
                    self.players_cards_view[1][j].check_collide_rect(display)
                self.rule_cards_view[1].check_collide_rect(display)

        pygame.display.update()
