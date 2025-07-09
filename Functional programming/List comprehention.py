# LIST COMPREHENSION

# used to do the list operations in a single line

# 3 methods

# 1 method: range of element is added into a list

# 2 method: range of element is added into a list based on one condition

# 3 method: range of element is added into a list based on more than one condition

# METHOD 1

# 1 to 20
lst=[]
for i in range(1,21):
    lst.append(i)
print(lst)

# syntax
# var=[ print range ]

# 1 to 10
lst=[i for i in range(1,11)]
print(lst)

#10 to 30
lst=[i for i in range(10,31)]
print(lst)

# 1 to 10
lst=[i**2 for i in range(1,11)]
print(lst)

# element and the square
lst=[(i,i**2) for i in range(1,11)]
print('element and square :',lst)

# METHOD 2

# syntax
# var=[print range condition]

# 1 to 20 range of even number
lst=[i for i in range(1,21) if i%2==0]
print(lst)

# 1 to 50 odd number
lst=[i for i in range(1,51) if i%2==1]
print(lst)

# 1 to 30 even num square
lst=[(i,i**2) for i in range(1,31) if i%2==0]
print(lst)

# METHOD 3
# when there are more than one condition we use the method 3

# syntax
# var=[print1 if condition1 else print2 range]

# var=[print1 if condition1 else print2 if condition2 else print3 range]  ==> there is no elif so we use the multiple if conditions

lst=[(i,i**3) for i in range(1,31) if i%2==1]
print(lst)

# 1 to 25 even square, odd- cube
lst=[(i,i**2) if i%2==0 else (i,i**3) for i in range(1,26)]
print(lst)

# 1, 15 even ==> even
lst=[(i,'even') if i%2==0 else (i,'odd') for i in range(1,16)]
print(lst)

#1 to 50 if 1-16-small, if 16-35- medium , if i>35 - large

lst=[(i,'small') if i<=15 else (i,'medium') if i<=35 else (i,'large')  for i in range(1,51)]
print(lst)
