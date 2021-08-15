from __future__ import annotations

from homework_15.singleton import singleton


@singleton
class Dog:
    def __init__(self, name: str, breed: str):
        self.__name = name
        self.__breed = breed


if __name__ == '__main__':
    scooter_1 = Dog("Bobby", "husky")
    scooter_2 = Dog("Red", "some")
    print()
