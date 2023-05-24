# def cube(x):
#     return x*x*x

# print(cube(2))

li = [1, 3, 4, 5, 6]
# newL = []
# for i in li:
#     newL.append(cube(i))

# print(newL)

# map(functionname, listName)
# newL = list(map(cube, li))
newL = list(map(lambda x: x*x*x, li))
print(newL)

# Filter
# def filter_func(a):
#     return a>4

# newFilter = list(filter(filter_func, li))
newFilter = list(filter(lambda a: a>2, li))
print(newFilter)

# Reduce
from functools import reduce
numbers = [1, 2, 3, 4, 5]

# calculate the sum of the numbers using the reduce function

sum = reduce(lambda x,y: x+y, numbers)
print(sum)