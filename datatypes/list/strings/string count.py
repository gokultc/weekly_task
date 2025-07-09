# vovels >>aeiou
vovels='a,e,i,o,u,A,E,I,O,U'
lst=[]
string='luminartecnolab'
for i in string:
    if i in vovels:
        lst.append(i)

print(len(lst))