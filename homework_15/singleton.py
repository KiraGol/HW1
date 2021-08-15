from typing import Type


def singleton(_class: Type):
    def inner(*args):
        instance = None
        if not hasattr(_class, instance.__class__.__name__):
            setattr(_class, instance.__class__.__name__, _class(*args))
        return getattr(_class, instance.__class__.__name__)

    return inner
