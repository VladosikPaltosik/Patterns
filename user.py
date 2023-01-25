class Customer:
    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        return f'Name: {self.name}'


class CryptoCustomer(Customer):
    def __init__(self, name: str, money: float):
        super().__init__(name=name)
        self.money = money
        self.coins_sum = 0

    def __repr__(self):
        return f'Name: {self.name}\nCoins: {self.coins_sum}\nMoney: {self.money}'
