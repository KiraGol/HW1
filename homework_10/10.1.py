class Company:
    def __init__(
            self,
            company_name: str,
            the_number_of_employees: int,
            type_of_activity: str,
            income: int,
            costs: int,
            profit: int = None
    ):
        self.__company_name = company_name
        self.__the_number_of_employees = the_number_of_employees
        self.__type_of_activity = type_of_activity
        self.__income = income
        self.__costs = costs
        self.__profit = profit

    @property
    def profit(self):
        """returns the company's profit"""
        self.__profit: int = self.__income - self.__costs
        return self.__profit

    @staticmethod
    def charity(sum_of_charity) -> str:
        """returns a message indicating the amount to charity"""
        return f"Our company provided assistance " \
               f"in the amount of $ {sum_of_charity}"


if __name__ == '__main__':
    global_logic = Company("Global logic", 215, "IT outsourcing",
                           100000, 30000)
    print(global_logic.profit)
    print(global_logic.charity(100))
