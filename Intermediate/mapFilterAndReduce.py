#MAP

def cube(x):
    return x*x*x

print(cube(2))

l = [1,2,3,4,5]
# newl =[]
# for item in l:
#     newl.append(cube(item))


newl = list(map(cube,l)) #we can pass lambda finctions 
print(newl)

# Filter=========>
def filter_functions(a):
    return a>4

newwl = list(filter(filter_functions,l)) # same we can pass lambda functions 

print(newwl)


#  Reduce =====++++++>

from functools import reduce

numbers = [1,2,3,4,5]

# calculate the sum of the numbers using reduce 

def mysum(x,y):
    return x+y

sum = reduce(mysum,numbers)

print(sum)