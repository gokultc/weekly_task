#method 3 - single line swapping

num1,num2,num3,num4=10,20,30,40    #it is possible to define values in a single line

print(num4)
print(num2)

num1=10
num2=20

print("before swapping")
print("number1 is ",num1)
print("number2 is",num2)

num1,num2=num2,num1                 #single line swapping

print("after swapping")

print("number1",num1)
print("number2",num2)

