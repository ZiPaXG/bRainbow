import pygame.image
from assets.config import GEOMETRY


class CardView:
    def __init__(self, path_img):
        self.width = GEOMETRY["card"][0]
        self.height = GEOMETRY["card"][1]
        self.img = pygame.transform.scale(pygame.image.load(path_img), (self.width, self.height))
        self.first_point = [0, 0]
        self.second_point = [0, 0]

    def draw(self, display: pygame.Surface, x: int, y: int):
        self.first_point = [x, y]
        self.second_point = [x + self.width, y + self.height]
        display.blit(self.img, (x, y))
        print(self.first_point, self.second_point)
