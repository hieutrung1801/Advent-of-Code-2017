"""
The captcha requires you to review a sequence of digits (your puzzle input) and find the sum of all digits that match the
next digit in the list. The list is circular, so the digit after the last digit is the first digit in the list."""
f = open("Puzzle.txt", "r")

myNumber = f.readline()
myArray = [int(d) for d in str(myNumber)]

total1 = 0
total2 = 0

array_length = len(myArray)

print(myArray)

print(array_length)


for index, number in enumerate(myArray):
    if index < array_length - 1:
        if myArray[index] == myArray[index + 1]:
            total1 += myArray[index]
    else:
        if myArray[index] == myArray[0]:
            total1 += myArray[0]

"""--- Part Two ---
That is, if your list contains 10 items, only include a digit in your sum if the digit 10/2 = 5 steps forward matches it.
Fortunately, your list has an even number of elements."""
for index, number in enumerate(myArray):
    if index + int(array_length/2) < array_length:
        if myArray[index] == myArray[index + int(array_length/2)]:
            total2 += myArray[index]
    else:
        if myArray[index] == myArray[abs(array_length - index - int(array_length/2))]:
            total2 += myArray[index]

print(total1)
print('This is total 2: ')
print(total2)
