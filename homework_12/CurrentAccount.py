from abc import ABC, abstractmethod


class CurrentAccount(ABC):
    def __init__(
            self,
            customer_name: str,
            account_number: int,
            currency: str,
            income: int,
            costs: int,
            account_balance: int = None
    ):
        self.customer_name = customer_name
        self.account_number = account_number
        self.currency = currency
        self.income = income
        self.costs = costs
        self.account_balance = account_balance

    @abstractmethod
    def account_currency(self):
        """returns the currency of the client's account"""
        pass

    @property
    def account_balance(self):
        """returns the client's account balance"""
        self.account_balance: int = self.income - self.costs
        return self.account_balance


