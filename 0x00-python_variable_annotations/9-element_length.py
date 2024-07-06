#!/usr/bin/env python3
"""Element_length module"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """returns a tuple built from a list"""
    return [(i, len(i)) for i in lst]
