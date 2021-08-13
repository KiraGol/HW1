from typing import List

from homework_13.traincar import TrainCar


class Train:
    def __init__(self):
        self.__train_cars: List[TrainCar] = list()

    def add_train_car(self, train_car: TrainCar):
        self.__train_cars.append(train_car)

    @property
    def __len__(self):
        return len(self.__train_cars) - 1
