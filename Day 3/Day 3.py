"""
Each square on the grid is allocated in a spiral pattern starting at a location marked 1 and then counting up
while spiraling outward. For example, the first few squares are allocated like this:

17  16  15  14  13
18   5   4   3  12
19   6   1   2  11
20   7   8   9  10
21  22  23---> ...

While this is very space-efficient (no squares are skipped), requested data must be carried back to square 1
(the location of the only access port for this memory system) by programs that can only move up, down, left, or right.
They always take the shortest path: the Manhattan Distance between the location of the data and square 1.


"""
# Note: the bottom right corner is always the square of an odd number (starting from 1).

import math
mynumber = 265149

# Temporary variable to be used later
temp = 1

# The layer of the square which our number is on
layer = 0

# Find the nearest square number near my number, this will help finding the layer
square_of_my_number = math.ceil(math.sqrt(265149))
print(square_of_my_number)

# Find the layer
while temp <= square_of_my_number:
    temp += 2
    layer += 1
print(layer)

# The farthest point from one layer to the center will be its corners.
longest_distance = (layer - 1) * 2


manhattan_distance = longest_distance - (math.pow(square_of_my_number, 2) - mynumber)
print(manhattan_distance)
