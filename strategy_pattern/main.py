from strategy_pattern.strategy import AlgorithmManager
from strategy_pattern.strategy import QuickSort, BubbleSort


def client_code():
    manager = AlgorithmManager(strategy=QuickSort(), sequences=[4, 8, 3, 2, 9, 1])
    result = manager.sort()
    print(result)

    manager.strategy = BubbleSort()
    manager.sequences = [78, 95, 12, 1, 6, 5, 22]
    result = manager.sort()
    print(result)


if __name__ == '__main__':
    client_code()
