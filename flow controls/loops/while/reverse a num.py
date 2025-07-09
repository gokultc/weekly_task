num=int(input("enter the number :"))
rev=0
while(num>0):
    mod=num%10
    rev=(rev*10)+mod
    num=num//10
    print(num)
    print(mod)
print(rev)
