from homework_11.Car import Car


class Audi(Car):

    def transmission_control(self):
        print("Control by automatic transmission")

    @staticmethod
    def __repair_the_automatic_transmission():
        """returns the way to repair an automatic transmission"""
        print("Give it to a repair service "
              "that repairs automatic transmissions")