esum = osum = 0

for i in range(1, 51):
    if i % 2 == 0:
        esum += i
    
    else:
        osum += i


print("The sum of even numbers is :",esum)
print("The sum of odd numbers is :",osum)
