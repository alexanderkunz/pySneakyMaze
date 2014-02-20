"""
Rather small and/or useless algorithms implemented just for fun/completeness.
They can be useless because they are taking too long or don't generate
nice mazes. You still can use them if you find them useful, though.
"""

import random
from sneakymaze.prototypes import Maze2DPrototype


class AldBro2D(Maze2DPrototype):
	"""
	Aldous-Broder-Algorithm. Takes ages. Imagine a drunken guy running
	in random directions through the maze. Finishes when he was everywhere.
	"""

	def regenerate(self, seed=None, start=None):
		"""
		Generates a new maze. Be careful, this is already done in the
		constructor, so only call this if you want a second maze.
		"""

		#Clear
		self.clear()

		#Check Start
		if start:
			self.start = start

		#Variables
		rand = random.Random(seed)
		visited = 1
		should_visit = (self.size[0] - 1) * (self.size[1] - 1) / 4
		pos_last = list(self.start[:])
		pos_cur = list(self.start[:])

		#While still some cells left
		while visited < should_visit:

			#If not yet floor
			if not self.content[pos_cur[0]][pos_cur[1]]:

				#Increase Visited
				visited += 1

				#Make cell and passage floor
				passage_x = (pos_cur[0] + pos_last[0]) // 2
				passage_y = (pos_cur[1] + pos_last[1]) // 2
				self.content[pos_cur[0]][pos_cur[1]] = True
				self.content[passage_x][passage_y] = True

			#Random Move
			pos_last = pos_cur[:]
			rand1 = rand.randint(0, 1)  # Plus or Minus
			rand2 = rand.randint(0, 1)  # X or Y
			if rand1:
				if rand2:
					if pos_cur[0] + 2 < self.size[0]:
						pos_cur[0] += 2
				else:
					if pos_cur[1] + 2 < self.size[1]:
						pos_cur[1] += 2
			else:
				if rand2:
					if pos_cur[0] - 2 > 0:
						pos_cur[0] -= 2
				else:
					if pos_cur[1] - 2 > 0:
						pos_cur[1] -= 2

		return True


class BinTree2D(Maze2DPrototype):
	"""
	Binary-Tree Algorithm. Very fast, but not very nice output.
	"""

	def regenerate(self, seed=None, start=None):
		"""
		Generates a new maze. Be careful, this is already done in the
		constructor, so only call this if you want a second maze.
		Currently ignores the start, default direction is northwest.
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