array = []
mysum = 0
i = 0
with open('Puzzle.txt') as f:
    array = [[int(x) for x in line.split()] for line in f]



def quickSort(alist):
    quickSortHelper(alist, 0, len(alist)-1)

def quickSortHelper(alist, first, last):
    if first < last:

       splitpoint = partition(alist,first,last)

       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)


def partition(alist,first,last):
   pivotvalue = alist[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp


   return rightmark


length = len(array[0])
stop = len(array)
while i < stop:
    quickSort(array[i])
    print(array[i])
    i += 1

# for index, number in enumerate(array[0]):

index = 0
summed = 0
while index < stop:
    summed = 0
    for x in array[index]:
        for y in reversed(array[index]):
            if (y % x == 0) and (x != y) and summed == 0:
                summed = 1;
                print('x and y ' + repr(x) + ' ' + repr(y))
                mysum += y / x
                print(mysum)
    index += 1

print('Even Sum')
print(mysum)
