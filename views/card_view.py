import pygame.image
from assets.config import GEOMETRY


class CardView:
    def __init__(self, path_img):
        self.width = GEOMETRY["card"][0]
        self.height = GEOMETRY["card"][1]
        self.img = pygame.transform.scale(pygame.image.load(path_img), (self.width, self.height))
        self.rectangle = pygame.Rect(0, 0, 0, 0)

    def draw(self, display: pygame.Surface, x: int, y: int):
        self.rectangle = pygame.Rect(x, y, self.width, self.height)
        display.blit(self.img, (x, y))

    def check_collide_rect(self, display: pygame.Surface):
        if self.rectangle.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(display, (0, 255, 255), self.rectangle, 4, 10)
