evenSum = oddSum = 0

for i in range(1, 51):
    if i % 2 == 0:
        evenSum += i
    else:
        oddSum += i
print("The sum of even numbers is :",evenSum)
print("The sum of odd numbers is :",oddSum)
