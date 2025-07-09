low=int(input("enter the number :"))
up=int(input("enter the number :"))
even=0
odd=0
while(low<=up):
    if(low%2==0): 
        even+=low
    else:
        odd+=low
    low+=1

print(even)
print(odd)
