amount = float(input("Enter the purchase amount: "))
discount = 0.0

if (amount >= 10000):
    discount = 0.15
elif (amount >= 5000):
    discount = 0.10
else:
    discount = 0.0

sell_price = amount * (1 - discount)

print("Discount is: ",discount * 100, "%")
print("The selling price is: ", sell_price)
