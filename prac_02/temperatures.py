"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""


def main():
    """main function for converting values between celsius and fahrenheit"""
    menu = """C - Convert Celsius to Fahrenheit
    F - Convert Fahrenheit to Celsius
    Q - Quit"""
    print(menu)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            convert_to_fahrenheit()
        elif choice == "F":
            convert_to_celsius()
        else:
            print("Invalid option")
        print(menu)
        choice = input(">>> ").upper()
    print("you have quit")


def convert_to_celsius():
    """Converts a value to fahrenheit. """
    fahrenheit = float(input("Fahrenheit: "))
    celsius = 5 / 9 * (fahrenheit - 32)
    print("Results: {:.2f} celsius".format(celsius))


def convert_to_fahrenheit():
    """ Converts a value to fahrenheit. """
    celsius = float(input("Celsius: "))
    fahrenheit = celsius * 9.0 / 5 + 32
    print("Result: {:.2f} F".format(fahrenheit))


main()
