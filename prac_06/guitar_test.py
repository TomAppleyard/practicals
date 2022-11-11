from prac_06.guitar_class import Guitar

CURRENT_YEAR = 2022
VINTAGE_AGE = 50


def main():
    my_guitar = Guitar("Acoustic", 1999, 10250)
    print(my_guitar)
    print(my_guitar.is_vintage())


main()
