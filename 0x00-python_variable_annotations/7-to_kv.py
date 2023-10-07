#!/usr/bin/env python3
'''Task 7's module.
'''
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ Tuples from string k and number v
    Agrs:
        k: string
        v: [float/integer]
    Return: (k, v**2).
    """
    return (k, float(v**2))
