#sum of even numbers

low=int(input("enter low number:"))
upper=int(input("enter upper number:"))
sum=0
for i in range(low,upper+1):
    if(i%2==0):
        sum+=i
print(sum)