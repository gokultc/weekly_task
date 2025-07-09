f=open("C:/Users/GOKUL/Downloads/customer1.txt",'r')
dic={}
for i in f:
    print(i)
    data=i.rstrip('\n').split(',')
    age=data[3]
    prof=data[4]
# maximum age of same profession
#     if prof not in dic:
#         dic[prof]=age
#     else:
#         old=dic[prof]
#         if old<age:
#             dic[prof] = age
#
# for k,v in dic.items():
#     print(k,':',v)

# minimum age
    if prof not in dic:
        dic[prof] = age
    else:
        old = dic[prof]
        if old > age:
            dic[prof] = age

for k, v in dic.items():
    print(k, ':', v)
