# find the prime numbers from the list
# 2,3,5,7,
lst=[1,4,3,7,5,8,9,2,0,12,15,14]
lst1=[]
length=len(lst)
for i in lst:
    if i<1:
        print("not")
    elif i==2:
        lst1.append(i)
    elif i>2:
        for i in range(3,length+1):
            if i%2==0:
               flag=1
            else:
                print("prime")

print(lst1)