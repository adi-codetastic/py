# Write an array of integers and sort it in ascending order.
# Input: [9, 7, 8, 3, 2, 1, 5, 4, 6]
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

inp = [9, 7, 8, 3, 2, 1, 5, 4, 6]

print("Input: ", inp)

def adi_sort(input):

    #create a new list to store the sorted integers
    sorted_list = []
    smallest = input[0]
    smPos = 0
    for j in range(len(input)):
        for i in range(len(input)):
            if input[i] < smallest:
                smallest = input[i]
                smPos = i
        print("Smallest: ", smallest)
        input.pop(smPos)

adi_sort(inp)
