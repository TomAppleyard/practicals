from prac_06.car import Car
from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

MENU = "q - quit, choose - c, drive - d"


def main():
    """Write a taxi simulator program that uses your Taxi and SilverServiceTaxi
    classes. Each time, until they quit:
    The user should be presented with a list of available taxis and get to
    choose one. Then they should say how far they want to drive.
    At the end of each trip, show them the price and add it to their bill.
    """
    total_cost = 0
    taxis = [Taxi("toyota", 90), SilverServiceTaxi("lamborghini", 90, 2),
             SilverServiceTaxi("Hummer", 180, 4)]
    current_taxi = None
    print(MENU)
    menu_choice = input(">>> ").lower()
    while menu_choice != 'q':
        if menu_choice == 'c':
            print("Taxi list: ")
            display(taxis)
            taxi_choice = int(input("Choose taxi: "))
            try:
                current_taxi = taxis[taxi_choice]
            except IndexError:
                print("Invalid choice")
        elif menu_choice == "d":
            if current_taxi:
                current_taxi.start_fare()
                distance_to_drive = float(input("Drive how far? "))
                current_taxi.drive(distance_to_drive)
                trip_cost = current_taxi.get_fare()
                print(f"Your {current_taxi.name} trip cost you ${trip_cost:.2f}")
                total_cost += trip_cost
            else:
                print("Please choose txi")
        else:
            print("Invalid option")
        print(MENU)
        menu_choice = input(">>> ").lower()

    print(f"Total cost: ${total_cost:.2f}")
    display(taxis)


def display(taxis):
    """Display taxi list."""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


def run_tests():
    """Run tests for classes."""
    van = Car("sprinter", 100)
    van.drive(30)
    print("fuel =", van.fuel)
    print("odometer =", van._odometer)
    van.drive(55)
    print("fuel =", van.fuel)
    print("odometer = ", van._odometer)
    print(van)

    distance = int(input("Distance: "))
    while distance > 0:
        distance_travelled = van.drive(distance)
        print(f"{van} drove {distance_travelled}")
        distance = int(input("Distance: "))


main()
