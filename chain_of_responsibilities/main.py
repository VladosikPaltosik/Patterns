from chain_of_responsibilities.chain import Order
from chain_of_responsibilities.chain import OrderStatus
from common.user import Customer


def client_code():
    user = Customer(name='Jenna')
    order = Order(user=user)
    print(order.get_order_status())
    order.status = OrderStatus.IN_PROGRESS
    print(order.get_order_status())
    order.status = OrderStatus.DELIVERED
    print(order.get_order_status())


if __name__ == '__main__':
    client_code()
