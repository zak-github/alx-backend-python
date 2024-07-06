#!/usr/bin/env python3
"""String and int/float to Tuple"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """builds a tuple from string and a number that could be int or float"""
    return (k, v**2)
