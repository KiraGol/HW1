from homework_12.CurrentAccount import CurrentAccount


class HRNAcc(CurrentAccount):
    def __init__(
            self,
            customer_name: str,
            account_number: int,
            currency: str,
            income: int,
            costs: int,
            account_balance: int = None
    ):
        super().__init__(customer_name, account_number, currency, income,
                         costs, account_balance)

    @property
    def account_currency(self) -> str:
        return self.currency

    @property
    def __salary_crediting(self):
        """crediting the salary to the account"""
        return self.income + 100
