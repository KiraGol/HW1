import pytest as pytest

from homework_16.human import Human


@pytest.fixture
def human() -> Human:
    yield Human("John", 25, "male")
