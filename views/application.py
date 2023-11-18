import pygame

from assets.config import RESOURCES, GEOMETRY
from models.game import Game
from models.player import Player
from views.game_view import GameView


class Application:

    def __init__(self, deck):
        pygame.init()
        pygame.font.init()
        self.deck = deck
        self.size = (self.width, self.height) = GEOMETRY['display']

        self.FPS = RESOURCES['FPS']
        self.clock = pygame.time.Clock()

        self.display = pygame.display.set_mode(self.size)
        pygame.display.set_caption(RESOURCES['title'])

        self.vgame = GameView(self.display.get_width(), self.display.get_height())

        # Добавляем визуал карт (карты игроков и основная колода)
        self.vgame.add_player_cards_view(deck)
        self.vgame.add_rule_cards_view(deck)

    def run(self, list_players: list[Player]):
        running = True
        while running:
            self.vgame.redraw(self.display, list_players[0])
            for event in pygame.event.get():
                # нажали крестик на окне
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if len(self.vgame.rule_cards_view) > 1:
                            if self.vgame.rule_cards_view[0].rectangle.collidepoint(pygame.mouse.get_pos()):
                                self.vgame.rule_cards_view.pop(1)
                                self.deck.remove_rule_card_from_deck()
                            else:
                                for i in range(len(self.vgame.players_cards_view[0])):
                                    if self.vgame.players_cards_view[0][i].rectangle.collidepoint(pygame.mouse.get_pos()):
                                        Game.check_selected_card(list_players[0], self.deck.get_rule_deck()[1], self.deck.get_players_deck()[0], i)

                for i in self.vgame.players_cards_view[0]:
                    i.check_collide_rect(self.display)

        pygame.quit()
        