#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This file shows the basic usage of pySneakyMaze.
It outputs a few visual examples and benchmarks.
"""

import sneakymaze
import time

def visual():
    """Outputs a few visual examples."""

    #Simple2D
    print("Simple2D (79x19)")
    print(repr(sneakymaze.Simple2D((79, 19))) + "\n")

    #Prim2D
    print("Prim2D (79x19)")
    print(repr(sneakymaze.Prim2D((79, 19))) + "\n")

def benchmark():
    """Outputs a few benchmarks."""

    #How much loops
    b_samples = 100
    b_range = range(b_samples)

    #Simple2D
    time1 = time.time()
    for _ in b_range:
        sneakymaze.Simple2D((79, 9))
    time2 = time.time()
    b_s2d_t = (time2 - time1) / b_samples

    #Prim2D
    time1 = time.time()
    for _ in b_range:
        sneakymaze.Prim2D((79, 9))
    time2 = time.time()
    b_p2d_t = (time2 - time1) / b_samples

    #Results
    print("""
Average Benchmarking Results ({s} samples):
Simple2D (79x9): {s2d} seconds
Prim2D   (79x9): {p2d} seconds
""".format(s=b_samples,
           s2d=round(b_s2d_t, 6),
           p2d=round(b_p2d_t, 6)
          ))


if __name__ == "__main__":

    print("pySneakyMaze {}\n".format(sneakymaze.__version__))

    visual()
    benchmark()