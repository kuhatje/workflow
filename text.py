import pygame
from settings import Settings

pygame.init()

s = Settings()


class Text:
    def __init__(self, msg, x, y, x_displace=0, y_displace=0, size='small', color=s.black, antialias=True, surface=s.display):
        self.color = color
        self.textSurf, self.textRect = None, None
        self.surface = surface
        self.surfaceRect = self.surface.get_rect()
        
        if size == 'small':
            self.textSurf = s.smallFont.render(msg, antialias, self.color)
            self.textRect = self.textSurf.get_rect()
        elif size == 'large':
            self.textRect.center = x + x_displace, y + y_displace

    def draw(self):
        self.surface.blit(self.textSurf, self.textRect)
