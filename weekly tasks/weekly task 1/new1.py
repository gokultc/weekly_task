name=input("enter your name :")
if name and (name.isalpha() or name[0]=='_'):
    valid=True
    for char in name[1:]:
        if not (name.isalpha() or char=='_'):
            valid=False
            break
    if valid:
        print("valid")
    else:
        print("not valid")
else:
    print("not valid")




