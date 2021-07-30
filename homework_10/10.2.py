class Employee:
    def __init__(
            self,
            name: str,
            age: int,
            gender: bool,
            position: str,
            salary: int,
            income_tax: float = None
    ):
        self.__name = name
        self.__age = age
        self.__gender = gender
        self.__position = position
        self.__salary = salary
        self.__income_tax = income_tax

    @property
    def income_tax(self):
        """calculates the amount of income tax."""
        self.__income_tax: float = self.__salary * 0.2
        return self.__income_tax


if __name__ == '__main__':
    john = Employee("John", 30, True, "developer", 100)