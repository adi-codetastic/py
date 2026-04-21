def smallest(items):
    small = items[0]
    for item in items:
        if item < small:
            small  = item
    return small


items = [3, 10, 20, -23, 15, 20, 21, -77, -1000, -22, 15]

sm = smallest(items)

print("The smallest number in the array is: ", sm)