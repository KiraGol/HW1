from .Car import Car


class Toyota(Car):
    def __init__(self, model: str, color: str):
        self.__model = model
        self.__color = color

    @property
    def model(self):
        return self.__model

    @property
    def color(self):
        return self.__color

    def transmission_control(self):
        print("Control by manual transmission")

    @staticmethod
    def __repair_the_manual_transmission():
        """returns the way to repair an automatic transmission"""
        print("Give it to a repair service "
              "that repairs manual transmissions")

# Good but I want to see implementing of same method in Audi and Toyotan in different ways
# -4 points
