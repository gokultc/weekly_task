# add 1 to 100 and add even num to even list and find sum and add odd num to odd list and sum
lst=[]
even=[]
odd=[]
for i in range(1,101):
    lst.append(i)
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print(lst)
print(even)
print(odd)

print("sum of list",sum(lst))
print("sum of even",sum(even))
print("sum of odd",sum(odd))

