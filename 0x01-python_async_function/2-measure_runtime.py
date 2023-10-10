#!/usr/bin/env python3
"""Measure the runtime
"""
import asyncio
import random
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ measures the total execution time for wait_n(n, max_delay)
    Args:
        n (int):
        max_delay (int):
    Returns: float
    """
    s = time()
    asyncio.run(wait_n(n, max_delay))
    total_time = time() - s
    return total_time / n
