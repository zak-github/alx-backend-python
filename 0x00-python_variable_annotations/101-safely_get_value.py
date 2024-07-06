#!/usr/bin/env python3
"""Involved Type Annotations"""
from typing import Any, Mapping, TypeVar, Union


def safely_get_value(
        dct: Mapping,
        key: Any,
        default: Union[TypeVar('T'),
                       None] = None) -> Union[Any, TypeVar('T')]:
    """safely get a value from an Annotation"""
    if key in dct:
        return dct[key]
    else:
        return default
