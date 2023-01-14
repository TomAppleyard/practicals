from guitars import Guitars


def main():
    guitars = []
    in_file = open("guitars.csv", 'r')
    for line in in_file:
        parts = line.strip().split(',')
        guitar = Guitars(parts[0], int(parts[1]), float(parts[2]))
        guitars.append(guitar)

    guitars.sort()
    for guitar in guitars:
        print(guitar)

    in_file.close()


main()
