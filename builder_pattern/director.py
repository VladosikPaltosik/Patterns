from builder_pattern.builders import LaptopDeveloper


class Director:
    def __init__(self, builder: LaptopDeveloper = None) -> None:
        self._builder = builder

    @property
    def builder(self) -> LaptopDeveloper:
        return self._builder

    @builder.setter
    def builder(self, new_builder: LaptopDeveloper) -> None:
        self._builder = new_builder

    def create(self) -> None:
        self._builder.add_cpu()
        self._builder.setup_os()
