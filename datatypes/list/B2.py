# find the logic of lst1 and lst
# lst=[12 ,8 ,3 ,10 ,7 ,15 ,5]
# lst1=[48, 52, 57, 50, 53, 45, 55]


lst=[12,8,3,10,7,15,5]
lst1=[]
sum=sum(lst)
for i in lst:
    j=sum-i
    lst1.append(j)
print(lst1)