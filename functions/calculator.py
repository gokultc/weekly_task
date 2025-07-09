def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def multi(x,y):
    return x*y
def div(x,y):
    return x/y
x=int(input("Enter the first number :"))
y=int(input("Enter the second number :"))
print("A.addition")
print("B.substration")
print("C.multiplication")
print("D.division")
oper=input("Enter the operation :")
if oper=="A" or "a":
    print("sum=",add(x,y))
elif oper=="B" or oper=="b":
    print("sub=",sub(x,y))
elif oper=="C" or oper=="c":
    print("multi=",multi(x,y))
elif oper=="D" or oper=="d":
    print("div=",div(x,y))

