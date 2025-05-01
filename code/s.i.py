principal = int(input("Enter the Principal: "))
rate = int(input("Enter the rate of interest: "))
time = int(input("Enter the time of interest: "))

si = principal * (rate / 100) * time
amount = principal + si

print("The simple interest = ",si)
print("The amount = ",amount)