from prac_06.guitar_class import Guitar


def main():
    guitars = []
    name = input("Name: ")
    while name != '':
        year = int(input("Year: "))
        cost = int(input("Cost: "))
        guitar_to_add = Guitar(name, year, cost)
        guitars.append(guitar_to_add)
        name = input("Name: ")
    # guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    # guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    i = 0
    print("These are my guitars: ")
    for guitar in guitars:
        i += 1
        if guitar.is_vintage():
            vintage_string = "(vintage)"
        else:
            vintage_string = ''
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f} {vintage_string}")


main()
