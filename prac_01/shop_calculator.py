item_number = int(input("no. of items: "))
i = 0
total_price = 0
while i in range(item_number):
    i = i + 1
    price = float(input("price of item $: "))
    total_price += price
    print("total price: ${:.2f}". format(total_price))


