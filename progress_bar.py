import pygame
import time
from settings import Settings

pygame.init()

s = Settings()


class ProgressBar:
    # x and y are temporary testing variables. when done, remove ALL code involving the two. Pos is a set of defined y positions.
    def __init__(self, length, color, pos):
        displayRect = s.display.get_rect()

        # self.position = position
        self.leftPos = 200
        self.topPos = s.y_pos_values[pos-1]

        self.color = color
        self.length = length

        # surf and rect are set here.
        self.surf = pygame.Surface((self.length, s.progressBarWidth))
        self.rect = self.surf.get_rect()
        self.rect.topleft = self.leftPos, self.topPos

        self.maxLength = s.display_width-self.rect.left

    # Update length of progress bar
    def update(self, length_change):
        # length change less than one, bar length greater than one
        if length_change <= 0 < self.length:
            self.length += length_change
        # length change greater than one, bar length less than max length
        if length_change >= 1 and self.length < self.maxLength:
            self.length += length_change

        # surf and rect are set here again.
        self.surf = pygame.Surface((self.length, s.progressBarWidth))
        self.rect = self.surf.get_rect()
        self.rect.topleft = self.leftPos, self.topPos

    # Decay of progress bar over time
    def decay(self):
        pass

    # Draw the bar with current values
    def draw(self):
        self.surf.fill(self.color)
        s.display.blit(self.surf, self.rect)
