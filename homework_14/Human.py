from KiraMogilyuk.Hillel.homework_14.Action import Action


class Human:
    def __init__(self, name: str, age: int, action_name: str):
        self.__name = name
        self.__age = age
        self.__action = Action(action_name)

    @property
    def action(self):
        return self.__action


if __name__ == '__main__':
    john = Human("John", 32, "Dancing")
    print(john.action())

# I have add small modifications to make it works
# 1. Action should be initiated in constructor of Human
# 2. Action should receive 2 arrgument like name
# 3. Method __call__ in Action should return name
# You almost did it but -3 points
