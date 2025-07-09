# odd number and find the sum
lst=[]
for i in range(1,51):
    if i%2==1:
        lst.append(i)
print(lst)
print(sum(lst))