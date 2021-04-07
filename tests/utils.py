"""This module provides testing utility features."""
import datetime
import random
import string
import time
from typing import Any, Dict, Tuple

import pytz


def random_boolean() -> bool:
    """Get a psuedo-random boolean.

    Don't use this function for security/cryptographic purposes.
    """
    return random.choice([True, False])  # nosa: S311


def random_string(length: int) -> str:
    """Get a random string of n length.
    Args:
        length (int): length
    Returns:
        str:
    """

    return "".join(random.choice(string.ascii_letters) for _ in range(length))


def raise_for_status(func):
    """Decorator that raises a status upon error.

    Returns: the decorated function.
    """

    def wrapper(*args, **kwargs) -> Tuple[Dict[str, Any], int]:
        print(f"Called wrapper with function: '{func.__name__}'.")
        response = func(*args, **kwargs)
        print(f"response saved, status code: {response.status_code}")
        if response.status_code == 422:
            print(response.json()["detail"])
        response.raise_for_status()
        return response.json(), response.status_code

    return wrapper


def time_it(func):
    """Decorator to time function calls.

    TODO(Replace with the one from functools)
    """

    def wrapper(*args, **kwargs):
        started = time.time()
        result = func(*args, **kwargs)
        elapsed_seconds = time.time() - started
        elapsed_ms = round(elapsed_seconds * 1000)
        print(f"{func.__name__} took {elapsed_ms} ms to execute.")
        assert elapsed_ms < 200
        return result

    return wrapper


def random_int(n: int = 0, m: int = 1000):
    """Get a psuedo-random integer.

    Args:
        n (int): minimum value
        m (int): maximum value

    Returns: integer
    """
    return random.randrange(start=n, stop=m)


def random_datetime(start_year: int, end_year: int):
    """Get a psuedo-random datetime containing timezone.

    Args:
        start_year (int): bla bla
        end_year (int): bla bla

    Returns: datetime
    """
    year = random_int(n=start_year, m=end_year)
    month = random_int(n=1, m=12)
    day = random_int(n=1, m=29)
    hour = random_int(n=0, m=23)
    minute = random_int(n=1, m=59)
    tzinfo = pytz.timezone("Europe/Copenhagen")
    return datetime.datetime(
        year=year,
        month=month,
        day=day,
        hour=hour,
        minute=minute,
        tzinfo=tzinfo,
    )


def random_date(start_year: int, end_year: int):
    """Get a psuedo-random date.

    Args:
        start_year (int): bla bla
        end_year (int): bla bla

    Returns: date
    """
    return random_datetime(start_year=start_year, end_year=end_year).date()


def no_state_change(new_data: Dict[str, Any], old_data: Dict[str, Any]) -> None:
    """Check if two data models are relatively similiar.

    Args:
        new_data (Dict[str, Any]): bla bla
        old_data (Dict[str, Any]): bla bla
    """
    for key, item_value in old_data.items():
        # Timezones can be different, but could still be correct:
        try:
            model_dt = datetime.datetime.fromisoformat(item_value)
            data_dt = datetime.datetime.fromisoformat(new_data[key])
            assert model_dt == data_dt  # noqa: S101
        except TypeError:
            assert item_value == new_data[key]  # noqa: S101
        except ValueError:
            continue
