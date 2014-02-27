"""
Sidewinder
Poor Quality - Very Fast

A bit slower than the BinTree algorithm, but creates mazes with higher quality.

While it already works, its not finished, because it doesn't have the same
behavior as the standard sidewinder algorithm. I'll fix it when I get the time
and motivation for it.
"""

import random

from sneakymaze.prototypes import Maze2DPrototype


class Sidewinder2D(Maze2DPrototype):
    """
    A 2D-Sidewinder-Algorithm implementation.
    """

    def regenerate(self, seed=None, start=None):
        """
        Generates a new maze.
        """

        #Clear
        self.clear()

        #Variables
        group = []
        rand = random.Random(seed)

        for y in range(1, self.size[1], 2):
            for x in range(1, self.size[0], 2):

                #Variables
                west = False
                north = False

                #First row should be clear
                if y == 1:
                    if x > 1:
                        west = True

                #Decide if group end or not
                else:

                    #Append to group
                    group.append((x, y))

                    if x == self.size[0] - 1 or rand.randint(0, 1):

                        #Give an north passage to a random group item
                        i = group[rand.randint(0, len(group) - 1)]
                        self.content[i[0]][i[1] - 1] = True

                        #Clear group
                        group = []

                    else:

                        #Passage
                        if x > 1:
                            west = True
                        else:
                            north = True

                #Set cell to floor
                self.content[x][y] = True

                #West
                if west:
                    self.content[x - 1][y] = True

                #North
                if north:
                    self.content[x][y - 1] = True

        return True