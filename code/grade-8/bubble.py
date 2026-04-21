# Write an array of integers and sort it in ascending order.
# Input: [9, 7, 8, 3, 2, 1, 5, 4, 6]
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

inp = [9, 7, 8, 3, 2, 1, 5, 4, 6]

print("Input: ", inp)

def bubble(input):
    for i in range(len(input)):
        for j in range(len(input) - 1):
            if input[i] < input[j]:
                input[i], input[j] = input[j], input[i]
    print("Output: ", input)

bubble(inp)