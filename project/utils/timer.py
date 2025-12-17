# project/utils/timer.py
import time
from contextlib import contextmanager

def now() -> float:
    """High-resolution timestamp (seconds)."""
    return time.perf_counter()

@contextmanager
def timer():
    """Context manager that yields a start time and sets elapsed on exit."""
    start = now()
    yield lambda: now() - start
