#fibonoci series

n=int(input("enter the limit :"))
num1=0 #0 and 1 are the default values in the fibonoci series
num2=1
print(num1)
print(num2)
for i in range(3,n+1): #we started 3 because as first 2 values are 0 and one that we have been calculated
    sum=num1+num2
    num1=num2
    num2=sum
    print(sum)

# 0 1 1 2 3 5 8 13..
# (0 1 (0+1) (1+1) (1+2)...