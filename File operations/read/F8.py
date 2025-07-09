f=open("C:/Users/GOKUL/Downloads/temper.unknown",'r')
dic={}
for i in f:
    data=i.rstrip('\n').split(',')
    dist=data[0]
    temp=data[1]
    if dist not in dic:
        dic[dist]=temp
    else:
        old=dic[dist]
        if old>temp:
            dic[dist]=old
        else:
            dic[dist] = temp
for k,v in dic.items():
    print(k,':',v)


