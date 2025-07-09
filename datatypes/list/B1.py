# Implimenting the binary search

lst=[4,5,6,2,3,12,15,10,8]
element=int(input("Enter the element :"))
flag=0
lst.sort()
low=0
upper=len(lst)-1
while low<upper:
    mid = (low + upper) // 2
    if element>lst[mid]:
        low=mid+1
    elif element<lst[mid]:
        upper=mid-1
    elif element==lst[mid]:
        flag=1
        break

if flag==1:
    print("found")
else:
    print("not")