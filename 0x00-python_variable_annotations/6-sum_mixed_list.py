#!/usr/bin/env python3
""" Mixed list sum """
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ Returns sum fo mixed list as float """
    return float(sum(mxd_lst))
