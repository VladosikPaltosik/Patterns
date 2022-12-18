from threading import Lock


class SingletonMeta(type):
    _instances = {}
    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                cls._instances[cls] = super().__call__(*args, **kwargs)
            return cls._instances[cls]


class Queue(metaclass=SingletonMeta):

    def __init__(self):
        self.items = []

    def dequeue(self):
        self.items.pop()

    def enqueue(self, element):
        self.items.insert(0, element)

    def show(self):
        return self.items
