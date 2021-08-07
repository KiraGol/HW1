from homework_12.CurrentAccount import CurrentAccount


class USDAcc(CurrentAccount):
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
    def __commission_for_crediting_currency(self):
        """returns the amount of commission for crediting currency"""
        return self.income * 0.02