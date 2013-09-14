#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

SneakyMaze 1.0

Copyright 2013 Alexander Kunz
Released under the MIT License.

SneakyMaze is a library providing tools for creating infinite/finite
2D and 3D mazes.

"""

import random
import math

class EvenException(Exception):
    """
    EvenException is raised when a position or size is even when
    it shouldn't be.
    """

class Simple2D:
    """
    A 2D-Depth-First algorithm implementation. Currently the algorithm is
    heavily using recursion. With the default python recursion limit it
    shouldn't go much over 100x100 or else it could fail.
    """

    def __init__(self, size, seed = None, start=(1, 1)):

        #Size Checks
        if size[0] % 2 != 1 or size[1] % 2 != 1:
            raise EvenException
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

    def _getvalidneighbours(self, pos, invalid):
        """Returns all valid neighbours of a position."""
        mylist = []
        neighbours = self._getneighbours(pos)
        for neighbour in neighbours:
            if not neighbour in invalid:
                mylist.append(neighbour)
        return mylist

    def _computecell(self, lastcell, cell, visited, rand):
        """Main part of the generation algorithm."""

        #Update Array
        self.content[cell[0]][cell[1]] = True
        self.content[int(math.ceil((cell[0] + lastcell[0]) / 2.0))] \
                    [int(math.ceil((cell[1] + lastcell[1]) / 2.0))] = True

        #Get new Neighbours
        neighbours = self._getvalidneighbours(cell, visited)
        if len(neighbours) <= 0:
            return visited, rand

        #Append Neighbours to Visited
        visited += neighbours

        #Recursively compute each Neighbour
        rand.shuffle(neighbours)
        for neighbour in neighbours:
            visited, rand = self._computecell(cell,
                                              neighbour,
                                              visited,
                                              rand)

        return visited, rand

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
        visited = [self.start]

        visited, rand = self._computecell(self.start, self.start,
                                          visited, rand)

        return True

    def clear(self):
        """Sets all cells of the array to false."""
        self.content = [[False for _ in range(self.size[0])]
                        for _ in range(self.size[1])]

    def getstring(self, floor = ".", wall = "#"):
        """Returns a string representation of the 2D array."""
        mystr = ""
        for ycoord in range(0, self.size[1]):
            for xcoord in range(0, self.size[0]):
                mystr += floor if self.content[xcoord][ycoord] else wall
            mystr += "\n"
        return mystr

if __name__ == "__main__":

    import time

    print("You should import the library instead of running it!")
    print("But to not disappoint you, I'll show you a few fancy examples.")

    T1 = time.time()
    MAZE1 = Simple2D((79, 79), None, (1, 1))
    T2 = time.time()
    print("Time to generate Simple2D (79x79): {} seconds.".format(
          str(round(T2 - T1, 5))
          ))

    print(MAZE1)