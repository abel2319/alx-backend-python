#!/usr/bin/env python3
""" Module for summing up a list """
from typing import List

def sum_list(input_list: List[float]) -> float:
    """ Sum the list of floats
    Agrs:
        input_list: [float]
    Return: sum as a float.
    """
    return sum(input_list)
