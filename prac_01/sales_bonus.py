"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
sales = float(input("Sales: "))
while sales >= 0:
    if sales < 1000:
        bonus = 0.1 * sales
        print("Bonus: {:.2f}".format(bonus))
        sales = float(input("choose another value: "))
    if sales >= 1000:
        bonus = 0.15 * sales
        print("Bonus: {:.2f}".format(bonus))
        sales = float(input("choose another value: "))

print("negative sales!")





