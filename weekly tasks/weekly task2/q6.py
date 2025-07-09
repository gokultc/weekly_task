s1=int(input("enter the lengths of 1st sides"))
s2=int(input("enter the lengths of 2nd sides"))
s3=int(input("enter the lengths of 3rd sides"))

if s1==s2==s3:
    print("This is a equilateral triangle")
elif s1!=s2 and s2!=s3 and s1!=s3:
    print("This is a scalene triangle")
elif s1==s2 or s1==s3 or s2==s3:
    print("This is a isosceles triangle")

