from typing import List

from strategy_pattern.exceptions import NotAllValuesAreInteger
from abc import ABC, abstractmethod


class Algorithm(ABC):
    @abstractmethod
    def sort(self, sequences: List[int]) -> List[int]:
        pass


class BubbleSort(Algorithm):
    def sort(self, sequences: List[int]) -> List[int]:
        length = len(sequences)

        for i in range(length):
            for j in range(0, length-i-1):
                if sequences[j] > sequences[j+1]:
                    sequences[j], sequences[j+1] = sequences[j+1], sequences[j]

        return sequences


class QuickSort(Algorithm):
    def sort(self, sequences: List[int]) -> List[int]:
        if len(sequences) <= 1:
            return sequences

        pivot = sequences.pop()
        greater_items = []
        lower_items = []

        for item in sequences:
            if item < pivot:
                lower_items.append(item)
            else:
                greater_items.append(item)

        return self.sort(lower_items) + [pivot] + self.sort(greater_items)


class AlgorithmManager:
    def __init__(self, sequences: List[int], strategy: Algorithm):
        self._sequences = sequences
        self._strategy = strategy

    @property
    def strategy(self):
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Algorithm):
        self._strategy = strategy

    @property
    def sequences(self):
        return self._sequences

    @sequences.setter
    def sequences(self, values: List[int]):
        if not all(isinstance(item, int) for item in values):
            raise NotAllValuesAreInteger()
        self._sequences = values

    def sort(self):
        return self._strategy.sort(self._sequences)
