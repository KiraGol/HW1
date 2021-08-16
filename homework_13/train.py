from typing import List

from homework_13.traincar import TrainCar


class Train:
    def __init__(self):
        self.__train_cars: List[TrainCar] = list()

    def add_train_car(self, train_car: TrainCar):
        self.__train_cars.append(train_car)

    @property
    def __len__(self):
        # you should not return with -1 because train it is something like locomotive already
        return len(self.__train_cars) - 1


if __name__ == '__main__':
    train = Train()
    print(len(train))
    # this will not works since you have made magic method like property
    # always check and test your code
    # -2 points