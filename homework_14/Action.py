class Action:
    def __init__(self):
        self.__name = "speak"

    def __call__(self):
        print(f"{self.__name}")

