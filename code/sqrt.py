propertyOne = "Property 1 : Numbers ending with 2, 3, 7 or 8 is never a perfect square."
propertyThree = "Property 3 : If a number when divided by 3 gives a remainder 2, then it is not a perfect square."
propertyFour = "Property 4 : If a number when divided by 4 gives a remainder 2 or 3, then it is not a perfect square."

print("This calculator will evaluate your entered number against known properties of perfect square. If any property is violated, it will be highlighted. Below are the properties.")


print (propertyOne)
print (propertyThree)
print (propertyFour)
print("To exit the program, enter a number less than 0.")

num = int(input("Enter a number: "))

while (num > 0):
    isAnyPropertyViolated = False

    if(num % 10 == 2 or num % 10 == 3 or num % 10 == 7 or num % 10 == 8):
        print("Your number violates property 1.")
        isAnyPropertyViolated = True

    if(num % 3 == 2):
        print("Your number violates property 3.")
        isAnyPropertyViolated = True

    if(num % 4 == 2 or num % 4 == 3):
        print("Your number violates property 4.")
        isAnyPropertyViolated = True

    if (isAnyPropertyViolated == False):
        print ("No properties have been violated.")

    num = int(input("Enter a number: "))
