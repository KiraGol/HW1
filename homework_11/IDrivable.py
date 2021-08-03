from abc import ABC, abstractmethod


class IDrivable(ABC):
    @abstractmethod
    def drive(self):
        pass
