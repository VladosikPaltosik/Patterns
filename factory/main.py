from common.user import CryptoCustomer
from factory.wallets import BitcoinWallet, EthereumWallet


def client_code():
    user_1 = CryptoCustomer(money=100000, name='Vlad')
    user_2 = CryptoCustomer(money=50000, name='Ilya')

    bitcoin_wallet = BitcoinWallet()
    ethereum_wallet = EthereumWallet()

    bitcoin = bitcoin_wallet.get_cryptocurrency()
    ethereum = ethereum_wallet.get_cryptocurrency()

    bitcoin.buy_crypto(user=user_1, coins=2)
    ethereum.buy_crypto(user=user_1, coins=3)

    ethereum.buy_crypto(user=user_2, coins=1)

    print(f'BTC: {bitcoin.coins}')
    print(f'ETC: {ethereum.coins}')

    print(user_1)
    print(user_2)


if __name__ == '__main__':
    client_code()
