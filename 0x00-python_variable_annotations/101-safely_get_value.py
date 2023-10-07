#!/usr/bin/env python3
""" 11. More involved type annotations """
from typing import Sequence, List, Union, Any, Mapping, TypeVar


T = TypeVar('T')


def safely_get_value(dct: Mapping,
                     key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """ Safety get value """
    if key in dct:
        return dct[key]
    else:
        return default
