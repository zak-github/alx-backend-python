#!/usr/bin/env python3
"""Multiplier module"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """creates a function that can be used as a multiplier"""

    def multiplier_func(num: float) -> float:
        """multiplies a number with the cached multiplier number"""
        return num * multiplier

    return multiplier_func
