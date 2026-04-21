num = int(input("Enter the number for the prime detection zone : "))
isComposite = False
i = 2 

while i < num / 2:
    if num % i == 0:
        isComposite = True
        break
    i  = i + 1

if isComposite:
    print(num,"is composite")
else:
    print(num,"is prime")

print("I stopped at: ", i)
