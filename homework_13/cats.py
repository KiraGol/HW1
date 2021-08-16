class Cat:
    def __init__(self):
        self.__name = "Vas'ka"

    def __str__(self):
        return (
            f"{self.__class__.__name__}:{{\n\tname:{self.__name}\n}}"
        )


cat = Cat()
print(cat)
# It will workd but only for 1 field. If I will add more fields you will print still only name.
# Take a look on my last cod ein lesson 13 in examples. You can iterate fields of object using for key, value in self.__dict__.items()
# -2 points
# As alternative it could be done in next way:
# class Cat:
# def __cleaner(self, value: str):
#     return value.partition("__")[2]
#
# def __str__(self):
#     start, content, end = "{\n", "", "}"
#
#     for key, value in self.__dict__.items():
#         content += f"\t{self.__cleaner(key)}: {value}\n"
#
#     return f"{self.__class__.__name__} {start}{content}{end}"
k