FILENAME = "wimbledon.csv"
wimbledons = []
champions = []


def main():
    wimbledons = format_data(FILENAME)


def find_champions(wimbledons):
    champion_to_wins = {}
    countries = set()
    for wimbledon in wimbledons:
        countries.add(wimbledon[1])
        champion_to_wins[wimbledon[2]=wins]


def format_data(FILENAME):
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        wimbledon = [line.strip() for line in in_file]
        for part in wimbledon:
            wimbledon = part.split(',')
            wimbledons.append(wimbledon)
    return wimbledons
    #     in_file.readline()
    #     for line in in_file:
    #         wimbledon = line.strip().strip(',')
    #         wimbledons.append(wimbledon)
    # return wimbledons


main()
