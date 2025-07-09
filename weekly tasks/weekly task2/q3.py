n1=int(input("Enter the first number :"))
n2=int(input("Enter the second number :"))
n3=int(input("Enter the third number :"))
if  n1>n2 and n1>n3:
    print(n1,"greater")
elif n2>n1 and n2>n3:
    print(n2, "greater")
elif n3>n1 and n3>n2:
    print(n3, "greater")
else:
    print("all are equal numbers ")