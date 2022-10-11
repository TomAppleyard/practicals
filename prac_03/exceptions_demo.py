"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator != 0:
        fraction = numerator / denominator
        print(fraction)
    else:
        print("choose value other than zero!")
        denominator = int(input("Enter the denominator: "))
    except ValueError:
        print("Numerator and denominator must be valid integers!")
    except ZeroDivisionError:
        print("Cannot divide by zero!")
print("Finished.")

# The ValueError could occur with the user input if they don't input an integer
# The ZeroDivisionError could occur if the user inputted zero as the denominator
# Indeed!
