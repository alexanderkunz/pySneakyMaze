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
    print("Simple2D (79x9)")
    print(sneakymaze.Simple2D((79, 9)))


def benchmark():
    """Outputs a few benchmarks."""

    #How much loops
    b_samples = 100

    #Simple2D
    brange = range(b_samples)
    time1 = time.time()
    for _ in brange:
        sneakymaze.Simple2D((79, 9))
    time2 = time.time()
    b_s2d_t = (time2 - time1) / b_samples

    #Results
    print("""
Average Benchmarking Results ({s} samples):
Simple2D (79x9): {s2d} seconds
""".format(s= b_samples, s2d=round(b_s2d_t, 6)))


if __name__ == "__main__":

    print("pySneakyMaze {}\n".format(sneakymaze.__version__))

    visual()
    benchmark()