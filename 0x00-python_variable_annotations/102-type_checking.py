#!/usr/bin/env python3
""" zoom """
from typing import Tuple, Union

def zoom_array(lst: Tuple, factor: int = 2) -> Tuple:
    """ Zoom Array """
    zoomed_in: Tuple[Union[str, bool]] = [
        item for item in lst
        for i in range(factor)
    ]
    return tuple(zoomed_in)  # Convert the list to a tuple

array = (12, 72, 91)  # Use a tuple instead of a list

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)  # Use an integer value for the factor
