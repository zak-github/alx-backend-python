#!/usr/bin/env python3
"""1st Element of a Sequence"""
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """function that returns the first element of a Sequence"""
    if lst:
        return lst[0]
    else:
        return None
