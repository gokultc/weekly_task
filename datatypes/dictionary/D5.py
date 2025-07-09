# first recursive ( repeated ) character in field
# output= B first recursive character

pattern='ABCDBDABCD'
dic={}
for i in pattern:
    if i not in dic:
        dic[i]=1
    else:
        print(i,"first recusive charachter")
        break