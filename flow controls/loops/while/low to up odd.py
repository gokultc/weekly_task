low=int(input("enter the number :"))
up=int(input("enter the number :"))
sum=0
while(low<=up):
    if(low%2==1): #if(low%2!=0) can also be used in this problem
        sum+=low
    low+=1
print(low)