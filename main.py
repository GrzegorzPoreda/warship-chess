import pygame, sys
from warships.constants import WIDTH, HEIGHT, SQUARE_SIZE
from warships.game import Game

pygame.init()
pygame.font.init()

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Warship Chess')

def get_row_col_from_mouse(pos):
	x, y = pos
	row = y // SQUARE_SIZE
	col = x // SQUARE_SIZE
	return row, col

def main():
	clock = pygame.time.Clock()
	game = Game(WIN)

	while True:
		clock.tick(FPS)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()	
            
			if event.type == pygame.MOUSEBUTTONDOWN:
				pos = pygame.mouse.get_pos()
				row, col = get_row_col_from_mouse(pos)
				player_done = game.select(row, col)
				if player_done:
					game.update()	
					if game.get_winner('player') != None:
						game.draw_winner('player')
						main()
					while(not game.computer_turn()):
						continue
					game.update()
					if game.get_winner('computer') != None:
						game.draw_winner('computer')
						main()

		game.update()

if __name__ == '__main__':
	main()