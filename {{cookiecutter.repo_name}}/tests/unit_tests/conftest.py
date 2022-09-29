from typing import Union

from pytest import ExitCode
from pytest import Session

NO_TEST_RAN_CODE = 5
SUCCESS = 0


def pytest_sessionfinish(session: Session, exitstatus: Union[int, ExitCode]) -> None:
    if exitstatus == NO_TEST_RAN_CODE:
        session.exitstatus = SUCCESS
