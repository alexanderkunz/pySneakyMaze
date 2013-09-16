"""
Prim2D - Randomized Version of Prim's Algorithm
"""

import random

from sneakymaze.prototypes import Maze2DPrototype

class Prim2D(Maze2DPrototype):
    """
    A randomized 2D-Prim's-Algorithm implementation. Since this one is not
    using recursion, it should be able to compute much bigger mazes
    than Simple2D.
    """

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
                self.content[cell[0]][cell[1]] = True
                self.content[(cell[0] + cell[2]) / 2] \
                            [(cell[1] + cell[3]) / 2] = True

                #Add neighbours
                active += self._getwallneighbours_withorig(cell)

        return True