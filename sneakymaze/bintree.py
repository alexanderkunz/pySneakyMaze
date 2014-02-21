"""
Binary-Tree Algorithm
Very Poor Quality - Very Fast
"""

import random
from sneakymaze.prototypes import Maze2DPrototype


class BinTree2D(Maze2DPrototype):
	"""
	The 2D implementation.
	"""

	def regenerate(self, seed=None, start=None):
		"""
		Generates a new maze.
		"""

		#Clear
		self.clear()

		#Variables
		rand = random.Random(seed)

		#For every cell from left upper corner
		for cur_x in range(1, self.size[0], 2):
			for cur_y in range(1, self.size[1], 2):

				#First row has to be floor
				if cur_y == 1:
					west = cur_x > 1
					north = False

				#On second row and further
				else:
					if cur_x > 1 and rand.randint(0, 1):
						west = True
						north = False
					else:
						west = False
						north = True

				#Set cell to floor
				self.content[cur_x][cur_y] = True

				#West
				if west:
					self.content[cur_x - 1][cur_y] = True

				#North
				if north:
					self.content[cur_x][cur_y - 1] = True

		return True