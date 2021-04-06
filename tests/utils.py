from typing import Tuple, Dict, Any
import random
import string
import time
import datetime
import pytz


def random_boolean() -> bool:
    return random.choice([True, False])


def random_string(length: int) -> str:
    """Get a random string of n length.
    Args:
        length (int): length
    Returns:
        str:
            """

    return ''.join(random.choice(string.ascii_letters) for _ in range(length))


def raise_for_status(func):

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
    return random.randrange(start=n, stop=m)


def random_datetime(start_year: int, end_year: int):
    year = random_int(n=start_year, m=end_year)
    month = random_int(n=1, m=12)
    day = random_int(n=1, m=29)
    hour = random_int(n=0, m=23)
    minute = random_int(n=1, m=59)
    tzinfo = pytz.timezone('Europe/Copenhagen')
    return datetime.datetime(year=year, month=month, day=day, hour=hour,
                             minute=minute, tzinfo=tzinfo)


def random_date(start_year: int, end_year: int):
    return random_datetime(start_year=start_year, end_year=end_year).date()

def no_state_change(data: Dict[str, Any],
                    model: Dict[str, Any]) -> None:
    for key, val in model.items():
        try:
            # Timezones can be different, but could still be correct:
            model_dt = datetime.datetime.fromisoformat(val)
            data_dt = datetime.datetime.fromisoformat(data[key])
            assert model_dt == data_dt
        except TypeError:
            assert val == data[key]
        except ValueError:
            continue

