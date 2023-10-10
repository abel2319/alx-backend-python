#!/usr/bin/env python3
"""measure time module
"""
import asyncio
import random
from time import perf_counter

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measures time of async funcs.
    Args:
        n (int): times
        max_delay (int): dalay max number
    Returns: time
    """
    s = perf_counter()
    asyncio.run(wait_n(n, max_delay))
    total_time = perf_counter() - s
    return total_time
