import pygame
import sys
import random

screen_width = 640
screen_height = 480

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
white = (255, 255, 255)
screen.fill(white)
running = True


clock = pygame.time.Clock()
FPS = 30

rect_x=screen_width/2
rect_y=screen_height/2
rect_width=10
rect_height=10
rect_color1 = (120, 120, 60)
rect_color2 = (60, 120, 200)
rect_color = rect_color1


rect = pygame.Rect((rect_x, rect_y, rect_width, rect_height))
pygame.draw.rect(screen, rect_color, rect)


def main():
    while running:

        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    rect.y = rect.y + rect_height
                if event.key == pygame.K_UP:
                    rect.y = rect.y - rect_height
                if event.key == pygame.K_LEFT:
                    rect.x = rect.x - rect_width
                if event.key == pygame.K_RIGHT:
                    rect.x = rect.x + rect_width

        pygame.draw.rect(screen, rect_color, rect)
        pygame.display.flip()


if __name__ == '__main__':
    main()