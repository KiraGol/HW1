from typing import Type


def singleton(_class):
    def inner(*args):
        name = f"_{_class.__name__}__instance"

        if not hasattr(_class, name):
            setattr(_class, name, _class(*args))
        return getattr(_class, name)

    return inner

# Good but in your solution private attribute was not present but public with name NoneType was so -5 points
# Take a look on proper solution
