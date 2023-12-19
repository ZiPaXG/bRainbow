import pygame

from assets.config import *
from models.game import Game
from models.player import Player
from views.game_view import GameView
from models.deck import Deck


class Application:
    def __init__(self, list_players: list[Player]):
        pygame.init()
        pygame.font.init()

        self.list_players = list_players
        self.deck = None
        self.size = (self.width, self.height) = GEOMETRY['display']

        self.FPS = RESOURCES['FPS']
        self.clock = pygame.time.Clock()

        self.display = pygame.display.set_mode(self.size)
        pygame.display.set_caption(RESOURCES['title'])

        self.vgame = GameView(self.display.get_width(), self.display.get_height())

    def restart_game(self):
        for player in self.list_players:
            player.clear_score()

        self.deck = Deck()
        self.deck.shuffleCards()
        self.deck.give_cards(self.list_players)

        # Добавляем визуал карт (карты игроков и основная колода)
        self.vgame.add_player_cards_view(self.deck)
        self.vgame.add_rule_cards_view(self.deck)

    def run(self):
        self.restart_game()
        running = True
        while running:
            self.vgame.redraw(self.display, self.list_players[0])
            for event in pygame.event.get():
                # нажали крестик на окне
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if self.vgame.current_state == STATES['menu']:
                            if self.vgame.menu_rectangles[0].collidepoint(pygame.mouse.get_pos()):
                                self.vgame.current_state = STATES['game']
                            elif self.vgame.menu_rectangles[1].collidepoint(pygame.mouse.get_pos()):
                                self.vgame.current_state = STATES['rule']
                            elif self.vgame.menu_rectangles[2].collidepoint(pygame.mouse.get_pos()):
                                running = False

                        if self.vgame.current_state == STATES['rule']:
                            if self.vgame.rule_rectangles[0].collidepoint(pygame.mouse.get_pos()):
                                self.vgame.current_state = STATES['menu']

                        if self.vgame.current_state == STATES['game']:
                            if len(self.vgame.rule_cards_view) > 1:
                                if self.vgame.rule_cards_view[1].rectangle.collidepoint(pygame.mouse.get_pos()) and self.vgame.rule_cards_view[1].is_visible_border:
                                    Game.check_selected_card(self.list_players[0], self.deck.get_rule_deck()[1],
                                                            self.deck.get_players_deck()[1], 6)
                                    self.vgame.rule_cards_view.pop(1)
                                    self.deck.remove_rule_card_from_deck()
                                elif self.vgame.players_cards_view[0][0].rectangle.collidepoint(pygame.mouse.get_pos()):
                                    Game.check_selected_card(self.list_players[0], self.deck.get_rule_deck()[1],
                                                            self.deck.get_players_deck()[1], -1)
                                    self.vgame.rule_cards_view.pop(1)
                                    self.deck.remove_rule_card_from_deck()
                                else:
                                    for i in range(len(self.vgame.players_cards_view[1])):
                                        if self.vgame.players_cards_view[1][i].rectangle.collidepoint(pygame.mouse.get_pos()):
                                            Game.check_selected_card(self.list_players[0], self.deck.get_rule_deck()[1],
                                                                    self.deck.get_players_deck()[1], i)
                                            self.vgame.rule_cards_view.pop(1)
                                            self.deck.remove_rule_card_from_deck()
                            if len(self.vgame.rule_cards_view) == 1:
                                self.vgame.current_state = STATES['end']

                        if self.vgame.current_state == STATES['end']:
                            if self.vgame.end_rectangles[0].collidepoint(pygame.mouse.get_pos()):
                                self.restart_game()
                                self.vgame.current_state = STATES['game']

                            if self.vgame.end_rectangles[1].collidepoint(pygame.mouse.get_pos()):
                                running = not running

        pygame.quit()
        