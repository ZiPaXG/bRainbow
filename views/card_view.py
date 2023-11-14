import pygame.image

from assets.config import GEOMETRY


class CardView:
    def __init__(self, path_img):
        self.width = GEOMETRY["card"][0]
        self.height = GEOMETRY["card"][1]
        self.img = pygame.image.load(path_img)

    def draw(self, display: pygame.Surface, x: int, y: int):
        display.blit(self.img, (x, y))
