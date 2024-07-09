#!/usr/bin/env python3
"""executes multiple coroutines"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """sorted multiple delays"""
    delays = []
    completed = []

    for _ in range(n):
        delay = task_wait_random(max_delay)
        delays.append(delay)

    for delay in asyncio.as_completed((delays)):
        complete = await delay
        completed.append(complete)
    return completed
