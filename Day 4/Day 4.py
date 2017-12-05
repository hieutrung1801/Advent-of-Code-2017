
array = []
seen = set()
with open('Puzzle.txt') as f:
    array = [[str(x) for x in line.split()] for line in f]
i = 0
stop = len(array)
validCount = 0
print(array[0])
while i < stop:
    for x in array[i]:
        if x not in seen:
            seen.add(x)
    if len(seen) == len(array[i]):
        validCount += 1
    seen.clear()
    i += 1


print(validCount)
