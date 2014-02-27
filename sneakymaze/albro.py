"""
Aldous-Broder-Algorithm
Good Quality - Very Slow

Imagine a drunken guy running in random directions through the maze. The
generator finishes when he was everywhere. Because of this you shouldn't even
think about big mazes if you want to be still alive when it finally finishes.
"""

import random

from sneakymaze.prototypes import Maze2DPrototype


class AldBro2D(Maze2DPrototype):
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