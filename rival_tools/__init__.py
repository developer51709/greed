import asyncio
import functools
import time
from contextlib import asynccontextmanager


def thread(func):
    @functools.wraps(func)
    async def wrapper(*args, **kwargs):
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, functools.partial(func, *args, **kwargs))
    return wrapper


def ratelimit(key=None, limit=1, duration=5, wait=False):
    _cache = {}

    def decorator(func):
        @functools.wraps(func)
        async def wrapper(*args, **kwargs):
            now = time.time()
            k = key if isinstance(key, str) else func.__name__
            if k in _cache:
                calls = [t for t in _cache[k] if now - t < duration]
                if len(calls) >= limit:
                    if wait:
                        await asyncio.sleep(duration - (now - calls[0]))
                    else:
                        return None
                _cache[k] = calls
            else:
                _cache[k] = []
            _cache[k].append(now)
            return await func(*args, **kwargs)
        return wrapper

    if callable(key):
        f = key
        key = f.__name__
        return decorator(f)
    return decorator


@asynccontextmanager
async def lock(key, timeout=10):
    _locks = getattr(lock, '_locks', {})
    lock._locks = _locks
    if key not in _locks:
        _locks[key] = asyncio.Lock()
    try:
        await asyncio.wait_for(_locks[key].acquire(), timeout=timeout)
        yield
    except asyncio.TimeoutError:
        yield
    finally:
        if _locks[key].locked():
            _locks[key].release()


def timeit(func):
    @functools.wraps(func)
    async def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = await func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        return result
    return wrapper
