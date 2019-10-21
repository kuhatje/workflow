import pygame
from progress_bar import ProgressBar
from settings import Settings
from text import Text

s = Settings()
pygame.init()


# Set text objects
test = Text('Hello', s.display_width/2, s.display_height/2)



bars = []
for y_pos in s.y_pos_values:
    bars.append(ProgressBar(150, s.black, 1))

# test_bar_for_text_rect = ProgressBar(150, s.blue, 0, 50)

# bars = [bar1, bar2, bar3, bar4, test_bar_for_text_rect]


def game_loop():
    s.display.fill(s.white)

    pygame.display.update()
    length_change = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                if event.key == pygame.K_LEFT:
                    length_change = -1
                if event.key == pygame.K_RIGHT:
                    length_change = 1
            if event.type == pygame.KEYUP:
                length_change = 0

        s.display.fill(s.white)

        # Draw all bars. Update only if length_change is not zero

        for bar in bars:
            if length_change:
                bar.update(length_change)
            bar.draw()
            print(bar.rect.right)

        test.draw()

        pygame.display.update()
        s.clock.tick(60)


game_loop()
pygame.quit()
quit()
