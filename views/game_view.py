import pygame
from assets.config import GEOMETRY

class GameView:
    # Доделать
    BACKGROUND_COLOR = (0, 81, 44)

    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height
        self.background_img = None

    def redraw(self, display: pygame.Surface):
        if self.background_img is None:
            display.fill(GameView.BACKGROUND_COLOR, (0, 0, GEOMETRY['display'][0], GEOMETRY['display'][1]))
        pygame.display.update()
