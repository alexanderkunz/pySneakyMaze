"""
Prim2D - Randomized Version of the Prim-Algorithm
High Quality - Average Speed
Because the algorithm works without using recursion, it should be able to compute much bigger mazes
than those ones who do (for example Simple2D).
This algorithm should probably be your best choice if you want to generate high quality mazes of any size.
"""

import random

from sneakymaze.prototypes import Maze2DPrototype


class Prim2D(Maze2DPrototype):
	"""
	The 2D implementation.
	"""

	def regenerate(self, seed=None, start=None):
		"""
		Generates a new maze.
		"""

		#Clear
		self.clear()

		#Check Start
		if start:
			self.start = start

		#Repeat start for original cell
		if len(self.start) == 2:
			self.start += self.start

		#Variables
		rand = random.Random(seed)
		active = [self.start]

		while len(active):

			#Here you can put some stuff like
			#print(self)
			#to visualize each step of the algorithm.
			#Attention with running the example then, it includes the benchmarks
			#with many generations, so you would just spam your terminal.

			#Get random item and remove it from list
			index = rand.randint(0, len(active) - 1)
			cell = active[index]
			active.pop(index)

			#Ignore if already floor
			if not self.content[cell[0]][cell[1]]:

				#Make cell and passage floor with use of original cell
				passage_x = (cell[0] + cell[2]) // 2
				passage_y = (cell[1] + cell[3]) // 2
				self.content[cell[0]][cell[1]] = True
				self.content[passage_x][passage_y] = True

				#Add neighbours
				active += self._neighbours_wall_original(cell)

		return True