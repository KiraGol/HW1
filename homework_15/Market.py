from homework_15.products import Apple, Banana, Celery, Strawberry


class Market:
    @staticmethod
    def get_product(name: str):
        if name == "apple":
            return Apple()
        elif name == "banana":
            return Banana()
        elif name == "celery":
            return Celery()
        elif name == "strawberry":
            return Strawberry()
        else:
            raise Exception("Incorrect name of product.")


if __name__ == '__main__':
    print(id(Market.get_product("apple")))
    print(id(Market.get_product("banana")))
    print(id(Market.get_product("celery")))
    print(id(Market.get_product("strawberry")))
