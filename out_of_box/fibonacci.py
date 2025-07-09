# 0 1 1 2 3 5 8 13...

n=6
sum=0
num1=0
num2=1
print(num1)
print(num2)
for i in range(2,n+1):
    sum=num1+num2
    num1=num2
    num2=sum
    print(sum)

