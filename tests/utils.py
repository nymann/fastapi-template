import random
import string
import time


def random_string(length: int) -> str:
    """Get a random string of n length.

    Args:
        length (int): length

    Returns:
        str:
    """
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))


def time_it(func):

    def wrapper(*args, **kwargs):
        started = time.time()
        result = func(*args, **kwargs)
        elapsed_seconds = time.time() - started
        elapsed_ms = round(elapsed_seconds * 1000)
        print(f"{func.__name__} took {elapsed_ms} ms to execute.")
        assert elapsed_ms < 200
        return result

    return wrapper
