a = float(input("Enter the purchase amount: "))
d = 0.0

if(a >= 10000):
    d = 0.15

elif(a >= 5000):
    d = 0.10

else:
    d = 0.0

s = a * (1 - d)

print("Your discounted price: ",s)