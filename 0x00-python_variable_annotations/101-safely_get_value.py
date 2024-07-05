#!/usr/bin/env python3
""" Mapping """
from typing import TypeVar, Mapping, Any, Union


# Create a type variable for the default value
T = TypeVar('T')


def safely_get_value(
    dct: Mapping,
    key: Any,
    default: Union[T, None] = None
) -> Union[Any, T]:
    """
    Returns the value associated with the given key in the dictionary `dct`.
    If the key is not found, returns the specified default value
    """
    if key in dct:
        return dct[key]
    else:
        return default
