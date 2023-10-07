#!/usr/bin/env python3
""" Complex types - functions"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Returns a function that multiplies a float by multiplier.
    Agrs:
        k: string
        v: [float/integer]
    Return: (k, v**2).
    """
    def f(n: float) -> float:
        """ callable function to multiply """
        return float(n * multiplier)

    return f
