class TrainCar:
    def __init__(self, number: int):
        self.__number = number
        self.__passengers = list()

    def add_passenger(self, passenger: str):
        return self.__passengers.append(passenger)

    @property
    def __len__(self):
        return len(self.__passengers)

    @property
    def __str__(self):
        return f"[{self.__number}]"


if __name__ == '__main__':
    train_car = TrainCar(1)
    train_car.add_passenger("John Dow")
    # print(len(train_car))
    # print(train_car)
    # it is not works since you have made both bagic methods like property -2 points

