import pygame

pygame.init()
pygame.font.init()

# strings used: player, computer, water, ship, player ship, damaged ship

WIDTH, HEIGHT = 800, 400
ROWS, COLS = 10, 20
OFFSET = ROWS
SQUARE_SIZE = WIDTH//COLS
BORDER_WIDTH = 5

WINNER_FONT = pygame.font.SysFont('comicsans', 60)

# rgb
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
DARK_BLUE = (0, 0, 153)
GREY = (128,128,128)
DARK_GREY = (64, 64, 64)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)