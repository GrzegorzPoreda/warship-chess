import pygame, random
from .constants import BLACK, HEIGHT, WIDTH, ROWS, RED, SQUARE_SIZE, COLS, DARK_GREY, DARK_BLUE, WHITE, BORDER_WIDTH, OFFSET, WINNER_FONT, YELLOW, GREEN
from .piece import Piece

pygame.init()
pygame.font.init()

class Board:
	def __init__(self):
		self.board = []
		self.create_board()
    
	def draw_squares(self, win):
		win.fill(BLACK)
		for row in range(ROWS):
			square_color = DARK_GREY
			for col in range(row % 2, COLS, 2):
				if col >= COLS//2:
					square_color = DARK_BLUE
				pygame.draw.rect(win, square_color, (col*SQUARE_SIZE, row*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))				

	def draw_damaged_ship(self, win, row, col):
		pygame.draw.rect(win, RED, (col*SQUARE_SIZE, row*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))				

	def draw_player_ship(self, win, row, col):
		pygame.draw.rect(win, YELLOW, (col*SQUARE_SIZE, row*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))				

	def get_piece(self, row, col):
		return self.board[row][col]

	def create_board(self):
		for row in range(ROWS):
			self.board.append([])
			for col in range(COLS):
				self.board[row].append('water')
		self.randomize_ships()	

	def randomize_ships(self):
		for i in range(5):
			row = random.randint(0, ROWS - 1)
			col = random.randint(OFFSET, COLS - 1)
			while self.board[row][col] == 'player ship':
				row = random.randint(0, ROWS - 1)
				col = random.randint(OFFSET, COLS - 1)
			self.board[row][col] = 'player ship'
		for i in range(5):
			row = random.randint(0, ROWS - 1)
			col = random.randint(0, OFFSET - 1)
			while self.board[row][col] == 'ship':
				row = random.randint(0, ROWS - 1)
				col = random.randint(0, OFFSET - 1)
			self.board[row][col] = 'ship'

	def draw(self, win):
		self.draw_squares(win)
		for row in range(ROWS):
			for col in range(COLS):
				piece = self.board[row][col]
				if not isinstance(piece, str):
					piece.draw(win)
				elif piece == 'damaged ship':
					self.draw_damaged_ship(win, row, col)
				elif piece == 'player ship':
					self.draw_player_ship(win, row, col)
		pygame.draw.rect(win, WHITE, (COLS*SQUARE_SIZE//2 - BORDER_WIDTH//2, 0, BORDER_WIDTH, HEIGHT))

	def add_new_piece(self, row, col, color):
		self.board[row][col] = Piece(row, col, color)

	def add_damaged_ship(self, row, col):
		self.board[row][col] = 'damaged ship'

	def get_winner(self, player):
		if player == 'player':
			for row in range(ROWS):
				for col in range(0, COLS - OFFSET, 1):
					if self.board[row][col] == 'ship':
						return None
			return player
		if player == 'computer':
			for row in range(ROWS):
				for col in range(OFFSET, COLS, 1):
					if self.board[row][col] == 'player ship':
						return None
			return player

	def draw_winner(self, win, winner):
		draw_text = WINNER_FONT.render(winner + ' wins!', 1, GREEN)
		win.blit(draw_text, (WIDTH//2 - draw_text.get_width()//2,
								HEIGHT//2 - draw_text.get_height()/2))
		pygame.display.update()
		pygame.time.delay(2000)