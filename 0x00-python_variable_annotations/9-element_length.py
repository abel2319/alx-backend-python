#!/usr/bin/env python3
""" Module for annatation"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ function to annotate"""
    return [(i, len(i)) for i in lst]
