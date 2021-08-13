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



