# find odd number and find the cube of it

lst=[1,2,3,4,5,6,7,8,9,10]
f=list(filter(lambda n:n%2==1,lst))
c=list(map(lambda f:f**3,f))
print(c)