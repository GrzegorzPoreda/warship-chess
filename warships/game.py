import pygame, random
from .constants import RED, WHITE, OFFSET, ROWS, COLS
from .board import Board

pygame.init()
pygame.font.init()

class Game:
	def __init__(self, win):
		self.win = win
		self.board = Board()
		self.turn = 'player'
	
	def update(self):
		self.board.draw(self.win)
		pygame.display.update()

	def switch_turns(self):
		if self.turn == 'player':
			self.turn = 'computer'
		else:
			self.turn = 'player'

	def select(self, row, col):
		piece = self.board.get_piece(row, col)
		if self.turn == 'player' and col >= OFFSET:
			return False 
		if piece == 'water':
			self.board.add_new_piece(row, col, WHITE)
			self.switch_turns()
			return True
		elif piece == 'ship':
			self.board.add_new_piece(row, col, RED)
			self.switch_turns()
			return True
		elif piece == 'player ship':
			self.board.add_damaged_ship(row, col)
			self.switch_turns()
			return True
		return False

	def get_winner(self, player):
		return self.board.get_winner(player)

	def computer_turn(self):
		row = random.randint(0, ROWS - 1)
		col = random.randint(OFFSET, COLS - 1)
		if self.select(row, col):
			return True
		return False
		
	def draw_winner(self, winner):
		self.board.draw_winner(self.win, winner)