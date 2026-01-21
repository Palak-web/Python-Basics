#MAP

def cube(x):
    return x*x*x

l = [1,2,5,4,6]
# newl = []
# for item in l:
#     newl.append(cube(item))

newl = list(map(cube ,l))
print(newl)

#FILTER
def filter_function(a):
    return a>4
newl = list(filter(filter_function,l))
print(newl)

#REDUCE
from functools import reduce

#List of number
numbers = [1,3,4,5,2]

#Calculate the sum of the numbers using the reduce function
sum = reduce(lambda x,y: x + y, numbers)
print(sum)  #print sum