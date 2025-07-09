#multiplication of a given number

num=int(input("enter a number:"))

for i in range(1,11,1):
    sum=i*num
    print(i,"x",num,"=",sum) # or else we can directly add the values in it (i,"x",num,"=",i*num)