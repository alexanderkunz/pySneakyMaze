"""
This file contains the basic maze prototypes.
They contain a few useful tools for the child classes.
"""

import math

from sneakymaze.exceptions import InvalidSizeException, EvenException


class Maze2DPrototype(object):
	"""
	The 2D maze prototype.
	"""

	def __init__(self, size, seed=None):

		#Convert Size to Tuple if needed
		if not type(size) in (type(()), type([])):
			if isinstance(type(size), int):
				size = (size, size)
			else:
				raise InvalidSizeException

		#Make sure that the Size is an integer
		size = (int(math.floor(size[0])), int(math.floor(size[1])))

		#Size Checks
		if size[0] % 2 != 1 or size[1] % 2 != 1:
			raise EvenException
		if size[0] < 3 or size[1] < 3:
			raise InvalidSizeException
		self.size = size

		#Start Checks
		self.start = (1, 1)

		#Clear Content
		self.content = None

		#Start Generator
		self.regenerate(seed)

	def __repr__(self):
		return self.string()

	def _is_inside(self, pos):
		"""Checks if a position is inside the array."""
		inside_x = (pos[0] >= 0) and (pos[0] < self.size[0])
		inside_y = (pos[1] >= 0) and (pos[1] < self.size[1])
		return inside_x and inside_y

	def _neighbours(self, pos):
		"""Returns all neighbours of a position."""
		cell = (pos[0], pos[1] + 2)
		if self._is_inside(cell):
			yield cell
		cell = (pos[0], pos[1] - 2)
		if self._is_inside(cell):
			yield cell
		cell = (pos[0] + 2, pos[1])
		if self._is_inside(cell):
			yield cell
		cell = (pos[0] - 2, pos[1])
		if self._is_inside(cell):
			yield cell

	def _neighbours_original(self, pos):
		"""
		Returns all neighbours of a position with the original cell.
		That means, that one neighbour item will look like this:
		(neighbour_x, neighbour_y, original_x, original_y)
		"""
		cell = (pos[0], pos[1] + 2, pos[0], pos[1])
		if self._is_inside(cell):
			yield cell
		cell = (pos[0], pos[1] - 2, pos[0], pos[1])
		if self._is_inside(cell):
			yield cell
		cell = (pos[0] + 2, pos[1], pos[0], pos[1])
		if self._is_inside(cell):
			yield cell
		cell = (pos[0] - 2, pos[1], pos[0], pos[1])
		if self._is_inside(cell):
			yield cell

	def _neighbours_wall(self, pos):
		"""Returns only the neighbours which are a wall (have value 'False')."""
		wall_list = []
		neighbours = self._neighbours(pos)
		for neighbour in neighbours:
			if not self.content[neighbour[0]][neighbour[1]]:
				wall_list.append(neighbour)
		return wall_list

	def _neighbours_wall_original(self, pos):
		"""
		Returns only the neighbours which are a wall (have value 'False').
		Contains the original cell at index 2 and 3.
		"""
		wall_list = []
		neighbours = self._neighbours_original(pos)
		for neighbour in neighbours:
			if not self.content[neighbour[0]][neighbour[1]]:
				wall_list.append(neighbour)
		return wall_list

	def clear(self):
		"""Sets all cells of the array to false."""
		self.content = []
		for _ in range(self.size[0]):
			self.content.append([False for _ in range(self.size[1])])

	def string(self, floor=".", wall="#"):
		"""Returns a string representation of the 2D array."""
		return_str = ""
		for coord_y in range(0, self.size[1]):
			for coord_x in range(0, self.size[0]):
				return_str += floor if self.content[coord_x][coord_y] else wall
			return_str += "\n"
		return return_str

	def is_floor(self, x, y):
		"""Returns True if a specific tile is a floor."""
		if (x < 0) or (y < 0) or (x >= self.size[0]) or (y >= self.size[1]):
			return False
		return self.content[x][y]

	def is_wall(self, x, y):
		"""Returns True if a specific tile is a wall."""
		if (x < 0) or (y < 0) or (x >= self.size[0]) or (y >= self.size[1]):
			return True
		return not self.content[x][y]

	def regenerate(self, seed=None, start=None):
		"""Override! Should create a new maze."""
		pass