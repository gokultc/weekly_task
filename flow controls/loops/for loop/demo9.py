#odd number
low=int(input("enter number :"))
upper=int(input("enter number:"))
for i in range(low,upper+1):
    if i%2==1:
        print(i)