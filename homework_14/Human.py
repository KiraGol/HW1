from homework_14.Action import Action


class Human:
    def __init__(self, name: str, age: int):
        self.__name = name
        self.__age = age
        self.__action = Action

    @property
    def action(self):
        return self.__action


if __name__ == '__main__':
    john = Human
    action = Action
    print(action())






