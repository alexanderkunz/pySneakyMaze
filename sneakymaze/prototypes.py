"""
This file contains the prototypes needed for the implementations
of the algorithms.
"""

class Maze2DPrototype(object):
    """
    Prototype for 2D mazes with standard functions.
    """

    size = None
    content = None

    def __init__(self):
        pass

    def __repr__(self):
        return self.getstring()

    def _isinside(self, pos):
        """Checks if a position is inside the array."""
        xinside = pos[0] > 0 and pos[0] < self.size[0]
        yinside = pos[1] > 0 and pos[1] < self.size[1]
        return xinside and yinside

    def _getneighbours(self, pos):
        """Returns all neighbours of a position."""
        neighbours = []
        cell = (pos[0], pos[1] + 2)
        if self._isinside(cell):
            neighbours.append(cell)
        cell = (pos[0], pos[1] - 2)
        if self._isinside(cell):
            neighbours.append(cell)
        cell = (pos[0] + 2, pos[1])
        if self._isinside(cell):
            neighbours.append(cell)
        cell = (pos[0] - 2, pos[1])
        if self._isinside(cell):
            neighbours.append(cell)
        return neighbours

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