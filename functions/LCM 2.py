def fun_lcm(x,y):
    if x>y:
        greater=x
    else:
        greater=y
    while True:
        if greater%x==0 and greater%y==0:
            lcm=greater
            return lcm
        else:
            greater+=1

n1=int(input("Enter a number :"))
n2=int(input("Enter a number :"))
print(fun_lcm(n1,n2))
