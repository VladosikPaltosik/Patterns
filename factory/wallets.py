from abc import ABC
from abc import abstractmethod

from factory.cryptocurrencies import Bitcoin
from factory.cryptocurrencies import Ethereum


class CryptoWallet(ABC):

    @abstractmethod
    def get_cryptocurrency(self):
        pass


class BitcoinWallet(CryptoWallet):
    def get_cryptocurrency(self):
        return Bitcoin(price=10000, coins=1000)


class EthereumWallet(CryptoWallet):
    def get_cryptocurrency(self):
        return Ethereum(price=1000, coins=5000)
