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
        self.rule_rectangles = [
            pygame.Rect(0, 0, 0, 0)
        ]
        self.end_rectangles = [
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
        display.blit(self.font_very_big.render('bRainbow', False, (255, 255, 255)), (50, 200))

        text_start = self.font_big.render('Играть', False, (255, 255, 255))
        self.menu_rectangles[0] = text_start.get_rect()
        self.menu_rectangles[0].x, self.menu_rectangles[0].y = 50, 350
        display.blit(text_start, (50, 350))

        text_rule = self.font_big.render('Правила', False, (255, 255, 255))
        self.menu_rectangles[1] = text_rule.get_rect()
        self.menu_rectangles[1].x, self.menu_rectangles[1].y = 50, 450
        display.blit(text_rule, (50, 450))

        text_exit = self.font_big.render('Выйти', False, (255, 255, 255))
        self.menu_rectangles[2] = text_exit.get_rect()
        self.menu_rectangles[2].x, self.menu_rectangles[2].y = 50, 550
        display.blit(text_exit, (50, 550))

    def draw_rule(self, display: pygame.Surface):
        text_back = self.font_big.render('Назад', False, (255, 255, 255))
        self.rule_rectangles[0] = text_back.get_rect()
        self.rule_rectangles[0].x, self.rule_rectangles[0].y = 50, 20
        display.blit(text_back, (50, 20))

        display.blit(
            self.font_middle.render('Всего будет 24 раунда. Каждому игроку будет выдана колода из 6 карт', False, (255, 255, 255)),
            (50, 100))
        display.blit(
            self.font_middle.render('Также есть общая колода карт. Они будут вытягиваться поочереди. К ним применяются следующие правила:', False, (255, 255, 255)),
            (50, 170))
        display.blit(
            self.font_middle.render('1. На карте из общей колоды указано <Цвет> - берем карту, название которой есть цвет окраски слова', False, (255, 255, 255)),
            (50, 240))
        display.blit(
            self.font_middle.render('2. На карте из общей колоды название написано черным - берем карту, название которой есть цвет фона', False, (255, 255, 255)),
            (50, 310))
        display.blit(
            self.font_middle.render('3. Выпала карта bRainbow-нужно быстрее всех забрать ее', False, (255, 255, 255)),
            (50, 380))
        display.blit(
            self.font_middle.render('4. На карте из общей колоды указано <Название> - берем карту с цветом названия указанного слова', False, (255, 255, 255)),
            (50, 450))

    def draw_end(self, display: pygame.Surface, score_player=0):
        display.blit(
            self.font_very_big.render('Игра окончена', False, (255, 255, 255)),
            (600, 100))
        display.blit(
            self.font_big.render(f'Ваши очки: {score_player}', False, (255, 255, 255)),
            (715, 210))
        
        text_restart = self.font_middle.render('Переиграть', False, (255, 255, 255))
        self.end_rectangles[0] = text_restart.get_rect()
        self.end_rectangles[0].x, self.end_rectangles[0].y = 620, 280
        display.blit(text_restart, (620, 280))
        
        text_exit = self.font_middle.render('Выйти', False, (255, 255, 255))
        self.end_rectangles[1] = text_exit.get_rect()
        self.end_rectangles[1].x, self.end_rectangles[1].y = 900, 280
        display.blit(text_exit, (900, 280))

    def redraw(self, display: pygame.Surface, player: Player):
        display.fill(GameView.BACKGROUND_COLOR, (0, 0, GEOMETRY['display'][0], GEOMETRY['display'][1]))

        if self.current_state == STATES['menu']:
            self.draw_menu(display)

        elif self.current_state == STATES['rule']:
            self.draw_rule(display)

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

        elif self.current_state == STATES['end']:
            self.draw_end(display, player.get_score())
        
        pygame.display.update()
