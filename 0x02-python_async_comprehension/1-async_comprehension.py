#!/usr/bin/env python3
"""comprehension that takes no arg"""
import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """coroutine that takes no arg"""
    return [x async for x in async_generator()]
