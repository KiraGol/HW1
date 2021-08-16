from KiraMogilyuk.Hillel.homework_15.singleton_task.singleton import singleton


@singleton
class Dog:
    def __init__(self, name: str, breed: str):
        self.__name = name
        self.__breed = breed


if __name__ == '__main__':
    scooter_1 = Dog("Bobby", "husky")
    scooter_2 = Dog("Red", "some")
    # dogs with names scooter 1 and 2 looks strange)
    # next time will reduce points for copy paste
    print()
