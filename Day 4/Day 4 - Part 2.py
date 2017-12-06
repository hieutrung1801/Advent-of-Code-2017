import collections
compare = lambda x, y: collections.Counter(x) == collections.Counter(y)
array = []
temp_array = []
array2 = []
with open('Puzzle.txt') as f:
    array = [[str(x) for x in line.split()] for line in f]

i = 0
invalid = 0
validCount = 0
stop = len(array)
y = 0
while y < stop:
    print(y)
    for x in array[y]:
        temp_array = list(x)
        array2.append(temp_array)
    for x in array2:
        for i in range(0, len(array2)):
            if array2.index(x) != i and compare(x, array2[i]) is True:
                invalid = 1
    if invalid == 0:
        validCount += 1
    temp_array.clear()
    array2.clear()
    invalid = 0
    y += 1
print(validCount)
