import pygame

pygame.init()


class Settings:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.fps = 60

        self.resolution = self.display_width, self.display_height = 800, 600

        self.white = 255, 255, 255
        self.black = 0, 0, 0
        self.blue = 0, 0, 200

        self.smallFont = pygame.font.SysFont('comicsansms', 25)
        self.largeFont = pygame.font.SysFont('comicsansms', 50)
        
        self.display = pygame.display.set_mode(self.resolution)

        self.progressBarWidth = 25

        self.y_pos_values = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600]
