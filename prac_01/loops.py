
for i in range(1, 21, 2):
    print(i, end=' ')
print()

# count in 10s from 0 to 100

for i in range(0, 101, 10):
    print(i, end=' ')
print()

# count down in 1s from 20 to 1

for i in reversed(range(1, 21, 1)):
    print(i, end=' ')
print()

# print inputted number of stars

stars = int(input("No. of stars: "))
for i in range(stars):
    print('*', end=' ')
print('\n')

# print inputted number of stars increasing by one by line

i = 0
while i in range(stars):
    i = i + 1
    print('*' * i)
