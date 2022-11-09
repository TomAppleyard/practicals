FILENAME = "wimbledon.csv"


def main():
    results = []
    print(FILENAME)
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()  # removes first line read csv file
        for line in in_file:
            parts = line.strip().split(',')
            results.append(parts)
    champion_to_wins, countries = find_champions(results)
    print("Wimbledon Champions:")
    for name, wins in champion_to_wins.items():  # items() returns a list of all the key and values ina dictionary
        print(name, wins)


def find_champions(results):
    champion_to_wins = {}
    countries = set()
    for result in results:
        countries.add(result[1])
        try:
            champion_to_wins[result[2]] += 1
        except KeyError:
            champion_to_wins[result[2]] = 1
    return champion_to_wins, countries


main()
