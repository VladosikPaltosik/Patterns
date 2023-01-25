class Laptop:
    def __init__(self) -> None:
        self.id = None
        self._parts = []

    def add(self, part: str) -> None:
        self._parts.append(part)

    def __str__(self) -> str:
        return f'{self.id}, {self._parts}'
