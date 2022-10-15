import random

numof_quick_picks = int(input("Number of quick picks: "))
numbers = []

for i in range(numof_quick_picks):
    numbers = []
    for j in range(6):
        number = random.randint(1, 46)
        while number in numbers:
            number = random.randint(1, 46)
        numbers.append(number)
    print(" ".join(f"{number:2}" for number in numbers))


#
# number for number in numbers
# number = (random.randint(1, 46))
# print(number, end=' ')
# LISTS = [number * numof_quick_picks for number in LINE]
# print(LISTS)
