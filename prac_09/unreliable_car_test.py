from unreliable_car import UnreliableCar


def main():
    """Test some UnreliableCars."""

    good_car = UnreliableCar("good", 100, 90)
    bad_car = UnreliableCar("bad", 100, 9)

    for i in range(1, 12):
        print(f"Driving {i}km:")
        print(f"{good_car.name:12} drove {good_car.drive(i):2}km")
        print(f"{bad_car.name:12} drove {bad_car.drive(i):2}km")

    # print the final states of the cars
    print(good_car)
    print(bad_car)


main()
