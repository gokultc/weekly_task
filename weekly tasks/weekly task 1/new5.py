print("Enter the marks of the subjects")
m1=int(input("Maths :"))
m2=int(input("english :"))
m3=int(input("biology :"))
m4=int(input("zoology :"))
m5=int(input("geography :"))
total=m1+m2+m3+m4+m5
avg=total/5
print("total mark is",total)
if avg>=90:
    print("Grade is s")
elif avg>80:
    print("Grade is A+")
elif avg>70:
    print("Grade is A")
elif avg>60:
    print("Grade is b+")
elif avg>50:
    print("Grade is b")
elif avg>40:
    print("Grade is c+")
elif avg<40:
    print("you have failed...!!")

