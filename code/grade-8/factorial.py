def loop_factorial(num):
    fact = 1
    for i in range(2, num + 1):
        fact = fact * i
    return fact


def factorial(num) -> int:
    if num == 1:
        return 1
    return num * factorial(num - 1)


inp = int(input("Enter a number to fint factorial: "))
f = loop_factorial(inp)
print("The factorial by loop is: ", f)

f2 = factorial(inp)
print("The factorial by recursion is: ", f2)