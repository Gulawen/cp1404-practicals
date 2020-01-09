from CP1404.prac_08.taxi import Taxi


def test():
    new_taxi = Taxi("Prius 1", 100)
    new_taxi.drive(40)
    print(new_taxi)
    print("Fare:${:.2f}".format(new_taxi.get_fare()))

    new_taxi.start_fare()

    new_taxi.drive(100)
    print(new_taxi)
    print("Fare:${:.2f}".format(new_taxi.get_fare()))


test()
