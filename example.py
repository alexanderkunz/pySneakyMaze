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

    #AldBro2D
    print("AldBro2D (79x19)")
    print(repr(sneakymaze.AldBro2D((79, 19))) + "\n")

def benchmark_func(samples, func, *args):
    srange = range(samples)
    time1 = time.time()
    for _ in srange:
        func(*args)
    time2 = time.time()
    return (time2 - time1) / samples

def benchmark():
    """Outputs a few benchmarks."""

    #How much loops
    samples = 100

    print("Average Benchmarking Results ({s} samples):".format(s=samples))

    #Simple2D
    s2d_t = benchmark_func(samples, sneakymaze.Simple2D, (79, 9))
    print("Simple2D (79x9): {t}s".format(t=round(s2d_t, 6)))

    #Prim2D
    p2d_t = benchmark_func(samples, sneakymaze.Prim2D, (79, 9))
    print("Prim2D (79x9): {t}s".format(t=round(p2d_t, 6)))

    #AldBro2D
    ab2d_t = benchmark_func(samples, sneakymaze.AldBro2D, (79, 9))
    print("AlBro2D (79x9): {t}s".format(t=round(ab2d_t, 6)))


if __name__ == "__main__":

    print("pySneakyMaze {}\n".format(sneakymaze.__version__))

    visual()
    benchmark()