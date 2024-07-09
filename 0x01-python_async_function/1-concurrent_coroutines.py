#!/usr/bin/env python3
"""
List of all the delays.
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: float) -> List[float]:
    """
    Spawns n wait_random tasks with the specified max_delay.
    Returns a list of delays in ascending order.
    """
    delays = []

    # Spawn n wait_random tasks
    tasks = [wait_random(max_delay) for _ in range(n)]

    # Gather results concurrently
    for delay in asyncio.as_completed(tasks):
        result = await delay
        delays.append(result)

    return delays
