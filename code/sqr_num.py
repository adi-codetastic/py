num = int(input("Enter a number to find odd squares from 1 to your number: "))

for i in range(num, 0, -1):
    if i % 2 == 1:
        print("Square of", i,"is",i * i)
    else:
        continue