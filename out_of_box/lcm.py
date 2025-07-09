n1=3 #int(input("enter n1 :"))
n2=4 #int(input("enter n2 :"))
if n1>n2:
    greater=n1
else:
    greater=n2
while True:
    if greater%n1==0 and greater%n2==0:
        lcm=greater
        print(lcm)
        break
    else:
        greater+=1



