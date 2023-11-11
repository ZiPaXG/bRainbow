import pygame

from assets.config import RESOURCES, GEOMETRY
from views.game_view import GameView


class Application:

    def __init__(self):
        pygame.init()
        self.size = (self.width, self.height) = GEOMETRY['display']

        self.FPS = RESOURCES['FPS']
        self.clock = pygame.time.Clock()

        self.display = pygame.display.set_mode(self.size)
        pygame.display.set_caption(RESOURCES['title'])

        self.vgame = GameView(self.display.get_width(), self.display.get_height())

    def run(self):
        running = True
        while running:
            self.vgame.redraw(self.display)
            for event in pygame.event.get():
                # нажали крестик на окне
                if event.type == pygame.QUIT:
                    running = False

        pygame.quit()


app = Application()
app.run()