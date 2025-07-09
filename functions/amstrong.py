#121 = 121

n=int(input("enter num"))
temp=n
sum=0

while n>0:
    add=n%10
    n=n//10
    sum+=add**3

if temp==sum:
    print("arm")
else:
    print("not")

