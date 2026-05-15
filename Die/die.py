from random import randint

class Die:
	"""A class that represents a die"""

	def __init__(self, num_sides):
		"""Assume the die has 6 faces"""
		self.num_sides = num_sides

	def roll(self):
		"""Returns a random value between 1 and the number of faces"""
		return randint(1, self.num_sides)