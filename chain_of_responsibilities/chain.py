from __future__ import annotations

import enum
from abc import ABC
from abc import abstractmethod

from common.user import Customer


class Handler(ABC):

    @abstractmethod
    def set_next(self, handler: Handler):
        raise NotImplementedError()

    @abstractmethod
    def handle(self, request: OrderStatus):
        raise NotImplementedError()


class StatusHandler(Handler):
    _next_handler: Handler

    def set_next(self, handler):
        self._next_handler = handler
        return handler

    def handle(self, request: OrderStatus):
        if self._next_handler:
            return self._next_handler.handle(request)
        return None


class StatusCreated(StatusHandler):

    def handle(self, request: OrderStatus):
        if request == OrderStatus.CREATED:
            return OrderStatus.CREATED
        return super().handle(request)


class StatusInProgress(StatusHandler):

    def handle(self, request: OrderStatus):
        if request == OrderStatus.IN_PROGRESS:
            return OrderStatus.IN_PROGRESS
        return super().handle(request)


class StatusDelivered(StatusHandler):

    def handle(self, request: OrderStatus):
        if request == OrderStatus.DELIVERED:
            return OrderStatus.DELIVERED
        return super().handle(request)


class OrderStatus(enum.Enum):
    DELIVERED = 'delivered'
    IN_PROGRESS = 'in progress'
    CREATED = 'created'


class Order:
    def __init__(self, user: Customer):
        self.user = user
        self.status = OrderStatus.CREATED

    def get_order_status(self):
        created = StatusCreated()
        in_progress = StatusInProgress()
        delivered = StatusDelivered()

        created.set_next(in_progress).set_next(delivered)

        return created.handle(self.status)
