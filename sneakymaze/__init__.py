#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
A python library for generating two dimensional mazes. Mazes are saved in
boolean arrays to mark wall (False) or floor (True). Several algorithms
are implemented, each with its own pros and cons. The faster ones usually
have a lower quality than the slower ones. Lower quality means, that the
mazes are more biased. A good start for generating high quality mazes is
the Prim2D-Algorithm, which has a very good quality-performance ratio.
"""

__author__ = "Alexander Kunz"
__email__ = "alexanderkunz@hotmail.de"
__license__ = "MIT"
__version__ = "1.0"

from sneakymaze.simple import Simple2D
from sneakymaze.prim import Prim2D
from sneakymaze.sidewinder import Sidewinder2D
from sneakymaze.albro import AldBro2D
from sneakymaze.bintree import BinTree2D