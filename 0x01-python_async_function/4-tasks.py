#!/usr/bin/env python3
"""Tasks
"""
import asyncio


task_wait_random = __import__('3-tasks').task_wait_random


def task_wait_n(max_delay: int) -> asyncio.Task:
    """create async task
    Args:
        max_delay (int): max dalay number
    Returns: asyncio.Task
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]
