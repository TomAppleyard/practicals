"""Ask user for name and print it to a file called name.txt"""

name = input("Name: ")

out_file = open("name.txt", 'w+')
print(name, file=out_file)

out_file.close()

"""open name.txt and read the name and prints an introduction string"""

in_file = open("name.txt", 'r')
name = in_file.readline()
print(f"Your name is {name}")

in_file.close()

"""write numbers to a txt file in rows then add the first two numbers"""

out_file = open("numbers.txt", 'w+')
print("17\n42\n400", file=out_file)
out_file.close()

in_file = open("numbers.txt", 'r')
number1 = int(in_file.readline())
number2 = int(in_file.readline())
print(number1 + number2)

"""read and add all numbers in txt file"""

total = 0
in_file = open("numbers.txt", 'r')
for line in in_file:
    number = int(line)
    total += number
print(total)



