""""You're standing in a room with "digitization quarantine" written in LEDs along one wall. The only door is locked, but it includes a small interface. "Restricted Area - Strictly No Digitized Users Allowed."

It goes on to explain that you may only leave by solving a captcha to prove you're not a human. Apparently, you only get one millisecond to solve the captcha: too fast for a normal human, but it feels like hours to you.

The captcha requires you to review a sequence of digits (your puzzle input) and find the sum of all digits that match the next digit in the list. The list is circular, so the digit after the last digit is the first digit in the list.
"""
f = open("Puzzle.txt", "r")
myNumber = f.readline()
myArray = [int(d) for d in str(myNumber)]
print(myArray)
array_length = len(myArray)
print(array_length)
total1 = 0
total2 = 0

for index, number in enumerate(myArray):
    if index < array_length - 1:
        if myArray[index] == myArray[index + 1]:
            total1 += myArray[index]
    else:
        if myArray[index] == myArray[0]:
            total1 += myArray[0]

"""--- Part Two ---

You notice a progress bar that jumps to 50% completion. Apparently, the door isn't yet satisfied, but it did emit a star as encouragement. 
The instructions change:
Now, instead of considering the next digit, it wants you to consider the digit halfway around the circular list.
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
