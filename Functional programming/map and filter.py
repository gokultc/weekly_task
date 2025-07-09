# MAP AND FILTER

# MAP

# if every element in a list needed a corresponding value or change in value we use the map function

# lst[1,2,3,4,5,6,7,8,9,10]  f(x)==>[1,4,9,16,25,36,..]

# syntax
# var=list(map(function,iterable))
#            (operation to perform,name of the list)

lst=[1,2,3,4,5]
def sqr(n):
    return n**2
f=list(map(sqr,lst))
#       OR
# f=list(map(lambda n:n**2,lst))
print(f)




# FILTER

# it is used in a list when we need to filter out certain values based on condition

# lst[1,2,3,4,5,6,7,8,9,10] lst()=[2,4,6,8]

# syntax
# var=list(filter(function,iterable))
#              (operation to perform,name of the list)

lst=[1,2,3,4,5]
f=list(filter(lambda n:n%2==0,lst))