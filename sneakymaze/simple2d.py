"""
Simple2D - Depth-First-Algorithm
"""

import random

from sneakymaze.prototypes import Maze2DPrototype

class Simple2D(Maze2DPrototype):
    """
    A 2D-Depth-First-Algorithm implementation. Currently the algorithm is
    heavily using recursion. With the default python recursion limit it
    shouldn't go much over 100x100 or else it could fail.
    """

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