from abc import ABC, abstractmethod

from homework_11.IMoveable import IMoveable
from homework_11.IDrivable import IDrivable


class Car(IMoveable, IDrivable, ABC):
    def move(self):
        """returns the way the car moved"""
        print("The car is moved using wheels")

    def drive(self):
        """returns the way the car driven"""
        print("The car is driven by the engine")

    @abstractmethod
    def transmission_control(self):
        """control by means of manual, automatic, hybrid transmission"""
        pass

