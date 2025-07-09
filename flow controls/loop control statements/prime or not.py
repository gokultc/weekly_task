# prime or not

num=int(input("enter the number :"))
if(num<0):
    print("please enter a positive number..")
elif(num==0):
    print("you have entered zero")
elif (num==1):
    print("one is comosite number")
else:
    for i in range(2,num): # 2 is here because every number will be divisible
        if(num%i==0):
            print("it is not prime")
            break
    else:
        #this else part is paired with the for loop, not the if statement
        print(num,"is a prime number")