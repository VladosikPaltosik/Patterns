from __future__ import annotations

from abc import ABC
from abc import abstractmethod
from itertools import count

from builder_pattern.product import Laptop


class LaptopDeveloper(ABC):
    @abstractmethod
    def setup_os(self):
        pass

    @abstractmethod
    def add_cpu(self):
        pass


class BaseLaptopDeveloper(LaptopDeveloper):
    _ids = count(1)

    def __init__(self) -> None:
        self._laptop = Laptop()

    def setup_os(self) -> None:
        raise NotImplementedError()

    def add_cpu(self) -> None:
        raise NotImplementedError()

    @property
    def laptop(self) -> Laptop:
        laptop = self._laptop
        laptop.id = next(self._ids)
        self._laptop = Laptop()
        return laptop


class MacbookDeveloper(BaseLaptopDeveloper):
    _ids = count(1)

    def __init__(self) -> None:
        super().__init__()

    def setup_os(self) -> None:
        self._laptop.add('MacOS')

    def add_cpu(self) -> None:
        self._laptop.add('M1')


class DellDeveloper(BaseLaptopDeveloper):
    _ids = count(1)

    def __init__(self) -> None:
        super().__init__()

    def setup_os(self) -> None:
        self._laptop.add('Windows11')

    def add_cpu(self) -> None:
        self._laptop.add('Intel core i7')
