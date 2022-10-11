"""Ask user for name and print it to a file called name.txt"""

name = input("Name: ")

out_file = open("name.txt", 'w+')
print(name, file=out_file)

"""open name.txt and read the name and prints an introduction string"""
name = .readline()
print(f"Your name is {name}")

out_file.close()
