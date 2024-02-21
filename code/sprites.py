import pygame

from globals import *


class Sprite(pygame.sprite.Sprite):
    def __init__(self, pos, surf=pygame.Surface, groups=None):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(center=pos)


class Clickable_Sprite(Sprite):
    def __init__(self, pos, surf=pygame.Surface, groups=None):
        super().__init__(pos, surf, groups)

    def update(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            print('colliding')
