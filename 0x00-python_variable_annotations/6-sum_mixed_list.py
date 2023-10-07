#!/usr/bin/env python3
""" Module for summing up a list """
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ Sum the list of floats and integers
    Agrs:
        input_list: [float]
    Return: sum as a float.
    """
    return float(sum(mxd_lst))
