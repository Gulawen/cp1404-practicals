from CP1404.prac_08.unreliable_car import UnreliableCar


def test():
    new_car = UnreliableCar("Parker",150, 70)
    print(new_car.drive(100))
    print(new_car.drive(50))

test()
