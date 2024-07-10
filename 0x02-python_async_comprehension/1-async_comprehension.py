#!/usr/bin/env python3
""" Coroutine with no arguments """
async_generator = __import__('1-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    coroutine will collect 10 random numbers using an async
    comprehensing over async_generator,
    then return the 10 random numbers.

    """
    return [x async for x in async_generator()]
