psw=(input("enter the password :"))
check=len(psw)
if check==8:
    if any(char.isdigit() for char in psw):
        print("password is correct")
    else:
        print("please include at least one digit input..!!")
else:
    print("please enter 8 charachters")

