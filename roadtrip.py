miles = int(input("how many miles will you be traveling?"))
fuel = int (input("what is your car's fuel effecentcy (MPG)"))
gas = 3.15
gallons = miles / fuel
final_price = gallons * gas
print("your total price will be:")
print(final_price)