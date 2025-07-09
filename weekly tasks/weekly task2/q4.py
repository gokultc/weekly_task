gender=input("Enter your gender (m,f) :" )
age=int(input("Enter your age :"))
if gender =="m":
    gen=1
else:
    gen=0

if age>=18 or age<30:
    if gen==1:
        print("wage is 700")
    else:
        print("wage is 750")
elif age>=30 or age<=40:
    if gen==1:
        print("wage is 800")
    else:
        print("wage is 850")
