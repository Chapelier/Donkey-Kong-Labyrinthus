
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
		futur_case = None
		if direction == "up":
			self.direction = self.UP
			try:
				futur_case = self.level.structure[self.num_y-1][self.num_x]
				if futur_case == 'X':
					raise IndexError
			except IndexError:
				pass
			else:
				self.num_y -= 1
		if direction == "down":
			self.direction = self.DOWN
			try:
				futur_case = self.level.structure[self.num_y+1][self.num_x]
				if futur_case == 'X':
					raise IndexError
			except IndexError:
				pass
			else:
				self.num_y += 1
		if direction == "left":
			self.direction = self.LEFT
			try:
				futur_case = self.level.structure[self.num_y][self.num_x-1]
				if futur_case == 'X':
					raise IndexError
			except IndexError:
				pass
			else:
				self.num_x -= 1
		if direction == "right":
			self.direction = self.RIGHT
			try:
				futur_case = self.level.structure[self.num_y][self.num_x+1]
				if futur_case == 'X':
					raise IndexError
			except IndexError:
				pass
			else:
				self.num_x += 1

		self.level.display(window)
		position_x = self.num_x * WIDTH_SPRITES
		position_y = self.num_y * WIDTH_SPRITES
		window.blit(self.direction, (position_x, position_y))

		if futur_case == 'B':
			return True
