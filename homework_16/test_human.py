import pytest

from homework_16.conftest import human
from homework_16.human import Human


def test_grow_if_alive(human):
    human.grow()

    assert human.age == 26


def test_grow_if_dead(human, monkeypatch):
    monkeypatch.setattr(
        human, "_Human__age", 99
    )
    human.grow()

    assert "dead"


def test_is_alive(human):
    human._Human__is_alive()

    assert True


def test_is_alive_if_dead(human, monkeypatch):
    monkeypatch.setattr(
        human, "_Human__status", "dead"
    )
    with pytest.raises(Exception, match="is already dead..."):
        human._Human__is_alive()


def test_change_gender_from_male(human):
    human.change_gender("female")

    assert human.gender == "female"


def test_change_gender_from_female(human, monkeypatch):
    monkeypatch.setattr(
        human, "_Human__gender", "female"
    )
    human.change_gender("male")

    assert human.gender == "male"


def test_check_raise_of_exception_for_change_gender_if_already_has_gender \
                (human):
    with pytest.raises(Exception, match="already has gender"):
        human.change_gender("male")


def test_check_raise_of_exception_validate_gender(human):
    with pytest.raises(Exception, match="Not correct name of gender"):
        human.change_gender("any")


def test_age(human):
    human.age

    assert human.age == 25


def test_gender(human):
    human.gender

    assert human.gender == "male"
