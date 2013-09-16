"""
Simple2D - Depth-First-Algorithm
"""

import math
import random

from sneakymaze.prototypes import Maze2DPrototype
from sneakymaze.exceptions import InvalidSizeException, EvenException

class Simple2D(Maze2DPrototype):
    """
    A 2D-Depth-First-Algorithm implementation. Currently the algorithm is
    heavily using recursion. With the default python recursion limit it
    shouldn't go much over 100x100 or else it could fail.
    """

    def __init__(self, size, seed = None, start=(1, 1)):

        #Init Base Class
        super(Simple2D, self).__init__()

        #Convert Size to Tuple if needed
        if not type(size) in (type(()), type([])):
            if type(size) == type(0):
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
        if start[0] % 2 != 1 or start[1] % 2 != 1:
            raise EvenException
        self.start = start

        #Clear Content
        self.content = None

        #Start Generator
        self.regenerate(seed)

    def _getvalidneighbours(self, pos):
        """Returns all valid neighbours of a position."""
        mylist = []
        neighbours = self._getneighbours(pos)
        for neighbour in neighbours:
            if not self.content[neighbour[0]][neighbour[1]]:
                mylist.append(neighbour)
        return mylist

    def _computecell(self, lastcell, cell, rand):
        """Main part of the generation algorithm."""

        #Update Array
        self.content[(cell[0] + lastcell[0]) / 2] \
                    [(cell[1] + lastcell[1]) / 2] = True

        #Get new Neighbours
        neighbours = self._getvalidneighbours(cell)
        if len(neighbours) <= 0:
            return

        #Add Neighbour to Content
        for neighbour in neighbours:
            self.content[neighbour[0]][neighbour[1]] = True

        #Recursively compute each Neighbour
        rand.shuffle(neighbours)
        for neighbour in neighbours:
            self._computecell(cell, neighbour, rand)

    def regenerate(self, seed=None, start=None):
        """
        Generates a new maze. Be careful, this is already done in the
        constructor, so only call this if you want a second maze.
        """

        #Clear
        self.clear()

        #Check Start
        if start != None:
            self.start = start

        #Variables
        rand = random.Random(seed)

        self.content[self.start[0]][self.start[1]] = True
        self._computecell(self.start, self.start, rand)

        return True