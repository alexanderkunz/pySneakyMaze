"""
Rather small and/or useless algorithms implemented just for fun/completeness.
They can be useless because they are taking too long or don't generate
nice mazes. You still can use them if you find them useful, though.
"""

import random
from prototypes import Maze2DPrototype

class AldBro2D(Maze2DPrototype):
    """
    Aldous-Broder Algorithm. Takes ages. Imagine a drunken guy running
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
        if start != None:
            self.start = start

        #Variables
        rand = random.Random(seed)
        visited = 1
        shouldvisit = (self.size[0] - 1) * (self.size[1] - 1) / 4
        lastpos = list(self.start[:])
        curpos = list(self.start[:])

        #While still some cells left
        while visited < shouldvisit:

            #If not yet floor
            if self.content[curpos[0]][curpos[1]] == False:

                #Increase Visited
                visited += 1

                #Make cell and passage floor
                self.content[curpos[0]][curpos[1]] = True
                self.content[(curpos[0] + lastpos[0]) / 2] \
                            [(curpos[1] + lastpos[1]) / 2] = True

            #Random Move
            lastpos = curpos[:]
            rand1 = rand.randint(0, 1) #Plus or Minus
            rand2 = rand.randint(0, 1) #X or Y
            if rand1:
                if rand2:
                    if curpos[0] + 2 < self.size[0]:
                        curpos[0] += 2
                else:
                    if curpos[1] + 2 < self.size[1]:
                        curpos[1] += 2
            else:
                if rand2:
                    if curpos[0] - 2 > 0:
                        curpos[0] -= 2
                else:
                    if curpos[1] - 2 > 0:
                        curpos[1] -= 2

        return True