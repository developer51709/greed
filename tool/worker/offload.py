from __future__ import annotations

import asyncio
import os
from functools import partial
from typing import Awaitable, Callable, TypeVar, TYPE_CHECKING
from typing_extensions import ParamSpec

from .dask import get_dask, start_dask

if TYPE_CHECKING:
    from tool.greed import Greed


P = ParamSpec("P")
T = TypeVar("T")


def strtobool(val) -> bool:
    if not val:
        return False
    val = str(val)
    val = val.lower()
    if val in {"y", "yes", "t", "true", "on", "1"}:
        return True
    elif val in {"n", "no", "f", "false", "off", "0"}:
        return False
    else:
        msg = f"invalid truth value {val!r}"
        raise ValueError(msg)


DEBUG = strtobool(os.getenv("DEBUG", "OFF"))


def offloaded(f: Callable[P, T], batch_size: int = None) -> Callable[P, Awaitable[T]]:
    async def offloaded_task(*a, **ka):
        loop = asyncio.get_running_loop()

        if batch_size and a and isinstance(a[-1], (list, tuple)):
            data = a[-1]
            other_args = a[:-1]
            batches = [
                data[i : i + batch_size] for i in range(0, len(data), batch_size)
            ]

            async def process_batch(batch):
                args = (*other_args, batch)
                meth = partial(f, *args, **ka)
                return await loop.run_in_executor(None, meth)

            results = await asyncio.gather(*[process_batch(batch) for batch in batches])
            return [item for batch in results for item in batch]

        meth = partial(f, *a, **ka)
        return await loop.run_in_executor(None, meth)

    return offloaded_task
