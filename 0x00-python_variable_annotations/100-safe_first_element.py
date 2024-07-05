#!/usr/bin/env python3
""" Duck typed annotations """
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ Returns the first element of the input, otherwise None"""
    if lst:
        return lst[0]
    else:
        return None
