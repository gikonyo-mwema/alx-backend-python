#!/usr/bin/env python3
"""executes multiple coroutines"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """sorted multiple delays"""
    delays = []
    completed = []

    for _ in range(n):
        delay = wait_random(max_delay)
        delays.append(delay)

    for delay in asyncio.as_completed((delays)):
        complete = await delay
        completed.append(complete)
    return completed
