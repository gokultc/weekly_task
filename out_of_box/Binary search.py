lst=[1,4,6,3,0,6,2,1,2,99,53,5,69,8,]
n=4
lst.sort()
print(lst)
low=0
upper=len(lst)-1
mid=(upper+low)//2
for i in lst:
    if n>lst[mid]:
        mid