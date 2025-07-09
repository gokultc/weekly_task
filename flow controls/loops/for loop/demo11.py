#sum of even and odd number

low=int(input("enter the lower limit number:"))
upper=int(input("enter the upper limit number:"))
even=0
odd=0
for i in range(low,upper+1):
    if(i%2==0):
        even+=i
    else:
        odd+=i
print("even",even)
print("odd",odd)

