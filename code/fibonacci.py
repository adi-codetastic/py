def fibonacci(count):
    fib1 = 1
    fib2 = 0
    for i in range(1, count + 1):
        print(fib1)
        temp = fib1
        fib1 = fib1 + fib2
        fib2 = temp


count = int(input("How many fibonacci numbers should i print? "))
fibonacci(count)