from builder_pattern.builders import DellDeveloper
from builder_pattern.builders import MacbookDeveloper
from builder_pattern.director import Director


def client_code():
    director = Director()
    mac_developer = MacbookDeveloper()
    director.builder = mac_developer

    director.create()
    first_mac = mac_developer.laptop
    print(first_mac)

    director.create()
    second_mac = mac_developer.laptop
    print(second_mac)

    dell_developer = DellDeveloper()
    director.builder = dell_developer
    director.create()

    first_dell = dell_developer.laptop
    print(first_dell)


if __name__ == '__main__':
    client_code()
