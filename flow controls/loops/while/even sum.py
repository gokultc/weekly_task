low=int(input("enter the number :"))
up=int(input("enter the number :"))
sum=0
while(low<=up):
    if(low%2==0):
        sum+=low
    low+=1
print(sum)
