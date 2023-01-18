from taxi import Taxi


def main():
    print("Create a new taxi object")
    new_taxi = Taxi("Prius 1", 100)
    print("Drive taxi 40km")
    new_taxi.drive(40)
    print(new_taxi)
    print("Restart the meter")
    new_taxi.start_fare()
    print("Drive taxi 100km")
    new_taxi.drive(100)
    print(new_taxi)


main()
