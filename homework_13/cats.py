class Cat:
    def __init__(self):
        self.__name = "Vas'ka"

    def __str__(self):
        return (
            f"{self.__class__.__name__}:{{\n\tname:{self.__name}\n}}"
        )


cat = Cat()
print(cat)


