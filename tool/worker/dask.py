import asyncio
import os
from typing import Callable
from loguru import logger

GLOBAL_DASK = {}


class FakeClient:
    def __init__(self):
        self.status = "running"

    async def close(self):
        self.status = "closed"

    def submit(self, func, pure=False):
        return func()

    def write_scheduler_file(self, path):
        pass


def get_dask():
    client = GLOBAL_DASK.get("client")
    if client is not None and client.status not in ("closed", "closing"):
        return client
    return None


async def start_dask(bot, address: str):
    client = get_dask()
    if client is not None:
        return client
    client = FakeClient()
    GLOBAL_DASK["client"] = client
    logger.info("Dask stub client started (running locally)")
    return client


def submit_coroutine(func: Callable, *args, **kwargs):
    loop = asyncio.get_event_loop()
    task = asyncio.run_coroutine_threadsafe(func(*args, **kwargs), loop=loop)
    return task.result()
