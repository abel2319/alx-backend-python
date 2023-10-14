#!/usr/bin/env python3
"""Async Generator
"""
import asyncio
import random
from typing import Generator, Any


async def async_generator() -> Generator[float, None, None]:
    """Caroutine
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
