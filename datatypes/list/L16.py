# count number of consonant >> other letters other than the vovels (a,e,i,o,u)

string='luminartecnolab'
vovels='a,e,i,o,u,A,E,I,O,U'
lst=[]
for i in string:
    if i not in vovels:
        lst.append(i)

print(len(lst))
print(len(string))
print()

