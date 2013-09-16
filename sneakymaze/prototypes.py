"""
This file contains the prototypes needed for the implementations
of the algorithms.
"""

import math
from sneakymaze.exceptions import InvalidSizeException, EvenException

class Maze2DPrototype(object):
    """
    Prototype for 2D mazes with standard functions.
    """

    def __init__(self, size, seed = None, start=(1, 1)):

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

    def __repr__(self):
        return self.getstring()

    def _isinside(self, pos):
        """Checks if a position is inside the array."""
        xinside = pos[0] > 0 and pos[0] < self.size[0]
        yinside = pos[1] > 0 and pos[1] < self.size[1]
        return xinside and yinside

    def _getneighbours(self, pos):
        """Returns all neighbours of a position."""
        cell = (pos[0], pos[1] + 2)
        if self._isinside(cell):
            yield cell
        cell = (pos[0], pos[1] - 2)
        if self._isinside(cell):
            yield cell
        cell = (pos[0] + 2, pos[1])
        if self._isinside(cell):
            yield cell
        cell = (pos[0] - 2, pos[1])
        if self._isinside(cell):
            yield cell

    def _getneighbours_withorig(self, pos):
        """
        Returns all neighbours of a position with the original cell.
        That means, that one neighbour item will look like this:
        (neighbourx, neighboury, originalx, originaly)
        """
        cell = (pos[0], pos[1] + 2, pos[0], pos[1])
        if self._isinside(cell):
            yield cell
        cell = (pos[0], pos[1] - 2, pos[0], pos[1])
        if self._isinside(cell):
            yield cell
        cell = (pos[0] + 2, pos[1], pos[0], pos[1])
        if self._isinside(cell):
            yield cell
        cell = (pos[0] - 2, pos[1], pos[0], pos[1])
        if self._isinside(cell):
            yield cell

    def _getwallneighbours(self, pos):
        """Returns only the neighbours which are a wall (have value 'False')."""
        mylist = []
        neighbours = self._getneighbours(pos)
        for neighbour in neighbours:
            if not self.content[neighbour[0]][neighbour[1]]:
                mylist.append(neighbour)
        return mylist

    def _getwallneighbours_withorig(self, pos):
        """
        Returns only the neighbours wich are a wall (have value 'False').
        Contains the original cell at index 2 and 3.
        """
        mylist = []
        neighbours = self._getneighbours_withorig(pos)
        for neighbour in neighbours:
            if not self.content[neighbour[0]][neighbour[1]]:
                mylist.append(neighbour)
        return mylist

    def clear(self):
        """Sets all cells of the array to false."""
        self.content = [[False for _ in range(self.size[1])]
                        for _ in range(self.size[0])]

    def getstring(self, floor = ".", wall = "#"):
        """Returns a string representation of the 2D array."""
        mystr = ""
        for ycoord in range(0, self.size[1]):
            for xcoord in range(0, self.size[0]):
                mystr += floor if self.content[xcoord][ycoord] else wall
            mystr += "\n"
        return mystr

    def regenerate(self, seed=None, start=None):
        """Override! Should create a new maze."""
        pass