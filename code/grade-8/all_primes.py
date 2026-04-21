num = int(input("Enter the number for the prime detection zone. I will find all primes between 1 and your number: "))

for i in range(2, num):

    isComposite = False
    for j in range(2, int(i / 2) + 1):
        if i % j == 0:
            isComposite = True
            break
    if isComposite == False:
        print(i,"is prime")


print("finished")