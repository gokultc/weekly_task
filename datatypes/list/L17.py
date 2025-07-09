# LINEAR SEARCH ALGORITHM
# find the element from the list and print if found

lst=[1,3,4,5,6,7,23,54,32,2]
v=int(input("enter the value :"))
flag=0
for i in lst:
    if v==i:
        flag=1
if flag==1:
    print("found")
else:
    print("not found")

# LINEAR SEARCH ALGORITHM
# It is an algorithm that searches and compare each element in the list
# it's drawback is it's time complexity ( takes more time )
# to overcome this we use binary search algorithm