
import pygame
from constantes import *

class Level(object):
	def __init__(self, structure):
		self.structure = structure

	@classmethod
	def openFile(cls, file):
		with open(file, "r") as file:
			structure = [[car for car in line if car != '\n'] for line in file.readlines()]
		return Level(structure)

	def display(self, window):

		wall = pygame.image.load(WALL).convert_alpha()
		banana = pygame.image.load(BANANA).convert_alpha()
		start = pygame.image.load(START).convert_alpha()
		
		for num_case_y in range(len(self.structure)):
			for num_case_x in range(len(self.structure[0])):
				position_x = num_case_x * WIDTH_SPRITES
				position_y = num_case_y * WIDTH_SPRITES

				if self.structure[num_case_y][num_case_x] == "X":
					window.blit(wall, (position_x, position_y))
				elif self.structure[num_case_y][num_case_x] == "B":
					window.blit(banana, (position_x, position_y))
				elif self.structure[num_case_y][num_case_x] == "D":
					window.blit(start, (position_x, position_y))

class Donkey(object):

	def __init__(self, up, down, left, right, level):
		self.num_x = 0
		self.num_y = 0
		self.UP = pygame.image.load(up).convert_alpha()
		self.DOWN = pygame.image.load(down).convert_alpha()
		self.LEFT = pygame.image.load(left).convert_alpha()
		self.RIGHT = pygame.image.load(right).convert_alpha()
		self.level = level
		self.direction = self.DOWN

	def move(self, direction, window):
		increment = {'up': (0, -1, self.UP),
					'down': (0, 1, self.DOWN),
					'left': (-1, 0, self.LEFT),
					'right': (1, 0, self.RIGHT)}
		new_x = self.num_x+increment[direction][0]
		new_y = self.num_y+increment[direction][1]
		futur_case = self.level.structure[new_y][new_x]
		
		x_in_grid = 0 <= new_x < SPRITES_PER_LINES
		y_in_grid = 0 <= new_y < SPRITES_PER_LINES
		not_wall = futur_case != 'X'

		if x_in_grid and y_in_grid and not_wall:
			self.num_x += increment[direction][0]
			self.num_y += increment[direction][1]
		self.direction = increment[direction][2]
		
		self.level.display(window)
		position_x = self.num_x * WIDTH_SPRITES
		position_y = self.num_y * WIDTH_SPRITES
		window.blit(self.direction, (position_x, position_y))

		if futur_case == 'B':
			return True
