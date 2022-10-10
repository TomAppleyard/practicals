price_per_kWh = float(input("price per kWh (cents): "))
daily_use = float(input("daily use (kWh): "))
billing_days = float(input("number of days in billing period:"))
electricity_bill = price_per_kWh * daily_use * billing_days
print("electricity bill = {:.2f}cents".format(electricity_bill))
