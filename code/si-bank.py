print("Interest-rates: 0-3 years - 5%; 3-5 years - 8%; above 5 years - 10%")

principal = int(input("Enter the Principal: "))
time = int(input("Enter the time of interest: "))

rate = 10

if (time <= 3):
    rate = 5
elif (time <= 5):
    rate = 8

si = principal * (rate / 100) * time
amount = principal + si

print("rate is: ",rate)
print("The simple interest = ",si)
print("The amount = ",amount)