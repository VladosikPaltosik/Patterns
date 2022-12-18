from singelton.queue_implementation import Queue


def client_code():
    users = ['Andrew', 'James', 'Lebron', 'Jordan']

    queue_1 = Queue()
    queue_1.enqueue(users[0])
    # Expected: [Andrew]
    print(queue_1.show())

    queue_2 = Queue()
    queue_2.enqueue(users[1])
    # Expected: [James, Andrew]
    print(queue_2.show())

    queue_3 = Queue()
    queue_3.enqueue(users[2])
    queue_3.dequeue()
    # Expected: [Lebron, James]
    print(queue_3.show())


if __name__ == '__main__':
    client_code()
