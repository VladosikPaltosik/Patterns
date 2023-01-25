from abc import ABC
from abc import abstractmethod

from factory.descriptors import PositiveNumber
from common.user import CryptoCustomer


class Crypto(ABC):
    @abstractmethod
    def buy_crypto(self, user: CryptoCustomer, coins: int) -> None:
        pass


class BaseCrypto(Crypto):
    price = PositiveNumber()
    coins = PositiveNumber()

    def __init__(self, price: int, coins: int) -> None:
        self.price = price
        self.coins = coins

    def buy_crypto(self, user: CryptoCustomer, coins: int) -> None:
        self.coins -= coins
        user.coins_sum += coins
        user.money -= self.price


class Bitcoin(BaseCrypto):
    def __init__(self, price: int, coins: int) -> None:
        super().__init__(price=price, coins=coins)


class Ethereum(BaseCrypto):
    def __init__(self, price: int, coins: int) -> None:
        super().__init__(price=price, coins=coins)
