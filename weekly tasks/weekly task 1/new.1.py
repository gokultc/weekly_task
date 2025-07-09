name=input("enter your name :")
c=0
flag=0
if name[0].isalpha() or name[0]=='_':
    for char in name[1:]:
        if (char.isalnum() or char=='_'):
            flag=1
if flag>0:
    print("this is  valid name")
else:
    print("this is not valid name")
