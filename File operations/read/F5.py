f=open('C:/Users/GOKUL/Downloads/sample4.txt','r')
for i in f:
    data=i.rstrip('/n').split(',')

# print the data of person age above 23
    age=data[3]
    if age>'23':
        print(i)

# age =21 and print fname,lname,age,phnno
    age=data[3]
    if age=='21':
        print(data[1],data[2],data[3],data[4])

if loc in Chennai:
    loc = data[5]
    if loc=="Chennai":
        print(data[1],data[2],data[3])

# print if age >23 and loc at Chennai
    age=data[3]
    loc=data[5]
    if age>='23' and loc=='Chennai':
        print(data[1],data[2],data[3],data[4])
